#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
using a REST API returning the TODO list progress
"""

import requests
from sys import argv
import csv
import json

if __name__ == '__main__':
    if len(argv) > 1:
        """handling the arguments"""
        uid = argv[1]
        url = "https://jsonplaceholder.typicode.com/"
        req = requests.get("{}users/{}".format(url, uid)).json()
        user = req.get('username')
        todos = requests.get("{}users/{}/todos".format(url, uid)).json()
        task = [{"task": t.get("title"),
                 "completed": t.get("completed"),
                 "username": user} for t in todos]
        """
        jsonify the tasks
        """
        jd = {}
        jd[uid] = task
        with open('{}.json'.format(uid), 'w') as jsonf:
            json.dump(task, jsonf)
    else:
        print('usage: {} <user_id>'.format(argv[0]))
        exit(1)  # word
