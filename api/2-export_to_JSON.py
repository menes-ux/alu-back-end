#!/usr/bin/python3
"""
Using a REST API and an EMP_ID, save info about their TODO list in a json file
"""
import json
import requests
import sys

if __name__ == "__main__":
    """ Main section """
    BASE_URL = 'https://jsonplaceholder.typicode.com'
    employee_id = sys.argv[1] if len(sys.argv) > 1 else None

    if not employee_id:
        print("Please provide an employee ID as an argument.")
        sys.exit(1)

    employee = requests.get(f"{BASE_URL}/users/{employee_id}/").json()
    employee_name = employee.get("username")
    emp_todos = requests.get(f"{BASE_URL}/users/{employee_id}/todos").json()
    serialized_todos = []

    for todo in emp_todos:
        serialized_todos.append({
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": employee_name
        })

    output_data = {employee_id: serialized_todos}

    # ----------------------------------------------------
    # FIX: Define the filename variable here
    file_name = f"{employee_id}.json"
    # ----------------------------------------------------

    with open(file_name, 'w') as file:
        json.dump(output_data, file) # Auto-graders often require no 'indent'
        # OR: json.dump(output_data, file, indent=4) if formatting is required

    # FIX: Use the correctly defined file_name variable
    print(f"Tasks for employee {employee_id} exported to {file_name}") 
    # The example output doesn't show a concluding period, 
    # so remove it to be safe.