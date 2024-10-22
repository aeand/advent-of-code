import time
from operator import itemgetter

# ---------------------------------------------------
# 28801 too low, 85052 too high, 62848 use all data, 62323 not correct
# ---------------------------------------------------
def a():
  _input = open("./input/day18.txt", "r").read().splitlines()
  coords = (0,0)
  li = []
  for line in _input:
    d = line.split()[0]
    l = line.split()[1]

    if d == "U":
      for i in range(int(l)):
        coords = (coords[0], coords[1] - 1)
        li.append(coords)
    if d == "R":
      for i in range(int(l)):
        coords = (coords[0] + 1, coords[1])
        li.append(coords)
    if d == "D":
      for i in range(int(l)):
        coords = (coords[0], coords[1] + 1)
        li.append(coords)
    if d == "L":
      for i in range(int(l)):
        coords = (coords[0] - 1, coords[1])
        li.append(coords)

  x_min = min(li, key = itemgetter(0))[0]
  x_max = max(li, key = itemgetter(0))[0]
  y_min = min(li, key = itemgetter(1))[1]
  y_max = max(li, key = itemgetter(1))[1]

  s = ""
  for j in range(y_min, y_max+1):
    is_in = False
    pre = ""
    for i in range(x_min, x_max+1):
      temp = "."
      if (i, j) in li:
        if pre != "#":
          is_in = not is_in
        temp = "#"
      elif is_in:
        temp = "!"

      pre = temp
      s += temp
      if i == x_max:
        s += "\n"

  new_input = list(filter(None, s.split("\n")))
  result = 0
  for line in new_input:
    if line.find("#!") == -1 or line.find("!#") == -1:
      line = line.replace("!", ".")
    result += line.count("#") + line.count("!")

  return result

start_time = time.perf_counter()
a_result = a()
end_time = time.perf_counter()
print("day 11 a solution: %s in %s seconds!"%(a_result, round(end_time - start_time, 5)))