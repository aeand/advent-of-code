import time

# ---------------------------------------------------
# 389056265
# ---------------------------------------------------
def a():
  with open("./input/day5.txt", "r") as file:
    raw_input = file.readlines()

  seeds = []
  maps = [[], [], [], [], [], [], []]

  seeds = list(map(int, raw_input[0].split(":")[1].strip().split()))
  raw_input.pop(0)
  raw_input.pop(0)
  raw_input.pop(0)

  i = 0
  for line in raw_input:
    if ":" in line:
      i += 1
      continue
    if line == "\n":
      continue
    if line[-1] == "\n":
      line = line[:-1]

    maps[i].append(list(map(int, line.split())))

  results = []
  for seed in seeds:
    num1 = filter_through_map(seed, maps[0])
    num2 = filter_through_map(num1, maps[1])
    num3 = filter_through_map(num2, maps[2])
    num4 = filter_through_map(num3, maps[3])
    num5 = filter_through_map(num4, maps[4])
    num6 = filter_through_map(num5, maps[5])
    num7 = filter_through_map(num6, maps[6])
    results.append(num7)

  result = 1000000000000000
  for num in results:
    if num < result:
      result = num

  return result

def filter_through_map(num: int, maps: list):
  new_num = 0

  for map in maps:
    range_start = map[1]
    range_end = range_start + map[2]

    if num >= range_start and num <= range_end:
      new_num = map[0] + num - range_start
      break

  if new_num != 0:
    return new_num
  else:
    return num

# ---------------------------------------------------
# 896125601 too high, 114197008 too low, 137516821 make sure you're using the full input data
# ---------------------------------------------------
def b():
  with open("./input/day5.txt", "r") as file:
    raw_input = file.readlines()

  seeds = []
  seed_to_soil_map = []
  soil_to_fertilizer_map = []
  fertilizer_to_water_map = []
  water_to_light_map = []
  light_to_temperature_map = []
  temperature_to_humidity_map = []
  humidity_to_location_map = []

  temp_seeds = list(map(int, raw_input[0].split(":")[1].strip().split()))
  for i in range(0, len(temp_seeds), 2):
    seeds.append([temp_seeds[i], temp_seeds[i] + temp_seeds[i + 1] - 1])
  raw_input.pop(0)
  raw_input.pop(0)

  map_counter = 1
  for line in raw_input:
    if line == "\n":
      map_counter += 1
      continue

    if "seed-to-soil" in line or map_counter == 1:
      if line[-1] == "\n":
        line = line[:-1]

      if not line[0].isdigit():
        continue
      else:
        seed_to_soil_map.append(list(map(int, line.split())))
    elif "soil-to-fertilizer" in line or map_counter == 2:
      if line[-1] == "\n":
        line = line[:-1]

      if not line[0].isdigit():
        continue
      else:
        soil_to_fertilizer_map.append(list(map(int, line.split())))
    elif "fertilizer-to-water" in line or map_counter == 3:
      if line[-1] == "\n":
        line = line[:-1]

      if not line[0].isdigit():
        continue
      else:
        fertilizer_to_water_map.append(list(map(int, line.split())))
    elif "water-to-light" in line or map_counter == 4:
      if line[-1] == "\n":
        line = line[:-1]

      if not line[0].isdigit():
        continue
      else:
        water_to_light_map.append(list(map(int, line.split())))
    elif "light-to-temperature" in line or map_counter == 5:
      if line[-1] == "\n":
        line = line[:-1]

      if not line[0].isdigit():
        continue
      else:
        light_to_temperature_map.append(list(map(int, line.split())))
    elif "temperature-to-humidity" in line or map_counter == 6:
      if line[-1] == "\n":
        line = line[:-1]

      if not line[0].isdigit():
        continue
      else:
        temperature_to_humidity_map.append(list(map(int, line.split())))
    elif "humidity-to-location" in line or map_counter == 7:
      if line[-1] == "\n":
        line = line[:-1]

      if not line[0].isdigit():
        continue
      else:
        humidity_to_location_map.append(list(map(int, line.split())))

  ranges1 = filter_through_map_b(seeds, seed_to_soil_map)
  ranges2 = filter_through_map_b(ranges1, soil_to_fertilizer_map)
  ranges3 = filter_through_map_b(ranges2, fertilizer_to_water_map)
  ranges4 = filter_through_map_b(ranges3, water_to_light_map)
  ranges5 = filter_through_map_b(ranges4, light_to_temperature_map)
  ranges6 = filter_through_map_b(ranges5, temperature_to_humidity_map)
  ranges7 = filter_through_map_b(ranges6, humidity_to_location_map)

  result = ranges7[0][0]
  for r in ranges7:
    if r[0] < result:
      result = r[0]

  return result - 1

def filter_through_map_b(input_ranges: list[list[int]], maps: list):
  for input_range in input_ranges:
    for map in maps:
      if input_range[1] < map[1] or input_range[0] > map[1] + map[2]: # outside map
        continue
      elif input_range[0] >= map[1] and input_range[1] <= map[1] + map[2]: # inside map
        m = range(map[1], map[1] + map[2] + 1)
        for i in range(len(m)):
          if input_range[0] == m[i]:
            break

        diff_index = input_range[1] - input_range[0]
        input_range[0] = input_range[0] * 0 + range(map[0], map[0] + map[2] + 1)[i]
        input_range[1] = input_range[1] * 0 + range(map[0], map[0] + map[2] + 1)[i + diff_index]
        break
      elif input_range[0] < map[1] and input_range[1] > map[1] + map[2]: # range covers map
        first_range = [input_range[0], map[1] - 1]
        second_range = [map[0], map[0] + map[2]]
        third_range = [map[1] + map[2] + 1, input_range[1]]
        input_ranges.append(first_range)
        input_range[0] = input_range[0] * 0 + second_range[0]
        input_range[1] = input_range[1] * 0 + second_range[1]
        input_ranges.append(third_range)
        break
      elif input_range[0] >= map[1] and input_range[1] > map[1] + map[2]: # partially in range, front
        m = range(map[1], map[1] + map[2] + 1)
        for i in range(len(m)):
          if input_range[0] == m[i]:
            break

        first_range = [range(map[0], map[0] + map[2] + 1)[i], map[0] + map[2]]
        second_range = [map[1] + map[2] + 1, input_range[-1]]
        input_range[0] = input_range[0] * 0 + first_range[0]
        input_range[1] = input_range[1] * 0 + first_range[1]
        input_ranges.append(second_range)
        break
      elif input_range[0] < map[1] and input_range[1] >= map[1]: # partially in range, back
        m = range(map[1], map[1] + map[2] + 1)
        for i in reversed(range(len(m))):
          if input_range[-1] == m[i]:
            break

        first_range = [input_range[0], map[1] - 1]
        second_range = [map[0], range(map[0], map[0] + map[2] + 1)[i]] # input_range[-1]
        input_ranges.append(first_range)
        input_range[0] = input_range[0] * 0 + second_range[0]
        input_range[1] = input_range[1] * 0 + second_range[1]
        break
      else:
        continue

  # need to remove earlier since I go through input per map. Otherwise I will add the same input_range to remove twice
  return input_ranges

start_time = time.perf_counter()
a_result = a()
end_time = time.perf_counter()
print("day 5 a solution: %s in %s seconds!"%(a_result, round(end_time - start_time, 5)))
start_time = time.perf_counter()
b_result = b()
end_time = time.perf_counter()
print("day 5 b solution: %s in %s seconds!"%(b_result, round(end_time - start_time, 5)))