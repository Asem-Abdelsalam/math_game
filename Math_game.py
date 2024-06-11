import json
import os
import random
#for timer
import threading
import time

# player progress
#______________________________________________
player_stats = {
    "level" : 1,
    "score" : 0,
    "lives" : 3
}

# saving json data as file
def save_progress():
    with open("progress.json", "w") as f:
        json.dump(player_stats, f)


# loading the json data
def load_progress():
    if os.path.exists("progress.json"):
        with open("progress.json", "r") as f:
            return json.load(f)
    return None
#______________________________________________
def generate_problem(level):
    if level < 3:
        a = random.randint(1,10)
        b = random.randint(1,10)
        operator = random.choice(["+", "-"])
    else:
        a = random.randint(1,20)
        b = random.randint(1,20)
        operator = random.choice(["+", "-", "*", "/"])

    # eval take string expression and solves it as integer
    problem = f"{a} {operator} {b}"
    answer = eval(problem)
    return problem, answer
#______________________________________________

