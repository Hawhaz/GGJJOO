#!/usr/bin/env python3
"""
Facebook Marketplace Agent - Professional Edition Setup

Professional setup script with comprehensive checks and configuration.
"""

import os
import sys
import subprocess
import json
from pathlib import Path
from typing import Dict, List, Optional

# Version and metadata
VERSION = "2.0.0"
AUTHOR = "Professional Automation Team"
DESCRIPTION = "Advanced Facebook Marketplace automation with professional-grade modules"

# Color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_colored(message: str, color: str = Colors.OKGREEN) -> None:
    """Print colored message to terminal."""
    print(f"{color}{message}{Colors.ENDC}")

def print_header(message: str) -> None:
    """Print header message."""
    print_colored(f"\n{'='*60}", Colors.HEADER)
    print_colored(f"{message.center(60)}", Colors.HEADER)
    print_colored(f"{'='*60}", Colors.HEADER)

def check_python_version() -> bool:
    """Check if Python version is compatible."""
    print_colored("\n🐍 Checking Python version...", Colors.OKBLUE)
    
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print_colored(f"❌ Python {version.major}.{version.minor} is not supported.", Colors.FAIL)
        print_colored("   Minimum required: Python 3.8+", Colors.WARNING)
        return False
    
    print_colored(f"✅ Python {version.major}.{version.minor}.{version.micro} - Compatible", Colors.OKGREEN)
    return True

def install_requirements() -> bool:
    """Install required packages."""
    print_colored("\n📦 Installing requirements...", Colors.OKBLUE)
    
    requirements_file = Path("requirements.txt")
    if not requirements_file.exists():
        print_colored("❌ requirements.txt not found!", Colors.FAIL)
        return False
    
    try:
        subprocess.run([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ], check=True, capture_output=True, text=True)
        print_colored("✅ Requirements installed successfully", Colors.OKGREEN)
        return True
    except subprocess.CalledProcessError as e:
        print_colored(f"❌ Failed to install requirements: {e}", Colors.FAIL)
        return False

def install_playwright_browsers() -> bool:
    """Install Playwright browsers."""
    print_colored("\n🌐 Installing Playwright browsers...", Colors.OKBLUE)
    
    try:
        # Install Playwright browsers
        subprocess.run([
            sys.executable, "-m", "playwright", "install", "chromium"
        ], check=True, capture_output=True, text=True)
        
        print_colored("✅ Playwright browsers installed successfully", Colors.OKGREEN)
        return True
    except subprocess.CalledProcessError as e:
        print_colored(f"❌ Failed to install Playwright browsers: {e}", Colors.FAIL)
        print_colored("   Try running manually: playwright install chromium", Colors.WARNING)
        return False
    except FileNotFoundError:
        print_colored("❌ Playwright not found. Installing requirements first...", Colors.WARNING)
        return False

def create_config_file() -> bool:
    """Create default configuration file."""
    print_colored("\n⚙️  Creating configuration files...", Colors.OKBLUE)
    
    # Create .env.example if it doesn't exist
    env_example = Path(".env.example")
    if not env_example.exists():
        env_content = """# Facebook Marketplace Agent Configuration
# Copy this file to .env and fill in your values

# Facebook Credentials (Optional - will prompt if not provided)
FACEBOOK_EMAIL=your_email@example.com
FACEBOOK_PASSWORD=your_password

# Browser Settings
HEADLESS=false
BROWSER_TIMEOUT=30000

# Behavior Settings
BEHAVIOR_PROFILE=normal
TYPING_SPEED=medium

# Image Settings
MAX_IMAGES_PROPERTY=50
MAX_IMAGES_ITEM=10
IMAGE_QUALITY=85

# Logging
LOG_LEVEL=INFO
LOG_FILE=logs/agent.log

# Professional Features
ENABLE_ANTI_DETECTION=true
ENABLE_ERROR_RECOVERY=true
ENABLE_SPEED_MODE=false
"""
        
        try:
            with open(env_example, 'w', encoding='utf-8') as f:
                f.write(env_content)
            print_colored("✅ Created .env.example", Colors.OKGREEN)
        except Exception as e:
            print_colored(f"❌ Failed to create .env.example: {e}", Colors.FAIL)
            return False
    
    # Create logs directory
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)
    print_colored("✅ Created logs directory", Colors.OKGREEN)
    
    # Create data directory
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    print_colored("✅ Created data directory", Colors.OKGREEN)
    
    return True

def verify_installation() -> bool:
    """Verify that the installation was successful."""
    print_colored("\n🔍 Verifying installation...", Colors.OKBLUE)
    
    try:
        # Test imports
        import playwright
        import bs4
        from PIL import Image
        
        print_colored("✅ Core dependencies verified", Colors.OKGREEN)
        
        # Check if main modules exist
        main_module = Path("app/core/facebook_marketplace_agent.py")
        if main_module.exists():
            print_colored("✅ Main agent module found", Colors.OKGREEN)
        else:
            print_colored("⚠️  Main agent module not found", Colors.WARNING)
        
        return True
        
    except ImportError as e:
        print_colored(f"❌ Import error: {e}", Colors.FAIL)
        return False

def print_usage_instructions() -> None:
    """Print usage instructions."""
    print_header("INSTALLATION COMPLETE")
    
    print_colored("\n🎉 Facebook Marketplace Agent Professional Edition is ready!", Colors.OKGREEN)
    
    print_colored("\n📋 Next Steps:", Colors.OKBLUE)
    print_colored("   1. Copy .env.example to .env and configure your settings", Colors.OKCYAN)
    print_colored("   2. Run the test script: python scripts/test_professional_agent.py", Colors.OKCYAN)
    print_colored("   3. Check the documentation in README.md", Colors.OKCYAN)
    
    print_colored("\n🚀 Quick Start:", Colors.OKBLUE)
    print_colored("   python -c \"from app.core.facebook_marketplace_agent import create_property_listing; print('Ready!')\"", Colors.OKCYAN)
    
    print_colored("\n📚 Documentation:", Colors.OKBLUE)
    print_colored("   • README.md - Complete documentation", Colors.OKCYAN)
    print_colored("   • examples/ - Usage examples", Colors.OKCYAN)
    print_colored("   • docs/ - Advanced guides", Colors.OKCYAN)
    
    print_colored("\n⚠️  Important Notes:", Colors.WARNING)
    print_colored("   • Always test in non-headless mode first", Colors.WARNING)
    print_colored("   • Respect Facebook's Terms of Service", Colors.WARNING)
    print_colored("   • Keep your credentials secure", Colors.WARNING)

def main() -> None:
    """Main setup function."""
    print_header(f"FACEBOOK MARKETPLACE AGENT v{VERSION}")
    print_colored(f"Professional Edition Setup", Colors.OKBLUE)
    
    success = True
    
    # Step 1: Check Python version
    if not check_python_version():
        success = False
    
    # Step 2: Install requirements
    if success and not install_requirements():
        success = False
    
    # Step 3: Install Playwright browsers
    if success:
        install_playwright_browsers()  # Non-critical, continue even if fails
    
    # Step 4: Create configuration files
    if success and not create_config_file():
        success = False
    
    # Step 5: Verify installation
    if success and not verify_installation():
        success = False
    
    # Final results
    if success:
        print_usage_instructions()
    else:
        print_colored("\n❌ Setup failed. Please check the errors above.", Colors.FAIL)
        sys.exit(1)

if __name__ == "__main__":
    main()