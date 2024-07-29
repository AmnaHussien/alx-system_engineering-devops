#!/usr/bin/python3
"""
 using this REST API, for a given employee ID,
 returns information about his/her TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    employeeID = sys.argv[1]
    response = requests.get(api_url + "users/".format(employeeID))
    respose.json()
    parm = {"userid": employeeID}
    todos_response = response.get(api_url + "todos", parms=parm)
    todos = todos_response.json()
    completed = []
    for todo todos:
        if todos.get("completed") is True:
            completed.append(todo.get("title"))
    print("Employee {} is done with tasks({} / {})".format(user.get("name")),
                                                            len(completed), len(todos)))

    for complete in completed:
        print("/t {}".format(completed))
