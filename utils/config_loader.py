# -*- coding: utf-8 -*-
import os
import json
import logging
from typing import Dict, Any, List, Optional, Tuple
from threading import Lock # Added for cache lock
import base64 # Added for key encoding
import hashlib # Added for key derivation
from cryptography.fernet import Fernet, InvalidToken # Added for encryption
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from utils.logging_utils import setup_logger
from werkzeug.security import generate_password_hash, check_password_hash

# --- Imports may need adjusting based on final directory structure ---
# We need to do this import here to avoid import errors. 
# The config_manager module imports from this file.
from utils.logging_utils import setup_logger

# Logger for config operations
logger = setup_logger('ddc.config_loader', level=logging.DEBUG)

# Note: This file now contains default configurations and validation logic,
# but delegates actual loading/saving to the ConfigManager

# --- Constants for Encryption ---
_TOKEN_ENCRYPTION_SALT = b'ddc-salt-for-token-encryption-key-v1' # CHANGE THIS if you need to invalidate all old keys
_PBKDF2_ITERATIONS = 260000 # Number of iterations for PBKDF2

# --- Load Configuration ---
_CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_DIR = os.path.abspath(os.path.join(_CURRENT_DIR, "..", "config"))

# Configuration files
BOT_CONFIG_FILE = os.path.join(CONFIG_DIR, "bot_config.json")
DOCKER_CONFIG_FILE = os.path.join(CONFIG_DIR, "docker_config.json")
CHANNELS_CONFIG_FILE = os.path.join(CONFIG_DIR, "channels_config.json")
WEB_CONFIG_FILE = os.path.join(CONFIG_DIR, "web_config.json")

# Ensure that the configuration directory exists
try:
    os.makedirs(CONFIG_DIR, exist_ok=True)
    print(f"CONFIG_LOADER: Ensured config directory exists: {CONFIG_DIR}")
except OSError as e:
    print(f"CONFIG_LOADER: Warning - Could not create config directory {CONFIG_DIR}: {e}")

# Default configurations for split files
DEFAULT_BOT_CONFIG = {
    "bot_token": None,
    "guild_id": None,
    "language": "en", # Language setting for the bot
    "timezone": "Europe/Berlin",
    "heartbeat_channel_id": None,
}

DEFAULT_DOCKER_CONFIG = {
    "servers": [],
    "docker_list_refresh_seconds": 60,
}

DEFAULT_CHANNELS_CONFIG = {
    "channel_permissions": {},
    "default_channel_permissions": {
        "commands": {
            "serverstatus": True,
            "command": False,
            "control": False,
            "schedule": False
        },
        "post_initial": False,
        "update_interval_minutes": 10,
        "inactivity_timeout_minutes": 10,
        "enable_auto_refresh": True,
        "recreate_messages_on_inactivity": True
    }
}

DEFAULT_WEB_CONFIG = {
    "web_ui_user": "admin",
    "web_ui_password_hash": generate_password_hash("admin", method="pbkdf2:sha256"),
    "scheduler_debug_mode": False  # Default to false for production systems
}

# Combined default configuration for compatibility and bot language
DEFAULT_CONFIG = {
    **DEFAULT_BOT_CONFIG, # Contains bot language
    **DEFAULT_DOCKER_CONFIG,
    **DEFAULT_CHANNELS_CONFIG,
    **DEFAULT_WEB_CONFIG
}

class ConfigError(Exception):
    """Custom exception class for configuration errors."""
    pass

