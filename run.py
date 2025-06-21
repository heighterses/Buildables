#!/usr/bin/env python3
"""
Buildables Website Startup Script
This script helps you start the Flask application with proper configuration.
"""

import os
import sys
from pathlib import Path

def check_environment():
    """Check if environment variables are properly configured"""
    required_vars = [
        'MAIL_USERNAME',
        'MAIL_PASSWORD',
        'ADMIN_EMAIL'
    ]
    
    missing_vars = []
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        print("❌ Missing environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        print("\n📝 Please create a .env file with the required variables.")
        print("   Use env_example.txt as a template.")
        return False
    
    return True

def main():
    """Main startup function"""
    print("🚀 Starting Buildables Website...")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not Path("app.py").exists():
        print("❌ Error: app.py not found!")
        print("   Please run this script from the project root directory.")
        sys.exit(1)
    
    # Check environment variables
    if not check_environment():
        print("\n💡 Quick Setup:")
        print("1. Copy env_example.txt to .env")
        print("2. Fill in your email credentials")
        print("3. Run this script again")
        sys.exit(1)
    
    # Check if requirements are installed
    try:
        import flask
        import flask_cors
        print("✅ Dependencies found")
    except ImportError:
        print("❌ Missing dependencies!")
        print("   Please run: pip install -r requirements.txt")
        sys.exit(1)
    
    print("✅ Environment configured")
    print("✅ Dependencies installed")
    print("\n🌐 Starting Flask server...")
    print("   Website will be available at: http://localhost:5000")
    print("   API endpoints available at: http://localhost:5000/api/")
    print("\n" + "=" * 50)
    
    # Import and run the Flask app
    try:
        from app import app
        app.run(debug=True, host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"❌ Error starting Flask app: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 