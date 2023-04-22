#!/usr/bin/env python3

import argparse
import json

# Parse the input file path and sorting order from the command line
parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='path to input JSON file')
parser.add_argument('-a', '--ascending', action='store_true', help='sort by create_localtime in ascending order')
args = parser.parse_args()

if args.ascending:
    reverse_order = False
else:
    reverse_order = True

# Prompt the user with a warning
if input('WARNING: This will destructively edit the input file by sorting the entries. Do you want to continue? (y/n) ') != 'y':
    print('Aborting...')
    exit()

# Read the JSON data from the input file
with open(args.input_file, 'r') as f:
    data = json.load(f)

# Sort the data by create_localtime
data.sort(key=lambda item: item['create_localtime'], reverse=reverse_order)

# Write the sorted JSON data to the input file (destructive edit)
with open(args.input_file, 'w') as f:
    json.dump(data, f, indent=4)

print('Done!')