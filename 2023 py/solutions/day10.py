import time

# ---------------------------------------------------
# 6786
# ---------------------------------------------------
def a():
  with open("./input/day10.txt", "r") as file:
    raw_input = file.readlines()

  coordinate_table = {}
  starting_coords = []
  y = 0
  for line in raw_input:
    x = 0
    for c in line:
      if c == "S":
        starting_coords.append(x)
        starting_coords.append(y)

      if c == ".":
        x += 1
        continue

      if c == "\n":
        break

      connecting_pipes = find_connected_pipes(c, x, y)
      coordinate_table.update({"{},{}".format(x, y): connecting_pipes})

      x += 1
    y += 1

  start_adjacent = []
  x = starting_coords[0]
  y = starting_coords[1]
  start_adjacent.append([x, y - 1])
  start_adjacent.append([x + 1, y])
  start_adjacent.append([x, y + 1])
  start_adjacent.append([x - 1, y])

  start_node = "{},{}".format(starting_coords[0],starting_coords[1])
  start_nodes_actual_adjacents = []
  for i in start_adjacent:
    adjacents_adjacents = coordinate_table.get("{},{}".format(i[0],i[1]))
    if adjacents_adjacents == None:
      continue

    for j in adjacents_adjacents:
      if j == start_node:
        start_nodes_actual_adjacents.append("{},{}".format(i[0],i[1]))

  coordinate_table.update({start_node: start_nodes_actual_adjacents})

  visited_pipes = []
  visited_pipes.append(start_node)
  real_loop = []
  loop = []
  for pipe in coordinate_table.get(start_node):
    loop.append(start_node)
    loop.append(pipe)
    visited_pipes.append(pipe)
    next_pipes = []
    new_pipes = coordinate_table.get(pipe)
    if new_pipes[0] != start_node:
      next_pipes.append(new_pipes[0])
    elif new_pipes[1] != start_node:
      next_pipes.append(new_pipes[1])

    for p in next_pipes:
      new_pipes = coordinate_table.get(p)

      if new_pipes == None or len(new_pipes) < 2: # is dead end
        loop = []
        new_adjacents = coordinate_table.get(start_node)
        new_adjacents.remove(pipe)
        coordinate_table.update({start_node: new_adjacents})
      elif new_pipes[0] in visited_pipes and new_pipes[1] in visited_pipes: # found loop
        loop.append(p)
        real_loop = list(loop)
        visited_pipes.append(p)
        break
      elif new_pipes[0] in visited_pipes: # continue loop
        next_pipes.append(new_pipes[1])
        loop.append(p)
        visited_pipes.append(p)
      elif new_pipes[1] in visited_pipes: # continue loop
        next_pipes.append(new_pipes[0])
        loop.append(p)
        visited_pipes.append(p)
      else:
        print("something went wrong here")

  real_loop = list(dict.fromkeys(real_loop))

  return len(real_loop) / 2

def find_connected_pipes(char: chr, char_x_coord: int, char_y_coord: int) -> list[list[int]]:
  if char == "|":
    return ["{},{}".format(char_x_coord, char_y_coord - 1), "{},{}".format(char_x_coord, char_y_coord + 1)]
  if char == "-":
    return ["{},{}".format(char_x_coord + 1, char_y_coord), "{},{}".format(char_x_coord - 1, char_y_coord)]
  if char == "L":
    return ["{},{}".format(char_x_coord, char_y_coord - 1), "{},{}".format(char_x_coord + 1, char_y_coord)]
  if char == "J":
    return ["{},{}".format(char_x_coord, char_y_coord - 1), "{},{}".format(char_x_coord - 1, char_y_coord)]
  if char == "7":
    return ["{},{}".format(char_x_coord, char_y_coord + 1), "{},{}".format(char_x_coord - 1, char_y_coord)]
  if char == "F":
    return ["{},{}".format(char_x_coord, char_y_coord + 1), "{},{}".format(char_x_coord + 1, char_y_coord)]
  if char == ".":
    return []

