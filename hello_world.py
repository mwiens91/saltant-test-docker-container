#!/usr/bin/env python3

import json
import os
import sys

# Take the JSON args passed in - require that we have the 'name'
# argument
args = json.loads(sys.argv[1])

worker_logs_path = os.path.join(
    os.environ['WORKER_LOGS_DIRECTORY'],
    os.environ['JOB_UUID'],)
worker_results_path = os.path.join(
    os.environ['WORKER_RESULTS_DIRECTORY'],
    os.environ['JOB_UUID'],)

os.makedirs(worker_logs_path, exist_ok=True)
os.makedirs(worker_results_path, exist_ok=True)

logfilepath = os.path.join(worker_logs_path, 'mylogfile.txt')
resultsfilepath = os.path.join(worker_results_path, 'myresultsfile.txt')

def hello(name, file_):
    print("Hello world %s" % name, file=file_)
    print("Hello job %s" % os.environ['JOB_UUID'], file=file_)
    print("Hello shell %s" % os.environ['SHELL'], file=file_)

with open(logfilepath, 'w') as f:
    # Write hello
    hello(args['name'], f)

with open(resultsfilepath, 'w') as f:
    # Write hello again
    hello(args['name'], f)
