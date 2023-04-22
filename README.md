# GPTTools
A set of tools that do cool stuff with ChatGPT

## Requirements
- Python 3 or later

## Setup
- Run `./setup.py` to install requirements

## ChatGPT export conversations.json Usage
- Run `./gptDater.py input_filename` to add a "create_localtime" attribute to each prompt entry in the input file with a converted local time from the original create time
- Run `./removeMappings.py input_filename` to destructively remove the 'mapping' attribute from each prompt entry in the input file