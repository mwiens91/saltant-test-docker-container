#!/usr/bin/env python3

import json
import os
import sys

# Take the JSON args passed in - require that we have the 'name'
# argument
args = json.loads(sys.argv[1])

with open('/logs/mylogfile.txt', 'w') as f:
    # Write hello
    f.write("Hello world %s\n" % args['name'])
    f.write("Hello shell %s" % os.environ['SHELL'])

with open('/results/myresultsfile.txt', 'w') as f:
    # Write hello again
    f.write("Hello world %s\n" % args['name'])
    f.write("Hello shell %s" % os.environ['SHELL'])
