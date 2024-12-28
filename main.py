from fastapi import FastAPI

from dto.advent1 import list1, list2
from models.advent1_model import advent1_part1,advent1_part2

from models.advent2_model import advent2_part1

app = FastAPI()

@app.get("/")
def read_root(): 
    return {"Hello": "World"}

@app.post("/advent1/part1")
def advent1_part1_controller(input_list1: list[int] = list1, input_list2: list[int] = list2):
    return advent1_part1(input_list1, input_list2)

@app.post("/advent1/part2")
def advent1_part2_controller(input_list1: list[int] = list1, input_list2: list[int] = list2):
    return advent1_part2(input_list1, input_list2)

@app.get("/advent2/part1")
def advent2_part1_controller():
    f = open("./dto/advent2")
    formatted_list = []
    for line in f:
        sublist = [int(str_num) for str_num in line.split()]
        formatted_list.append(sublist)
    return advent2_part1(formatted_list)