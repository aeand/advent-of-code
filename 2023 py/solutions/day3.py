import time

# ---------------------------------------------------
# 550064
# ---------------------------------------------------

def a():
  with open("./input/day3.txt", "r") as file:
    input = file.readlines()

  lookup_table: dict = {}

  y = 0
  for line in input:
    x = 0
    for c in line:
      if c == "\n":
        break
      lookup_table.update({"{},{}".format(x, y): c})
      x += 1
    y += 1

  # might need to update this with the input
  valid_symbols = {
    '$': True,
    '*': True,
    '#': True,
    '+': True,
    '@': True,
    '/': True,
    '-': True,
    '%': True,
    '&': True,
    '=': True,
  }

  result = 0
  skip_coordinates = ['0,0']
  skip_it = False

  y = 0
  for i in range(len(input)):
    x = 0
    for j in range(len(input[0]) - 1): # skip new line
      coordinates = "{},{}".format(x,y)
      skip_it = False

      for skip in skip_coordinates:
        if skip == coordinates:
          skip_it = True
          break

      if skip_it == True:
        x += 1
        continue

      value = lookup_table.get(coordinates)

      if value.isdigit():
        adjacents = []

        for a in range(-1, 2, 1):
          for b in range(-1, 2, 1):
            if x + a != x or y + b != y:
              adjacents.append("{},{}".format(x + a,y + b))

        for coord in adjacents:
          if valid_symbols.get(lookup_table.get(coord)) == True:

            total_number = []

            left = -1
            while left < 1:
              num_coords = "{},{}".format(x + left,y)
              neighbour_value = lookup_table.get(num_coords)
              if neighbour_value != None and neighbour_value.isdigit():
                total_number.insert(0, neighbour_value)
                left -= 1
              else:
                left = 2

            total_number.append(value)

            right = 1
            while right > -1:
              num_coords = "{},{}".format(x + right,y)
              neighbour_value = lookup_table.get(num_coords)
              if neighbour_value != None and neighbour_value.isdigit():
                total_number.append(neighbour_value)
                skip_coordinates.append(num_coords)
                right += 1
              else:
                right = -2

            ok_num = ''
            for num in total_number:
              ok_num += num

            result += int(ok_num)

      x += 1
    y += 1

  return result

# ---------------------------------------------------
# b 85010461
# ---------------------------------------------------

def b():
  with open("./input/day3.txt", "r") as file:
    input = file.readlines()

  lookup_table: dict = {}

  y = 0
  for line in input:
    x = 0
    for c in line:
      if c == "\n":
        break
      lookup_table.update({"{},{}".format(x, y): c})
      x += 1
    y += 1

  # might need to update this with the input
  valid_symbols = {
    '$': True,
    '*': True,
    '#': True,
    '+': True,
    '@': True,
    '/': True,
    '-': True,
    '%': True,
    '&': True,
    '=': True,
  }

  result = 0
  skip_coordinates = ['0,0']

  y = 0
  for i in range(len(input)):
    x = 0
    for j in range(len(input[0]) - 1): # skip new line
      coordinates = "{},{}".format(x,y)
      value = lookup_table.get(coordinates)

      if value == '*':
        adjacents = []

        for a in range(-1, 2, 1):
          for b in range(-1, 2, 1):
            if x + a != x or y + b != y:
              adjacents.append("{},{}".format(x + a,y + b))

        adjacent_numbers = []
        adjacent_coords_to_skip = []
        skip_adjacent_coord = False

        for coord in adjacents:
          skip_adjacent_coord = False

          for cor in adjacent_coords_to_skip:
            if coord == cor:
              skip_adjacent_coord = True
              break

          if skip_adjacent_coord == True:
            continue

          if lookup_table.get(coord).isdigit():
            adjacent_coord = coord.split(",")
            total_number = []

            left = -1
            while left < 1:
              num_coords = "{},{}".format(int(adjacent_coord[0]) + left,int(adjacent_coord[1]))
              neighbour_value = lookup_table.get(num_coords)
              if neighbour_value != None and neighbour_value.isdigit():
                total_number.insert(0, neighbour_value)
                adjacent_coords_to_skip.append(num_coords)
                left -= 1
              else:
                left = 2

            total_number.append(lookup_table.get(coord))

            right = 1
            while right > -1:
              num_coords = "{},{}".format(int(adjacent_coord[0]) + right,int(adjacent_coord[1]))
              neighbour_value = lookup_table.get(num_coords)
              if neighbour_value != None and neighbour_value.isdigit():
                total_number.append(neighbour_value)
                adjacent_coords_to_skip.append(num_coords)
                right += 1
              else:
                right = -2

            ok_num = ''
            for num in total_number:
              ok_num += num

            adjacent_numbers.append(ok_num)

        if len(adjacent_numbers) == 2:
            result += int(adjacent_numbers[0]) * int(adjacent_numbers[1])

      x += 1
    y += 1

  return result

start_time = time.perf_counter()
a_result = a()
end_time = time.perf_counter()
print("day 3 a solution: %s in %s seconds!"%(a_result, round(end_time - start_time, 5)))
start_time = time.perf_counter()
b_result = b()
end_time = time.perf_counter()
print("day 3 b solution: %s in %s seconds!"%(b_result, round(end_time - start_time, 5)))