import time

# ---------------------------------------------------
# 518107
# ---------------------------------------------------
def a():
  the_line = open("./input/day15.txt").read()
  result = 0
  for part in the_line.split(","):
    num = 0
    for c in part:
      num = ((num + ord(c)) * 17) % 256
    result += num
  return result
# ---------------------------------------------------
# 303404
# ---------------------------------------------------
def b():
  the_line = open("./input/day15.txt").read()
  boxes: list[list[str]] = []
  for b in range(256):
    boxes.append([])

  for part in the_line.split(","):
    if "-" in part:
      box_name = part.split("-")[0]
      box_index = hash_it(box_name)

      for b in boxes[box_index]:
        if b[0] == box_name:
          boxes[box_index].remove(b)
          break

    elif "=" in part:
      box_name = part.split("=")[0]
      box_value = part.split("=")[1]
      box_index = hash_it(box_name)

      for box in boxes[box_index]:
        if box[0] == box_name:
          box[1] = box_value
          break
      else:
        boxes[box_index].append([box_name, box_value])

###  handle 0 below

  result = 0
  for i, box in enumerate(boxes):
    for j, b in enumerate(box):
      result += (i + 1) * (j + 1) * int(b[1])

  return result

def hash_it(string: str):
  num = 0
  for c in string:
    num = ((num + ord(c)) * 17) % 256
  return num

start_time = time.perf_counter()
a_result = a()
end_time = time.perf_counter()
print("day 11 a solution: %s in %s seconds!"%(a_result, round(end_time - start_time, 5)))
start_time = time.perf_counter()
b_result = b()
end_time = time.perf_counter()
print("day 11 a solution: %s in %s seconds!"%(b_result, round(end_time - start_time, 5)))