# ---------------------------------------------------
# 
# ---------------------------------------------------
def b():
  with open("./input/day10.txt", "r") as file:
    raw_input = file.readlines()

  coordinate_table = {}
  character_table = {}
  starting_coords = []
  y = 0
  for line in raw_input:
    x = 0
    for c in line:
      if c == "S":
        starting_coords.append(x)
        starting_coords.append(y)

      if c == ".":
        character_table.update({"{},{}".format(x, y): c})
        x += 1
        continue

      if c == "\n":
        break

      character_table.update({"{},{}".format(x, y): c})
      connecting_pipes = find_connected_pipes_b(c, x, y)
      coordinate_table.update({"{},{}".format(x, y): connecting_pipes})

      x += 1
    y += 1

  start_adjacent = []
  x = starting_coords[0]
  y = starting_coords[1]
  start_adjacent.append([x, y - 1])
  start_adjacent.append([x + 1, y])
  start_adjacent.append([x, y + 1])
  start_adjacent.append([x - 1, y])

  start_node = "{},{}".format(starting_coords[0],starting_coords[1])
  start_nodes_actual_adjacents = []
  for i in start_adjacent:
    adjacents_adjacents = coordinate_table.get("{},{}".format(i[0],i[1]))
    if adjacents_adjacents == None:
      continue

    for j in adjacents_adjacents:
      if j == start_node:
        start_nodes_actual_adjacents.append("{},{}".format(i[0],i[1]))

  coordinate_table.update({start_node: start_nodes_actual_adjacents})

  visited_pipes = []
  visited_pipes.append(start_node)
  real_loop = []
  loop = []
  for pipe in coordinate_table.get(start_node):
    loop.append(start_node)
    loop.append(pipe)
    visited_pipes.append(pipe)
    next_pipes = []
    new_pipes = coordinate_table.get(pipe)
    if new_pipes[0] != start_node:
      next_pipes.append(new_pipes[0])
    elif new_pipes[1] != start_node:
      next_pipes.append(new_pipes[1])

    for p in next_pipes:
      new_pipes = coordinate_table.get(p)

      if new_pipes == None or len(new_pipes) < 2: # is dead end
        loop = []
        new_adjacents = coordinate_table.get(start_node)
        new_adjacents.remove(pipe)
        coordinate_table.update({start_node: new_adjacents})
      elif new_pipes[0] in visited_pipes and new_pipes[1] in visited_pipes: # found loop
        loop.append(p)
        real_loop = list(loop)
        visited_pipes.append(p)
        break
      elif new_pipes[0] in visited_pipes: # continue loop
        next_pipes.append(new_pipes[1])
        loop.append(p)
        visited_pipes.append(p)
      elif new_pipes[1] in visited_pipes: # continue loop
        next_pipes.append(new_pipes[0])
        loop.append(p)
        visited_pipes.append(p)
      else:
        print("something went wrong here")

  real_loop = list(dict.fromkeys(real_loop))

  real_loop.sort()

  high_points = []
  previous_x = ""
  for pipe in real_loop:
    x = pipe.split(',')[0]

    if x == previous_x:
      continue

    high_points.append(pipe)
    previous_x = x

  real_loop = list(reversed(real_loop))

  low_points = []
  previous_x = ""
  for pipe in real_loop:
    x = pipe.split(',')[0]

    if x == previous_x:
      continue

    low_points.append(pipe)
    previous_x = x

  low_points = list(reversed(low_points))

  # scan from high to low for character . and count amount
  # if one number reaches bottom. Remove it from high list
  # continue until high list is empty

  return 0

def find_connected_pipes_b(char: chr, char_x_coord: int, char_y_coord: int) -> list[list[int]]:
  if char == "|":
    return ["{},{}".format(char_x_coord, char_y_coord - 1), "{},{}".format(char_x_coord, char_y_coord + 1)]
  if char == "-":
    return ["{},{}".format(char_x_coord + 1, char_y_coord), "{},{}".format(char_x_coord - 1, char_y_coord)]
  if char == "L":
    return ["{},{}".format(char_x_coord, char_y_coord - 1), "{},{}".format(char_x_coord + 1, char_y_coord)]
  if char == "J":
    return ["{},{}".format(char_x_coord, char_y_coord - 1), "{},{}".format(char_x_coord - 1, char_y_coord)]
  if char == "7":
    return ["{},{}".format(char_x_coord, char_y_coord + 1), "{},{}".format(char_x_coord - 1, char_y_coord)]
  if char == "F":
    return ["{},{}".format(char_x_coord, char_y_coord + 1), "{},{}".format(char_x_coord + 1, char_y_coord)]
  if char == ".":
    return []

start_time = time.perf_counter()
a_result = a()
end_time = time.perf_counter()
print("day 10 a solution: %s in %s seconds!"%(a_result, round(end_time - start_time, 5)))
#start_time = time.perf_counter()
#b_result = b()
#end_time = time.perf_counter()
#print("day 10 b solution: %s in %s seconds!"%(b_result, round(end_time - start_time, 5)))