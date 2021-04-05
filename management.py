import requests
import json


def get_macros():
    """
    Get macros from backend database.
    """
    return json.loads(requests.get("http://127.0.0.1:5000/macros").content)["macros"]


def new_macro(name: str, cmd: str):
    """
    Create a new macro in backend database with the given name and command.
    """
    requests.post("http://127.0.0.1:5000/macros/new", json={"name": name, "cmd": cmd})


def delete_macro(id: int):
    """
    Delete the macro with the given id in the backend database.
    """
    requests.post(f"http://127.0.0.1:5000/macros/delete/{id}")


def set_macro_attribute(id: int, attribute: str, value: str):
    """
    Find a macro in the backend database with the given id and modify
    the given attribute to have the given value.
    """
    requests.post(f"http://127.0.0.1:5000/macros/{id}",
                  json={"attribute": attribute, "value": value})


if __name__ == "__main__":
    print("Welcome to the Elenchos Management System!")
    print("""Commands:
list:\t\t\t\tprint out a list of existing macros
new,<name>,<cmd>:\t\tcreate a new macro with a given name and command
delete,<id>:\t\t\tdelete macro with given id
set,<id>,<attribute>,<value>:\tset a given attribute to a given value for a given macro
quit:\t\t\t\tExit Elenchos Management System\n""")

    cmd = ""
    while cmd != "quit":
        cmd, *args = input("> ").split(",")

        if cmd == "list":
            macros = get_macros()
            if macros:
                print("name, id, priority, selected, cmd")
                for macro in macros:
                    print(f"{macro['name']},{macro['cmd']},{macro['priority']},{macro['selected']},{macro['cmd']}")
            else:
                print("No macros currently exist in database.")
        elif cmd == "new":
            new_macro(*args)
        elif cmd == "delete":
            delete_macro(*args)
        elif cmd == "set":
            set_macro_attribute(*args)
