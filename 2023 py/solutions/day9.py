import time

# ---------------------------------------------------
# 1684566095
# ---------------------------------------------------
def a():
  with open("./input/day9.txt", "r") as file:
    raw_input = file.readlines()

  result = 0
  for line in raw_input:
    input = []
    input.append(list(map(int, line.strip().split())))
    diff = [1]

    i = 0
    while is_all_zero(diff) == False:
      diff = create_diff_list(input, i)
      input.append(diff)
      i += 1

    new_value = 0
    new_values = [0]
    k = 0
    for index in reversed(range(i + 1)):
      if index == 0:
        break
      last_value = input[index - 1][-1]
      new_value = last_value + new_values[k]
      new_values.append(new_value)
      k += 1

    result += new_values[-1]

  return result

def is_all_zero(list: list[int]):
  for item in list:
    if item != 0:
      return False

  return True

def create_diff_list(input: list[list[int]], index: int):
  diff = []
  i = 0
  for value in range(len(input[index]) - 1):
    if i == len(input[index]):
      break

    if input[index][i] == 0:
      diff.append(input[index][i + 1])
    else:
      diff.append(input[index][i + 1] - input[index][i])
    i += 1

  return diff

# ---------------------------------------------------
# 1684566095
# ---------------------------------------------------
def b():
  with open("./input/day9.txt", "r") as file:
    raw_input = file.readlines()

  result = 0
  for line in raw_input:
    input = []
    input.append(list(map(int, line.strip().split())))
    diff = [1]

    i = 0
    while is_all_zero(diff) == False:
      diff = create_diff_list(input, i)
      input.append(diff)
      i += 1

    new_value = 0
    new_values = [0]
    k = 0
    for index in reversed(range(i + 1)):
      if index == 0:
        break
      first_value = input[index - 1][0]
      new_value = first_value - new_values[k]
      new_values.append(new_value)
      k += 1

    result += new_values[-1]

  return result

def is_all_zero(list: list[int]):
  for item in list:
    if item != 0:
      return False

  return True

start_time = time.perf_counter()
a_result = a()
end_time = time.perf_counter()
print("day 9 a solution: %s in %s seconds!"%(a_result, round(end_time - start_time, 5)))
start_time = time.perf_counter()
b_result = b()
end_time = time.perf_counter()
print("day 9 b solution: %s in %s seconds!"%(b_result, round(end_time - start_time, 5)))