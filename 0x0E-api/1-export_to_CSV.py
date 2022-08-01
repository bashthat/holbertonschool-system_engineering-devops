#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
using a REST API returning the TODO list progress
"""

import requests
from sys import argv
import csv

if __name__ == '__main__':
    if len(argv) > 1:
        uid = argv[1]
        url = 'https://jsonplaceholder.typicode.com/'
        """
        requesting the information from the API
        """
        req = requests.get('{}users/{}'.format(url, uid))
        name = req.json().get('name') # jsonify usernaame
        if name is not None: # checking the username
            """
            todos for the user
            """
            todos = requests.get('{}users/{}/todos'.format(url,
                                 uid)).json() # jsonify todos
        with open('{}.csv'.format(uid), 'w', newline='') as csvf:
            write = csv.writer(csvf, quoting=csv.QUOTE_ALL) # syscalls
            for task in todos: # writing the tasks to the csv file
                write.writerow([int(uid), name,
                                   task.get('completed'),
                                   task.get('title')]) # word
