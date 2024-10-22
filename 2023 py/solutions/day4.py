import time

# ---------------------------------------------------
# 25174
# ---------------------------------------------------
def a():
  with open("./input/day4.txt", "r") as file:
    input = file.readlines()

  result = 0

  for line in input:
    temp = line.split(":")[1].split('|')
    winning_numbers = temp[0].strip().split()
    card_numbers = temp[1].strip().split()

    card_points = 0
    first_win = True

    for win in winning_numbers:
      for num in card_numbers:
        if num == win:
          if first_win == True:
            card_points = 1
          else:
            card_points += card_points
          first_win = False

    result += card_points

  return result

# ---------------------------------------------------
# 6420979
# ---------------------------------------------------

def b():
  with open("./input/day4.txt", "r") as file:
    input = file.readlines()

  result = 0
  extra_loop = {1: 1} # id, amount

  for line in input:
    temp = line.split(":")
    card_id = temp[0].strip().split()[1].strip()
    temp = temp[1].split('|')
    winning_numbers = temp[0].strip().split()
    card_numbers = temp[1].strip().split()

    amount_card_should_repeat = 1

    if extra_loop.get(int(card_id)) != None:
      amount_card_should_repeat = extra_loop.get(int(card_id))

    for x in range(amount_card_should_repeat):
      result += 1
      next_card_id = int(card_id)

      for win in winning_numbers:
        for num in card_numbers:
          if num == win:
            next_card_id += 1
            next_card_value = extra_loop.get(next_card_id)

            if next_card_value == None:
              extra_loop[next_card_id] = 2
            else:
              l = "k"
              extra_loop[next_card_id] = extra_loop.get(next_card_id) + 1

  return result

start_time = time.perf_counter()
a_result = a()
end_time = time.perf_counter()
print("day 4 a solution: %s in %s seconds!"%(a_result, round(end_time - start_time, 5)))
start_time = time.perf_counter()
b_result = b()
end_time = time.perf_counter()
print("day 4 b solution: %s in %s seconds!"%(b_result, round(end_time - start_time, 5)))