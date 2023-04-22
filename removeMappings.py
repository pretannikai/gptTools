#!/usr/bin/env python3

import argparse
import json

# Parse the input file path from the command line
parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='path to input JSON file')
args = parser.parse_args()

# Prompt the user with a warning
if input('WARNING: This will destructively remove the "mapping" section from each prompt in the input file. Do you want to continue? (y/n) ') != 'y':
    print('Aborting...')
    exit()

# Read the JSON data from the input file
with open(args.input_file, 'r') as f:
    data = json.load(f)

# Remove the 'mapping' property from each item
for item in data:
    if 'mapping' in item:
        del item['mapping']

# Write the updated JSON data to the input file (destructive edit)
with open(args.input_file, 'w') as f:
    json.dump(data, f, indent=4)

print('Done!')