def validate_server_config(server_data: Dict[str, Any]) -> bool:
    """Validates a server configuration dictionary."""
    required_keys = ["name", "docker_name", "allowed_actions"]
    
    # Check required keys
    for key in required_keys:
        if key not in server_data:
            print(f"VALIDATE_SERVER: Missing required key '{key}'")
            return False
    
    # Validate name and docker_name
    if not isinstance(server_data.get("name"), str) or not server_data.get("name"):
        print("VALIDATE_SERVER: Invalid or empty 'name'")
        return False
    
    if not isinstance(server_data.get("docker_name"), str) or not server_data.get("docker_name"):
        print("VALIDATE_SERVER: Invalid or empty 'docker_name'")
        return False
    
    # Validate allowed_actions
    allowed_actions = server_data.get("allowed_actions")
    if not isinstance(allowed_actions, list):
        print("VALIDATE_SERVER: 'allowed_actions' must be a list")
        return False
    
    valid_actions = ["status", "start", "stop", "restart"]
    for action in allowed_actions:
        if not isinstance(action, str) or action not in valid_actions:
            print(f"VALIDATE_SERVER: Invalid action '{action}' in 'allowed_actions'")
            return False
    
    return True

# For backward compatibility, we use ConfigManager import and functions here
# This avoids changing all the code using these functions
def load_config() -> Dict[str, Any]:
    """
    Loads the configuration from the ConfigManager.
    Uses a cache for subsequent calls.
    
    Returns:
        Dictionary with complete configuration
    """
    # Import here to avoid circular imports
    from utils.config_manager import get_config_manager
    
    # Get config from the ConfigManager
    return get_config_manager().get_config()

def save_config(config_data: Dict[str, Any]) -> bool:
    """
    Saves the configuration using the ConfigManager.
    
    Args:
        config_data: Configuration dictionary to save
        
    Returns:
        bool: Success or failure
    """
    # Import here to avoid circular imports
    from utils.config_manager import get_config_manager
    
    # Use the ConfigManager to save
    return get_config_manager().save_config(config_data)

def get_server_config(server_name: str) -> Optional[Dict[str, Any]]:
    """Gets the configuration for a specific server from the cached config."""
    # Import here to avoid circular imports
    from utils.config_manager import get_config_manager
    
    # Use the ConfigManager to get server config
    return get_config_manager().get_server_config(server_name)

def update_server_config(server_name: str, new_config_data: Dict[str, Any]) -> bool:
    """Updates the configuration for a specific server and saves the whole config."""
    # Import here to avoid circular imports
    from utils.config_manager import get_config_manager
    
    # Use the ConfigManager to update server config
    return get_config_manager().update_server_config(server_name, new_config_data)

