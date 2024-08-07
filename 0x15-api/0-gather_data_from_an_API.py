#!/usr/bin/python3

"""
 using this REST API, for a given employee ID,
 returns information about his/her TODO list progress.
 First line: Employee EMPLOYEE_NAME is done with
 tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
EMPLOYEE_NAME: name of the employee
NUMBER_OF_DONE_TASKS: number of completed tasks
TOTAL_NUMBER_OF_TASKS: total number of tasks,
which is the sum of completed and non-completed tasks
Second and N next lines display the title of
completed tasks: TASK_TITLE (with 1 tabulation and 1 space
before the TASK_TITLE)
"""


import requests
import sys

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    employeeID = sys.argv[1]
    response = requests.get(api_url + "users/{}".format(employeeID))
    respose.json()
    parm = {"userId": employeeID}
    todos_response = requests.get(api_url + "todos", parms=parm)
    todos = todos_response.json()
    completed = []
    for todo in todos:
        if todos.get("completed") is True:
            completed.append(todo.get("title"))
    print("Employee {} is done with tasks({} / {})".format(user.get("name"),
                                                            len(completed), len(todos)))

    for complete in completed:
        print("/t {}".format(completed))
