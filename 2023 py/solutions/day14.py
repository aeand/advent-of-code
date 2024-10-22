import time

# ---------------------------------------------------
# 106990
# ---------------------------------------------------
def a():
  input = open("./input/day14.txt").read().splitlines()
  input = list(map("".join, zip(*input)))
  weights = 0

  # rock and roll
  for line in input:
    for rocks in filter(None, line.split('#')):
      line = line.replace(rocks, "".join(sorted(rocks))[::-1], 1)

    for i, rock in enumerate(line[::-1]):
      if rock == "O":
        weights += i + 1

  return weights

def b():
  input = open("./input/day14.txt").read().splitlines()
  weights = 0

  # rock and roll
  for spin in range(4000000001):
    input = list(map("".join, zip(*input)))
    for line in input:
      for rocks in filter(None, line.split('#')):
        line = line.replace(rocks, "".join(sorted(rocks))[::-1], 1)

  input = list(map("".join, zip(*input)))
  for line in input:
    for i, rock in enumerate(line[::-1]):
      if rock == "O":
        weights += i + 1

  return weights

start_time = time.perf_counter()
a_result = a()
end_time = time.perf_counter()
print("day 11 a solution: %s in %s seconds!"%(a_result, round(end_time - start_time, 5)))
start_time = time.perf_counter()
b_result = b()
end_time = time.perf_counter()
print("day 11 a solution: %s in %s seconds!"%(b_result, round(end_time - start_time, 5)))