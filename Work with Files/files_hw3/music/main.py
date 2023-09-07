import json
import os.path
from easygui import *


path = os.path.join("data_base", "test.json")

while True:
    interface = buttonbox("Choose action: ", "Action", ["ADD", "DEL", "SEARCH", "EDIT", "EXIT"])
    if interface == "EXIT":
        break
    elif interface == "ADD":
        data = multenterbox("Enter your data: ", "Group", ["Group/Band", "Album 1", "Album 2"])
        with open(path, "r") as file:
            old_data = json.load(file)
        old_data[data[0]] = {"Album 1": data[1], "Album 2": data[2]}
        with open(path, "w") as file:
            json.dump(old_data, file, indent=2)
    elif interface == "DEL":
        del_data = enterbox("Group/Band")
        with open(path, 'r') as file:
            old_data = json.load(file)
        old_data.pop(del_data)
        with open(path, "w") as file:
            json.dump(old_data, file, indent=2)
    elif interface == "SEARCH":
        with open(path, 'r') as file:
            old_data = json.load(file)
        data = enterbox("Enter Group/Band:")
        try:
            msgbox(f'Group/Band: {data}, Album 1: {old_data[data]["Album 1"]}, Album 2: {(old_data[data]["Album 2"])}')
        except KeyError:
            msgbox("Name doesn't exist in Database")
    elif interface == "EDIT":
        with open(path, 'r') as file:
            old_data = json.load(file)
        edit_name = enterbox("Enter name to edit data:")
        if edit_name in old_data:
            data = multenterbox("Edit details:", "Edit", ["Group/Band", "Album 1", "Album 2"], [f'{edit_name}', f'{old_data[edit_name]["Album 1"]}', f'{(old_data[edit_name]["Album 2"])}'])
            old_data.pop(edit_name)
            old_data[data[0]] = {"Album 1": data[1], "Album 2": data[2]}
            with open(path, "w") as file:
                json.dump(old_data, file, indent=2)
        else:
            msgbox("Name doesn't exist in Database")
    else:
        break
