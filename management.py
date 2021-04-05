import requests
import json


def get_macros():
    """
    Get macros from backend database.
    """
    return json.loads(requests.get("http://127.0.0.1:5000/macros"))


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

