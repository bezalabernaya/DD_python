# TODO решите задачу
import json


FILENAME = "input.json"

def task() -> float:
    with open(FILENAME, "r") as f:
        data = json.load(f)
        List = [Dict.get("score")*Dict.get("weight") for Dict in data]
        return round(sum(List), 3)


print(task())
