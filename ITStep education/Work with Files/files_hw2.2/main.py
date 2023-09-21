import json
import os.path
from easygui import *


path = os.path.join("data_base", "test1.json")

while True:
    interface = buttonbox("Choose action: ", "Action", ["ADD", "DEL", "SEARCH", "EDIT", "EXIT"])
    if interface == "EXIT":
        break
    elif interface == "ADD":
        data = multenterbox("Enter your data: ", "Employees", ["Name", "Age", "Work"])
        with open(path, "r") as file:
            old_data = json.load(file)
        old_data[data[0]] = {"Age": data[1], "Work":data[2]}
        with open(path, "w") as file:
            json.dump(old_data, file, indent=2)
    elif interface == "DEL":
        del_data = enterbox("Name")
        with open(path, 'r') as file:
            old_data = json.load(file)
        old_data.pop(del_data)
        with open(path, "w") as file:
            json.dump(old_data, file, indent=2)
    elif interface == "SEARCH":
        with open(path, 'r') as file:
            old_data = json.load(file)
        data = enterbox("Enter full name:")
        try:
            msgbox(f'Name: {data}, Age: {old_data[data]["Age"]}, Work: {(old_data[data]["Work"])}')
        except KeyError:
            msgbox("Name doesn't exist in Database")
    elif interface == "EDIT":
        with open(path, 'r') as file:
            old_data = json.load(file)
        edit_name = enterbox("Enter name to edit data:")
        if edit_name in old_data:
            data = multenterbox("Edit details:", "Edit", ["Name", "Age", "Work"], [f'{edit_name}', f'{old_data[edit_name]["Age"]}', f'{(old_data[edit_name]["Work"])}'])
            old_data.pop(edit_name)
            old_data[data[0]] = {"Age": data[1], "Work": data[2]}
            with open(path, "w") as file:
                json.dump(old_data, file, indent=2)
        else:
            msgbox("Name doesn't exist in Database")
    else:
        break
