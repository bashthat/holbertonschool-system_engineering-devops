#!/usr/bin/python3

"""
using a REST API returning the TODO list progress
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    R = requests.get(
        "https://jsonplaceholder.typicode.com/users/{:}".format(argv[1])
    ).json()
    R_two = requests.get(
        "https://jsonplaceholder.typicode.com/todos/?userId={:}".format
        (argv[1])).json()
    """
    adding details
    """
    userID = argv[1]
    name = R.get("username")
    """
    formatting the program
    """
    with open("{:}.csv".format(argv[1]), mode="w") as user_id_file:
        user_writer = csv.writer(user_id_file, quoting=csv.QUOTE_ALL)
        for task in R_two:  # iterate over the tasks
            user_writer.writerow(
                [userID, name, task.get("completed"), task.get("title")]
            )
