#!/usr/bin/env python3

import json
import os
import sys

# Take the JSON args passed in - require that we have the 'name'
# argument
args = json.loads(sys.argv[1])

def hello(name, file_):
    print("Hello world %s" % name, file=file_)
    print("Hello job %s" % os.environ['JOB_UUID'], file=file_)
    print("Hello shell %s" % os.environ['SHELL'], file=file_)

with open('/logs/mylogfile.txt', 'w') as f:
    # Write hello
    hello(args['name'], f)

with open('/results/myresultsfile.txt', 'w') as f:
    # Write hello again
    hello(args['name'], f)
