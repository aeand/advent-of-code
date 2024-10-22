import time

# ---------------------------------------------------
#
# ---------------------------------------------------
def a():
  _input = open("./input/day16.txt", "r").read().splitlines()
  coordinate_map = {} # x,y: (char, lit square)
  direction = {
    "up": [0,-1],
    "right": [1,0],
    "down": [0,1],
    "left": [-1,0]
  }
  y = 0
  for line in _input:
    x = 0
    for c in line:
      coordinate_map.update({"{},{}".format(x, y): (c, False)})
      x += 1
    y += 1

  travel("0,0", "right", coordinate_map, direction, len(_input), len(_input[0]), 0)

  result = 0
  for i in coordinate_map:
    if coordinate_map.get(i)[1] == True:
      result += 1

  return result

def travel(coords: str, curr_direction: str, coord_map: dict[str, tuple], direction: dict, x_max: int, y_max: int, loop_finder: int):
  c = list(map(int, coords.split(",")))
  if c[0] < 0 or c[0] >= x_max:
    return
  if c[1] < 0 or c[1] >= y_max:
    return

  # it never gets to 2,0 since it goes down first. Missing a few spots!!     
  print(coords)

  # find loop and return from it
  if coord_map.get(coords)[1] == True:
    return
    #loop_finder += 1

  if loop_finder > 5000:
    return

  # update node
  node = coord_map.get(coords)
  coord_map.update({coords: (node[0], True)})

  # travel further
  if node[0] == "|" and (curr_direction == "right" or curr_direction == "left"):
    d = direction.get("up")
    new_coords = list(map(int, coords.split(",")))
    new_coords[0] += d[0]
    new_coords[1] += d[1]
    up_coords = ",".join(list(map(str, new_coords)))

    d = direction.get("down")
    new_coords = list(map(int, coords.split(",")))
    new_coords[0] += d[0]
    new_coords[1] += d[1]
    down_coords = ",".join(list(map(str, new_coords)))

    if coord_map.get(down_coords)[1] == False and coord_map.get(up_coords)[1] == True:
      travel(down_coords, "up", coord_map, direction, x_max, y_max, loop_finder)
    else:
      travel(up_coords, "up", coord_map, direction, x_max, y_max, loop_finder)

  elif node[0] == "-" and (curr_direction == "up" or curr_direction == "down"):
    d = direction.get("left")
    new_coords = list(map(int, coords.split(",")))
    new_coords[0] += d[0]
    new_coords[1] += d[1]
    left_coords = ",".join(list(map(str, new_coords)))

    d = direction.get("right")
    new_coords = list(map(int, coords.split(",")))
    new_coords[0] += d[0]
    new_coords[1] += d[1]
    right_coords = ",".join(list(map(str, new_coords)))

    if coord_map.get(left_coords)[1] == False and coord_map.get(right_coords)[1] == True:
      travel(new_coords, "left", coord_map, direction, x_max, y_max, loop_finder)
    else:
      travel(new_coords, "left", coord_map, direction, x_max, y_max, loop_finder)

  elif node[0] == "\\":
    di = ""
    if curr_direction == "right":
      di = "down"
    elif curr_direction == "down":
      di = "right"
    elif curr_direction == "left":
      di = "up"
    elif curr_direction == "up":
      di = "left"

    d = direction.get(di)
    new_coords = list(map(int, coords.split(",")))
    new_coords[0] += d[0]
    new_coords[1] += d[1]
    new_coords = ",".join(list(map(str, new_coords)))
    travel(new_coords, "down", coord_map, direction, x_max, y_max, loop_finder)
  elif node[0] == "/":
    di = ""
    if curr_direction == "right":
      di = "up"
    elif curr_direction == "up":
      di = "right"
    elif curr_direction == "left":
      di = "down"
    elif curr_direction == "down":
      di = "left"

    d = direction.get(di)
    new_coords = list(map(int, coords.split(",")))
    new_coords[0] += d[0]
    new_coords[1] += d[1]
    new_coords = ",".join(list(map(str, new_coords)))
    travel(new_coords, di, coord_map, direction, x_max, y_max, loop_finder)
  else:
    d = direction.get(curr_direction)
    new_coords = list(map(int, coords.split(",")))
    new_coords[0] += d[0]
    new_coords[1] += d[1]
    new_coords = ",".join(list(map(str, new_coords)))
    travel(new_coords, curr_direction, coord_map, direction, x_max, y_max, loop_finder)

start_time = time.perf_counter()
a_result = a()
end_time = time.perf_counter()
print("day 11 a solution: %s in %s seconds!"%(a_result, round(end_time - start_time, 5)))