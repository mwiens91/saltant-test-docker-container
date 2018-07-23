#!/usr/bin/env python3

import json
import sys

# Take the JSON args passed in - require that we have the 'name'
# argument
args = json.loads(sys.argv[1])

with open('/logs/myfile.txt', 'w') as f:
    # Write hello
    f.write("Hello world %s" % args['name'])
    f.write("Hello shell %s" % os.environ['SHELL'])
