"""Test runner for main.py"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(__file__))

# Import and run main
from main import main

if __name__ == "__main__":
    main()