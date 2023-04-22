# GPTTools
A set of tools that does cool stuff with ChatGPT

## Requirements
- Python 3 or later

## Setup
- Run `./setup.py` to install requirements

## ChatGPT export conversations.json Usage
- Run `./gptDater.py input_filename` to add a "create_localtime" attribute to each prompt entry in the input file with a converted local time from the original create time
- Run `./removeMappings.py input_filename` to destructively remove the 'mapping' attribute from each prompt entry in the input file
- Run `./sorter.py input_filename` to destructively sort the input file by create_localtime, descending by default. Use option -a to sort in ascending order.