def process_config_form(form_data, current_config: Dict[str, Any]) -> Tuple[Dict[str, Any], bool, str]:
    """
    Process a configuration form submission.
    
    Args:
        form_data: Form data submitted by user
        current_config: Current configuration
        
    Returns:
        Tuple of (new_config, success, message)
    """
    # This function remains in config_loader since it contains a lot of form-specific logic
    # that doesn't make sense to move to the core ConfigManager
    print(f"[CONFIG-DEBUG] process_config_form called with {len(form_data)} form fields")
    print(f"[CONFIG-DEBUG] Form data keys: {list(form_data.keys())[:20]}...")  # First 20 keys
    try:
        new_config = current_config.copy()
        
        # Bot-specific settings (including bot language)
        if 'language' in form_data: # This is now the bot language
            language = form_data['language']
            if isinstance(language, list): language = language[0] if language else ''
            if language in ['en', 'de', 'fr']:
                new_config['language'] = language
            else:
                return current_config, False, "Invalid bot language selected"
        
        if 'timezone' in form_data:
            timezone = form_data['timezone']
            if isinstance(timezone, list): timezone = timezone[0] if timezone else ''
            new_config['timezone'] = timezone
        
        # ... (Rest of process_config_form logic remains, but without explicit Web-UI language processing) ...
        
        # Guild ID
        if 'guild_id' in form_data:
            guild_id = form_data['guild_id']
            if isinstance(guild_id, list): guild_id = guild_id[0] if guild_id else ''
            guild_id = str(guild_id).strip()
            if guild_id:
                if not guild_id.isdigit() or len(guild_id) < 17:
                    return current_config, False, "Guild ID appears invalid"
                new_config['guild_id'] = guild_id
            else:
                new_config['guild_id'] = None
        
        # Heartbeat Channel ID
        if 'heartbeat_channel_id' in form_data:
            heartbeat_id = form_data['heartbeat_channel_id']
            if isinstance(heartbeat_id, list): heartbeat_id = heartbeat_id[0] if heartbeat_id else ''
            heartbeat_id = str(heartbeat_id).strip()
            if heartbeat_id:
                if not heartbeat_id.isdigit():
                    return current_config, False, "Heartbeat channel ID must be numeric"
                new_config['heartbeat_channel_id'] = heartbeat_id
            else:
                new_config['heartbeat_channel_id'] = None

        # Docker Config
        if 'docker_list_refresh_seconds' in form_data:
            try:
                refresh_seconds = int(form_data['docker_list_refresh_seconds'])
                new_config['docker_list_refresh_seconds'] = max(10, refresh_seconds)
            except (ValueError, TypeError):
                return current_config, False, "Invalid docker list refresh interval"

        # Server Config (detailed logic from before)
        server_order_str = form_data.get('server_order', '')
        selected_servers_form = form_data.getlist('selected_servers') if hasattr(form_data, 'getlist') else form_data.get('selected_servers', [])
        if isinstance(selected_servers_form, str): # In case it comes as a string
            selected_servers_form = [s.strip() for s in selected_servers_form.split(',') if s.strip()]

        ordered_docker_names = [name.strip() for name in server_order_str.split('__,__') if name.strip()] if server_order_str else []
        selected_docker_names_set = set(selected_servers_form)
        
        new_server_list = []
        final_server_order = ordered_docker_names if ordered_docker_names else selected_servers_form

        # DEBUG: Show all allow_* keys in form_data
        allow_keys = [key for key in form_data.keys() if key.startswith('allow_')]
        print(f"[CONFIG-DEBUG] All allow_* keys in form_data: {allow_keys}")
        logger.info(f"[CONFIG] All allow_* keys in form_data: {allow_keys}")
        print(f"[CONFIG-DEBUG] Processing servers in order: {final_server_order}")
        logger.info(f"[CONFIG] Processing servers in order: {final_server_order}")

        for idx, docker_name in enumerate(final_server_order):
            if docker_name in selected_docker_names_set:
                display_name_val = form_data.get(f'display_name_{docker_name}', docker_name)
                display_name = display_name_val[0] if isinstance(display_name_val, list) else str(display_name_val).strip()
                if not display_name: display_name = docker_name
                
                allowed_actions = []
                for act in ['status', 'start', 'stop', 'restart']:
                    # CRITICAL FIX: The template uses container.name (which is docker_name) for checkbox names
                    # but the form data key needs to match what the template generates
                    action_flag = form_data.get(f'allow_{act}_{docker_name}')
                    
                    # IMPROVED: Try multiple fallback strategies for finding the checkbox
                    if action_flag is None and ' ' in docker_name:
                        alternative_name = docker_name.replace(' ', '_')
                        action_flag = form_data.get(f'allow_{act}_{alternative_name}')
                        if action_flag is not None:
                            logger.info(f"[CONFIG] Found checkbox with alternative name: allow_{act}_{alternative_name}")
                    
                    # If still not found, try to find any matching key (case-insensitive)
                    if action_flag is None:
                        # Look for any key that matches the pattern (case-insensitive)
                        for key in form_data.keys():
                            if key.lower() == f'allow_{act}_{docker_name}'.lower():
                                action_flag = form_data.get(key)
                                logger.info(f"[CONFIG] Found checkbox with case-insensitive match: {key}")
                                break
                    
                    # IMPROVED: Try with all special characters replaced with underscores
                    if action_flag is None:
                        sanitized_name = ''.join(c if c.isalnum() else '_' for c in docker_name)
                        sanitized_key = f'allow_{act}_{sanitized_name}'
                        action_flag = form_data.get(sanitized_key)
                        if action_flag is not None:
                            logger.info(f"[CONFIG] Found checkbox with sanitized name: {sanitized_key}")
                    
                    # ENHANCED DEBUG: Log what we're looking for and what we found
                    print(f"[CONFIG-DEBUG] Looking for checkbox: allow_{act}_{docker_name}")
                    logger.info(f"[CONFIG] Looking for checkbox: allow_{act}_{docker_name}")
                    print(f"[CONFIG-DEBUG] Found value: {action_flag} (type: {type(action_flag)})")
                    logger.info(f"[CONFIG] Found value: {action_flag} (type: {type(action_flag)})")
                    
                    # IMPROVED: Handle different value types more robustly
                    if action_flag is not None:
                        # Handle list values (from FormData)
                        if isinstance(action_flag, list):
                            action_flag = action_flag[0] if action_flag else None
                        
                        # Convert to string for comparison
                        action_flag_str = str(action_flag).lower() if action_flag is not None else None
                        
                        # Check if action is allowed
                        if action_flag_str in ['1', 'on', 'true', 'yes']:
                            allowed_actions.append(act)
                            print(f"[CONFIG-DEBUG] Action '{act}' ALLOWED for '{docker_name}' (value: {action_flag})")
                            logger.info(f"[CONFIG] Action '{act}' ALLOWED for '{docker_name}' (value: {action_flag})")
                        elif action_flag_str in ['0', 'off', 'false', 'no']:
                            print(f"[CONFIG-DEBUG] Action '{act}' DENIED for '{docker_name}' (value: {action_flag})")
                            logger.info(f"[CONFIG] Action '{act}' DENIED for '{docker_name}' (value: {action_flag})")
                        else:
                            print(f"[CONFIG-DEBUG] Action '{act}' UNKNOWN VALUE for '{docker_name}' (value: {action_flag})")
                            logger.warning(f"[CONFIG] Action '{act}' UNKNOWN VALUE for '{docker_name}' (value: {action_flag})")
                    else:
                        print(f"[CONFIG-DEBUG] Action '{act}' NOT FOUND for '{docker_name}'")
                        logger.warning(f"[CONFIG] Action '{act}' NOT FOUND for '{docker_name}'")
                
                # DEBUG: Log the final allowed_actions
                print(f"[CONFIG-DEBUG] Container '{docker_name}' final allowed_actions: {allowed_actions}")
                logger.info(f"[CONFIG] Container '{docker_name}' final allowed_actions: {allowed_actions}")
                
                server_entry = {
                    "name": display_name, 
                    "docker_name": docker_name, 
                    "allowed_actions": allowed_actions,
                    "order": idx  # Save the order as a field in the server configuration
                }
                if not validate_server_config(server_entry):
                    return current_config, False, f"Invalid configuration for server '{docker_name}'"
                new_server_list.append(server_entry)
        
        # Store the server_order directly in the main configuration
        # This makes it easier to maintain the order even if servers are added/removed
        new_config['server_order'] = final_server_order
        
        # Save server order to separate file for better persistence
        try:
            from utils.server_order import save_server_order
            save_server_order(final_server_order)
            print(f"SERVER_ORDER: Saved order to dedicated file: {final_server_order}")
        except Exception as e:
            print(f"SERVER_ORDER: Error saving to dedicated file: {e}")
        
        # Sort server list by order explicitly
        new_server_list.sort(key=lambda s: s.get('order', 999))
        new_config['servers'] = new_server_list

        # Channel Permissions (detailed logic from before)
        channel_permissions = {}
        found_indices = set()
        for key_form in form_data:
            if key_form.startswith('channel_id_'):
                try: found_indices.add(int(key_form.split('_')[-1]))
                except ValueError: pass
        if 'channels_count' in form_data: # For tests
            try:
                for i in range(1, int(form_data.get('channels_count', '0')) + 1):
                    if f'channel_{i}_id' in form_data: found_indices.add(i)
            except (ValueError, TypeError): pass

        for index in sorted(list(found_indices)):
            channel_id_val = form_data.get(f'channel_id_{index}', '')
            channel_id = channel_id_val[0].strip() if isinstance(channel_id_val, list) and channel_id_val else str(channel_id_val).strip()
            if not channel_id.isdigit(): continue

            channel_name_val = form_data.get(f'channel_name_{index}', '')
            channel_name = channel_name_val[0].strip() if isinstance(channel_name_val, list) and channel_name_val else str(channel_name_val).strip()
            if not channel_name: channel_name = f'Channel {channel_id}'

            commands = {}
            for cmd_key in ['serverstatus', 'command', 'control', 'schedule']:
                cmd_val = form_data.get(f'cmd_{cmd_key}_{index}') or form_data.get(f'channel_{index}_commands_{cmd_key}')
                commands[cmd_key] = cmd_val in ['1', 'on', 'true', True, 'True']

            def get_bool_form_val(key_prefix, default_val):
                val = form_data.get(f'{key_prefix}_{index}') or form_data.get(f'channel_{index}_{key_prefix}')
                return (val in ['1', 'on', 'true', True, 'True']) if val is not None else default_val

            def get_int_form_val(key_prefix, default_val, min_val=1):
                val_str = form_data.get(f'{key_prefix}_{index}') or form_data.get(f'channel_{index}_{key_prefix}')
                try: return max(min_val, int(val_str)) if val_str is not None else default_val
                except (ValueError, TypeError): return default_val

            channel_permissions[channel_id] = { 
                'name': channel_name, 
                'commands': commands, 
                'post_initial': get_bool_form_val('post_initial', False),
                'update_interval_minutes': get_int_form_val('update_interval_minutes', 10),
                'inactivity_timeout_minutes': get_int_form_val('inactivity_timeout_minutes', 10, min_val=0),
                'enable_auto_refresh': get_bool_form_val('enable_auto_refresh', True),
                'recreate_messages_on_inactivity': get_bool_form_val('recreate_messages_on_inactivity', True)
            }
        new_config['channel_permissions'] = channel_permissions
        new_config['default_channel_permissions'] = DEFAULT_CHANNELS_CONFIG['default_channel_permissions'] # Always set default here for now

        # Web UI User / Password
        if 'web_ui_user' in form_data:
            web_user = form_data['web_ui_user']
            new_config['web_ui_user'] = web_user[0].strip() if isinstance(web_user, list) and web_user else str(web_user).strip()

        # Scheduler Debug Mode
        scheduler_debug = form_data.get('scheduler_debug_mode', '0')
        new_config['scheduler_debug_mode'] = scheduler_debug in ['1', 'on', 'true', True, 'True']

        if 'new_web_ui_password' in form_data:
            password_val = form_data['new_web_ui_password']
            password = password_val[0].strip() if isinstance(password_val, list) and password_val else str(password_val).strip()
            if password: # Only if a new password was specified
                confirm_val = form_data.get('confirm_web_ui_password', '')
                confirm_password = confirm_val[0].strip() if isinstance(confirm_val, list) and confirm_val else str(confirm_val).strip()
                if password != confirm_password:
                    return current_config, False, "Passwords do not match"
                new_config['new_web_ui_password'] = password # Temp key for save_config
            elif 'new_web_ui_password' in new_config: # Remove old temp key if field is empty
                del new_config['new_web_ui_password']

        # Bot Token
        if 'bot_token' in form_data:
            token_val = form_data['bot_token']
            token = token_val[0].strip() if isinstance(token_val, list) and token_val else str(token_val).strip()
            if token:
                new_config['bot_token'] = token
        
        return new_config, True, "Configuration processed successfully."
    except Exception as e:
        print(f"PROCESS_CONFIG_FORM: Error processing form data: {e}")
        return current_config, False, "An error occurred while processing the configuration."
