#!/usr/bin/env python3

import subprocess

# Define the path to the requirements file
requirements_file = 'requirements.txt'

# Install the required packages using pip
subprocess.call(['pip3', 'install', '-r', requirements_file])
