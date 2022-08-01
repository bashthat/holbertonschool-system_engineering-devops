#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Gather data from an API
"""

import requests
from sys import argv

if __name__ == '__main__':
    if len(argv) > 1:
        userId = int(argv[1])
        url = 'https://jsonplaceholder.typicode.com/users/'
        """
        requesting the information from the API
        """
        req = requests.get('{}/{}'.format(url, userId))
        data = req.json()
        name = req.json().get('name')
        if name is not None: # checking the name
            user = requests.get('{}{}/todos'.format(url, userId))
            user = user.json()
            tasks = len(user)
            complete = []
            for task in user:
                if task.get('completed') is True:
                    complete.append(task)
            CompletedTaskNumber = len(complete)
            print ('Employee {} is done with tasks({}/{}):'.format(name, CompletedTaskNumber, tasks))
            """
            prniting the information
            """
            for task in complete: # printing the tasks
                title = task.get('title')
                print ('\t {}'.format(title))
