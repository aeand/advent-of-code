import time

# ---------------------------------------------------
# a 2265
# ---------------------------------------------------

def a():
  with open("./input/day2.txt", "r") as file:
    input = file.readlines()

  games = []

  index = 0
  for line in input:
    input[index] = line.split("\n")[0]
    input[index] = input[index].split("Game")[1]

    # format by id and draws
    temp = input[index].split(": ")
    id = int(temp[0].strip())
    draw = temp[1]
    games.append([id, draw])
    index += 1

  valid_games = []

  index = 0
  for game in games:
    id = game[0]
    draws = game[1].split("; ")

    for draw in draws:
      dice = draw.split(", ")
      is_draw_valid = True

      for die in dice:
        is_draw_valid = is_dice_valid(die)
        if is_draw_valid == False:
          break

      if is_draw_valid == False:
        break

    if is_draw_valid == True:
      valid_games.append(id)

    index += 1

  result = 0
  for id in valid_games:
    result += int(id)

  return result

def is_dice_valid(input: str):
  result = input.split(" ")

  if result[1] == "red":
    if int(result[0]) > 12:
      return False

  if result[1] == "green":
    if int(result[0]) > 13:
      return False

  if result[1] == "blue":
    if int(result[0]) > 14:
      return False

  return True

# ---------------------------------------------------
# b 64097
# ---------------------------------------------------

def b():
  with open("./input/day2.txt", "r") as file:
    input = file.readlines()

  games = []

  index = 0
  for line in input:
    input[index] = line.split("\n")[0]
    input[index] = input[index].split("Game")[1]

    # format by id and draws
    temp = input[index].split(": ")
    id = int(temp[0].strip())
    draw = temp[1]
    games.append([id, draw])
    index += 1

  result = 0

  index = 0
  for game in games:
    id = game[0]
    draws = game[1].split("; ")

    colors = {
      "red": 0,
      "green": 0,
      "blue": 0
    }

    for draw in draws:
      dice = draw.split(", ")

      for die in dice:
        # add bigger numbers to color
        temp = die.split()
        number = temp[0]
        color = temp[1]

        if int(number) > int(colors.get(color)):
          colors.update({color: number})

    result += int(colors.get("red")) * int(colors.get("green")) * int(colors.get("blue"))
    index += 1

  return result

start_time = time.perf_counter()
a_result = a()
end_time = time.perf_counter()
print("day 2 a solution: %s in %s seconds!"%(a_result, round(end_time - start_time, 5)))
start_time = time.perf_counter()
b_result = b()
end_time = time.perf_counter()
print("day 2 b solution: %s in %s seconds!"%(b_result, round(end_time - start_time, 5)))