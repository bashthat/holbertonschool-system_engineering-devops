#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
using a REST API returning the TODO list progress
"""

from cgitb import reset
import requests
import sys
import json

if __name__ == '__main__':
        uid = sys.argv[1]  # too many comments
        url = "https://jsonplaceholder.typicode.com/"
        user = "{}users/{}".format(url, uid)
        req = requests.get(user)
        jx = req.json()
        name = jx.get('username')
        todos = "{}todos?uid={}".format(url, uid)
        req = requests.get(todos)
        jx = req.json()
        xyz = []
        for task in jx:
            rnr = [{"task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": name}]
            xyz.append(rnr)  # append the username to the task
        """
        jsonify the tasks
        """
        rnr = {}
        rnr[uid] = xyz
        
        with open("{}.json".format(uid), mode='w') as f:
            json.dump(rnr, f)
