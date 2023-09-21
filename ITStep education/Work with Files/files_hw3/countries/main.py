import json
import os.path
from easygui import *

path = os.path.join("data_base", "test.json")

while True:
    interface = buttonbox("Choose action: ", "Action", ["ADD", "DEL", "SEARCH", "EDIT", "EXIT"])
    if interface == "EXIT":
        break
    elif interface == "ADD":
        data = multenterbox("Enter your data: ", "Countries", ["Name", "Capital"])
        with open(path, "r") as file:
            old_data = json.load(file)
        old_data[data[0]] = data[1]
        with open(path, "w") as file:
            json.dump(old_data, file, indent=2)
    elif interface == "DEL":
        del_data = enterbox("Country")
        with open(path, 'r') as file:
            old_data = json.load(file)
        old_data.pop(del_data)
        with open(path, "w") as file:
            json.dump(old_data, file, indent=2)
    elif interface == "SEARCH":
        with open(path, 'r') as file:
            old_data = json.load(file)
        data = enterbox("Enter country:")
        try:
            msgbox(f'Country: {data}, Capital: {old_data[data]}')
        except KeyError:
            msgbox("Country doesn't exist in Database")
    elif interface == "EDIT":
        with open(path, 'r') as file:
            old_data = json.load(file)
        edit_name = enterbox("Enter country to edit data:")
        if edit_name in old_data:
            data = multenterbox("Edit details:", "Edit", ["Name", "Capital"], [f'{edit_name}', f'{old_data[edit_name]}'])
            old_data.pop(edit_name)
            old_data[data[0]] = data[1]
            with open(path, "w") as file:
                json.dump(old_data, file, indent=2)
        else:
            msgbox("Country doesn't exist in Database")
    else:
        break