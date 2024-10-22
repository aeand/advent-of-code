# ---------------------------------------------------
# 896125601 too high, 114197008 too low, 137516821 make sure you're using the full input data, 137516821 (from before filtering out ranges from already mapped ranges) same as before, 137516820 is right!! 1 minus what I get
# ---------------------------------------------------
def b():
  with open("./input/day5.txt", "r") as file:
    raw_input = file.readlines()

  seeds = []
  maps = [[], [], [], [], [], [], []]

  temp_seeds = list(map(int, raw_input[0].split(":")[1].strip().split()))
  for i in range(0, len(temp_seeds), 2):
    seeds.append([temp_seeds[i], temp_seeds[i + 1]])
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

  ranges1 = filter(seeds, maps[0])
  ranges2 = filter(ranges1, maps[1])
  ranges3 = filter(ranges2, maps[2])
  ranges4 = filter(ranges3, maps[3])
  ranges5 = filter(ranges4, maps[4])
  ranges6 = filter(ranges5, maps[5])
  ranges7 = filter(ranges6, maps[6])

  result = ranges7[0][0]
  for r in ranges7:
    if r[0] < result:
      result = r[0]

  return result

def filter(ranges: list, maps: list):
  new_r = []

  for m in maps:
    remove_r = []
    extra_r = []

    for r in ranges:
      if r in remove_r:
        continue

      r_start = r[0]
      r_end = r[0] + r[1] - 1
      m_start = m[1]
      m_end = m[1] + m[2] - 1
      new_m_start = m[0]
      new_m_end = m[0] + m[2] - 1

      if outside_m(r_start, r_end, m_start, m_end):
        continue
      elif inside_m(r_start, r_end, m_start, m_end):
        m_range = range(m_start, m_end + 1)
        for i in range(len(m_range)):
          if r_start == m_range[i]:
            break

        diff = r_end - r_start
        new_r.append([range(new_m_start, new_m_end + 1)[i], range(new_m_start, new_m_end + 1)[i + diff]])
        remove_r.append(r)
        continue
      elif r_covers_m(r_start, r_end, m_start, m_end):
        first_range = [r_start, m_start - 1]
        second_range = [new_m_start, new_m_end]
        third_range = [m_end + 1, r_end]

        new_r.append(second_range)
        remove_r.append(r)
        extra_r.append(first_range)
        extra_r.append(third_range)
        continue
      elif r_front_in_m(r_start, r_end, m_start, m_end):
        m_range = range(m_start, m_end + 1)
        for i in range(len(m_range)):
          if r_start == m_range[i]:
            break

        first_range = [range(new_m_start, new_m_end + 1)[i], new_m_end]
        second_range = [m_end + 1, r_end]

        new_r.append(first_range)
        remove_r.append(r)
        extra_r.append(second_range)
        continue
      elif r_back_in_m(r_start, r_end, m_start, m_end):
        m_range = range(m_start, m_end + 1)
        for i in range(len(m_range)):
          if r_end == m_range[i]:
            break

        first_range = [r_start, m_start - 1]
        second_range = [new_m_start, range(new_m_start, new_m_end + 1)[i]]

        new_r.append(second_range)
        remove_r.append(r)
        extra_r.append(first_range)
        continue

    for r in remove_r:
      ranges.remove(r)

    for r in extra_r:
      ranges.append(r)

  ranges += new_r
  return ranges

def outside_m(r_start, r_end, m_start, m_end):
  return r_end < m_start or r_start > m_end

def inside_m(r_start, r_end, m_start, m_end):
  return r_start >= m_start and r_end <= m_end

def r_covers_m(r_start, r_end, m_start, m_end):
  return r_start < m_start and r_end > m_end

def r_front_in_m(r_start, r_end, m_start, m_end):
  return r_start >= m_start and r_start <= m_end and r_end > m_end

def r_back_in_m(r_start, r_end, m_start, m_end):
  return r_start < m_start and r_end <= m_end and r_end >= m_start

""" ra = [7, 7]
ma = [4, 6]

print("outside_m", outside_m(ra[0], ra[1], ma[0], ma[1]))
print("inside_m", inside_m(ra[0], ra[1], ma[0], ma[1]))
print("r_covers_m", r_covers_m(ra[0], ra[1], ma[0], ma[1]))
print("r_front_in_m", r_front_in_m(ra[0], ra[1], ma[0], ma[1]))
print("r_back_in_m", r_back_in_m(ra[0], ra[1], ma[0], ma[1])) """