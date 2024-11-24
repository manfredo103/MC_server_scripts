#!/bin/bash

# Set the directory to navigate to
directory="/var/lib/pufferpanel/servers/2c1ff730/"

# Change to the specified directory
cd "$directory"

# Start the Python process
python3 restart.py
