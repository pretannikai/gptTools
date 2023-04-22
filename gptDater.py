#!/usr/bin/env python3

import argparse
import json
import datetime
import pytz

# Define the local timezone (replace with your own timezone)
local_tz = pytz.timezone('America/New_York')

# Parse the input file path from the command line
parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='path to input JSON file')
args = parser.parse_args()

# Read the JSON data from the input file
with open(args.input_file, 'r') as f:
    data = json.load(f)

# Loop over each item and add the new field
for item in data:
    create_time = item['create_time']
    create_localtime = datetime.datetime.fromtimestamp(create_time, tz=pytz.utc).astimezone(local_tz)
    item['create_localtime'] = create_localtime.isoformat()

# Write the updated JSON data to an output file
with open('output.json', 'w') as f:
    json.dump(data, f, indent=4)
