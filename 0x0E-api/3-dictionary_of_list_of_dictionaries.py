#!/usr/bin/python3
"""
extend your Python script to export data in the JSON format.
"""

import requests
import json
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    req = requests.get('{}users'.format(url)).json()
    xyz = {}
    for user in req:
        Id = user.get('id')  # request id
        username = user.get('username')  # username
        todos = requests.get('{}users/{}/todos'.format(url,
                             Id)).json()  # jsonify todos
        tsk = [{'username': username, 'task': tsk.get('title'),
                'completed': tsk.get('completed')} for tsk in todos]
        xyz[Id] = tsk  # the tasks given the format to the problem
    with open('todo_all_employees.json', 'w') as jsn:
        json.dump(xyz, jsn)  # word
