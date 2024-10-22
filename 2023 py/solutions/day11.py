import time

# ---------------------------------------------------
# 9418609
# ---------------------------------------------------
def a():
  with open("./input/day11.txt", "r") as file:
    raw_input = file.readlines()

  xpand = []
  index = 0
  for line in raw_input:
    if "#" not in line:
      xpand.append(index)
    index += 1

  raw_input_y = []
  for i in range(len(raw_input[0]) - 1):
    raw_input_y.append("")

  for line in raw_input:
    index = 0
    for c in line:
      if c != "\n":
        raw_input_y[index] += c
      index += 1

  y_empty_line = ""
  ypand = []
  index = 0
  for line in raw_input_y:
    if "#" not in line:
      ypand.append(index)
      y_empty_line = line
    index += 1

  new_raw_input_y = list(raw_input_y)

  index = 0
  list_updated = 0
  for line in raw_input_y:
    if index in ypand:
      new_raw_input_y.insert(index + list_updated, y_empty_line)
      ypand.pop(0)
      list_updated += 1

    index += 1

  raw_input_x = []
  for i in range(len(new_raw_input_y[0])):
    raw_input_x.append("")

  for line in new_raw_input_y:
    index = 0
    for c in line:
      if c != "\n":
        raw_input_x[index] += c
      index += 1

  input = list(raw_input_x)
  x_empty_line = ""
  for i in range(len(input[9])):
    x_empty_line += "."

  index = 0
  list_updated = 0
  for line in raw_input_x:
    if index in xpand:
      input.insert(index + list_updated, x_empty_line)
      xpand.pop(0)
      list_updated += 1

    index += 1

  galaxies_table = {}

  y = 0
  id = 1
  for line in input:
    x = 0
    for c in line:
      if c == "\n":
        break
      if c == "#":
        galaxies_table.update({id: [x, y]})
        id += 1
      x += 1
    y += 1

  result = 0
  for id in range(1, len(galaxies_table) + 1):
    for other_id in range(id, len(galaxies_table) + 1):
      if id == other_id:
        continue

      path = [galaxies_table.get(other_id)[0] - galaxies_table.get(id)[0], galaxies_table.get(other_id)[1] - galaxies_table.get(id)[1]]
      result += abs(path[0]) + abs(path[1])

  return result

# ---------------------------------------------------
# 593821230983
# ---------------------------------------------------

def b():
  with open("./input/day11.txt", "r") as file:
    raw_input = file.readlines()

  xpand = []
  index = 0
  for line in raw_input:
    if "#" not in line:
      xpand.append(index)
    index += 1

  raw_input_y = []
  for i in range(len(raw_input[0]) - 1):
    raw_input_y.append("")

  for line in raw_input:
    index = 0
    for c in line:
      if c != "\n":
        raw_input_y[index] += c
      index += 1

  ypand = []
  index = 0
  for line in raw_input_y:
    if "#" not in line:
      ypand.append(index)
    index += 1

  galaxies_table = {}

  y = 0
  id = 1
  for line in raw_input:
    x = 0
    for c in line:
      if c == "\n":
        break
      if c == "#":
        galaxies_table.update({id: [x, y]})
        id += 1
      x += 1
    y += 1

  result = 0
  for id in range(1, len(galaxies_table) + 1):
    for other_id in range(id, len(galaxies_table) + 1):
      if id == other_id:
        continue

      galaxy = galaxies_table.get(id)
      other_galaxy = galaxies_table.get(other_id)

      path = [other_galaxy[0] - galaxy[0], other_galaxy[1] - galaxy[1]]
      extra_space = 0
      for x in xpand:
        if galaxy[1] < x < other_galaxy[1] or galaxy[1] > x > other_galaxy[1]:
          extra_space += 1
      for y in ypand:
        if galaxy[0] < y < other_galaxy[0] or galaxy[0] > y > other_galaxy[0]:
          extra_space += 1

      result += abs(path[0]) + abs(path[1]) + extra_space * 999999

  return result

start_time = time.perf_counter()
a_result = a()
end_time = time.perf_counter()
print("day 11 a solution: %s in %s seconds!"%(a_result, round(end_time - start_time, 5)))
start_time = time.perf_counter()
b_result = b()
end_time = time.perf_counter()
print("day 11 b solution: %s in %s seconds!"%(b_result, round(end_time - start_time, 5)))