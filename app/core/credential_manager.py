"""Credential manager for secure handling of Facebook credentials."""

import os
import json
import getpass
from typing import Optional, Tuple
from pathlib import Path
import logging
from cryptography.fernet import Fernet
import base64

logger = logging.getLogger(__name__)


class CredentialManager:
    """Manages Facebook credentials securely with session caching."""
    
    def __init__(self):
        self.session_file = Path(".facebook_session")
        self.key_file = Path(".session_key")
        self._cached_credentials = None
    
    def _get_or_create_key(self) -> bytes:
        """Get or create encryption key for session data."""
        if self.key_file.exists():
            with open(self.key_file, 'rb') as f:
                return f.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as f:
                f.write(key)
            return key
    
    def _encrypt_data(self, data: str) -> str:
        """Encrypt sensitive data."""
        key = self._get_or_create_key()
        f = Fernet(key)
        encrypted = f.encrypt(data.encode())
        return base64.b64encode(encrypted).decode()
    
    def _decrypt_data(self, encrypted_data: str) -> str:
        """Decrypt sensitive data."""
        try:
            key = self._get_or_create_key()
            f = Fernet(key)
            encrypted_bytes = base64.b64decode(encrypted_data.encode())
            decrypted = f.decrypt(encrypted_bytes)
            return decrypted.decode()
        except Exception as e:
            logger.warning(f"Failed to decrypt data: {e}")
            return None
    
    def save_session_credentials(self, email: str, password: str) -> None:
        """Save credentials for current session (encrypted)."""
        try:
            session_data = {
                'email': self._encrypt_data(email),
                'password': self._encrypt_data(password),
                'timestamp': str(os.path.getmtime(self.session_file) if self.session_file.exists() else 0)
            }
            
            with open(self.session_file, 'w') as f:
                json.dump(session_data, f)
            
            # Cache in memory for current session
            self._cached_credentials = (email, password)
            
            logger.info("✅ Credenciales guardadas para esta sesión")
            
        except Exception as e:
            logger.error(f"Error saving session credentials: {e}")
    
    def load_session_credentials(self) -> Optional[Tuple[str, str]]:
        """Load credentials from current session if available."""
        # First check memory cache
        if self._cached_credentials:
            return self._cached_credentials
        
        # Then check session file
        if not self.session_file.exists():
            return None
        
        try:
            with open(self.session_file, 'r') as f:
                session_data = json.load(f)
            
            email = self._decrypt_data(session_data['email'])
            password = self._decrypt_data(session_data['password'])
            
            if email and password:
                # Cache in memory
                self._cached_credentials = (email, password)
                logger.info("✅ Credenciales cargadas desde sesión anterior")
                return (email, password)
            
        except Exception as e:
            logger.warning(f"Could not load session credentials: {e}")
        
        return None
    
    def get_credentials(self) -> Tuple[str, str]:
        """Get Facebook credentials from various sources."""
        # Try to load from session first
        credentials = self.load_session_credentials()
        if credentials:
            return credentials
        
        # Try environment variables
        email = os.getenv('FACEBOOK_EMAIL')
        password = os.getenv('FACEBOOK_PASSWORD')
        
        if email and password:
            logger.info("✅ Using credentials from environment variables")
            self.save_session_credentials(email, password)
            return (email, password)
        
        # Prompt user for credentials
        print("\n🔐 Facebook credentials required")
        email = input("Email: ").strip()
        password = getpass.getpass("Password: ")
        
        if email and password:
            self.save_session_credentials(email, password)
            return (email, password)
        
        raise ValueError("No valid credentials provided")
    
    def clear_session(self) -> None:
        """Clear saved session data."""
        try:
            if self.session_file.exists():
                self.session_file.unlink()
            if self.key_file.exists():
                self.key_file.unlink()
            self._cached_credentials = None
            logger.info("✅ Session data cleared")
        except Exception as e:
            logger.error(f"Error clearing session: {e}")