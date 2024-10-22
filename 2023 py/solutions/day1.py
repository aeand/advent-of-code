import time

# ---------------------------------------------------
# a 54159
# ---------------------------------------------------

def a():
  with open("./input/day1.txt", "r") as file:
    input_lines = file.readlines()

  result = 0

  for line in input_lines:
    digits = [c for c in line if c.isdigit()]
    result += int(digits[0] + digits[-1])

  return result

# ---------------------------------------------------
# b 53866 twone
# ---------------------------------------------------

def b():
  with open("./input/day1.txt", "r") as file:
    input_lines = file.readlines()

  x = 0
  for line in input_lines:
    input_lines[x] = line.split("\n")[0]
    x += 1

  result = 0
  for line in input_lines:
    word = ''
    digits = []
    is_first_value = True

    if is_first_value == True:
      for c in line:
        # if digits 0 is NOT empty reverse search
        word += c
        value = list(map(word_to_number, [word]))

        if value[0] == None:
          continue
        else:
          word = ''
          digits.append(value[0])
          is_first_value = False
          break

    reverse_line = ""
    reverse_line = reverse_line.join(list(reversed(line)))

    if is_first_value == False:
      for c in reverse_line:
        word += c

        re_reversed_word = ""
        re_reversed_word = re_reversed_word.join(list(reversed(word)))

        value = list(map(word_to_number, [re_reversed_word]))

        if value[0] == None:
          continue
        else:
          word = ''
          digits.append(value[0])
          break


    result += int(digits[0] + digits[-1])

  return result

def search_forward():
  return 0

def search_backward():
  return 0

def word_to_number(word: str):
  if 'one' in word:
    return '1'
  if 'two' in word:
    return '2'
  if 'three' in word:
    return '3'
  if 'four' in word:
    return '4'
  if 'five' in word:
    return '5'
  if 'six' in word:
    return '6'
  if 'seven' in word:
    return '7'
  if 'eight' in word:
    return '8'
  if 'nine' in word:
    return '9'
  if '1' in word:
    return '1'
  if '2' in word:
    return '2'
  if '3' in word:
    return '3'
  if '4' in word:
    return '4'
  if '5' in word:
    return '5'
  if '6' in word:
    return '6'
  if '7' in word:
    return '7'
  if '8' in word:
    return '8'
  if '9' in word:
    return '9'
  else:
    return None

start_time = time.perf_counter()
a_result = a()
end_time = time.perf_counter()
print("day 1 a solution: %s in %s seconds!"%(a_result, round(end_time - start_time, 5)))
start_time = time.perf_counter()
b_result = b()
end_time = time.perf_counter()
print("day 1 b solution: %s in %s seconds!"%(b_result, round(end_time - start_time, 5)))