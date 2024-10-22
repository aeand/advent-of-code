import time

# ---------------------------------------------------
# 449550
# ---------------------------------------------------
def a():
  with open("./input/day6.txt", "r") as file:
    raw_input = file.readlines()

  input = []
  for line in raw_input:
    input.append(line.split("\n")[0].split(":")[1].strip())

  time = []
  for x in input[0].split(" "):
    if x != "":
      time.append(int(x.strip()))

  distance = []
  for x in input[1].split(" "):
    if x != "":
      distance.append(int(x.strip()))

  result = 1
  index = 0
  for t in time:
    possible_wins = 0
    for i in range(t):
      if i * (t - i) > distance[index]:
        possible_wins += 1

    result *= possible_wins
    index += 1

  return result

# ---------------------------------------------------
# 28360140
# ---------------------------------------------------
def b():
  with open("./input/day6.txt", "r") as file:
    raw_input = file.readlines()

  input = []
  for line in raw_input:
    input.append(line.split("\n")[0].split(":")[1].strip())

  time = ""
  for x in input[0].split(" "):
    if x != "":
      time += x.strip()

  distance = ""
  for x in input[1].split(" "):
    if x != "":
      distance += x.strip()

  result = 0
  for i in range(int(time)):
    if i * (int(time) - i) > int(distance):
      result += 1

  return result

start_time = time.perf_counter()
a_result = a()
end_time = time.perf_counter()
print("day 6 a solution: %s in %s seconds!"%(a_result, round(end_time - start_time, 5)))
start_time = time.perf_counter()
b_result = b()
end_time = time.perf_counter()
print("day 6 b solution: %s in %s seconds!"%(b_result, round(end_time - start_time, 5)))