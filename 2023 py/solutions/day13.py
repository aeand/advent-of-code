import time

# ---------------------------------------------------
#
# ---------------------------------------------------

def a():
  with open("./input/day13.txt") as file:
    raw_input = file.readlines()

  maps = []
  tmp = []
  for line in raw_input:
    if line == "\n":
      maps.append(tmp)
      tmp = []
      continue

    tmp.append(line[0:len(line)-1])

  maps.append(tmp)
  tmp = []

  result = 0
  for m in maps:
    done = False
    for i in range(len(m)):
      if i + 1 < len(m) and m[i] == m[i+1] and is_row_mirror(m, i) == True:
        result += (i + 1) * 100
        done = True

    if done == False:
      m_flip = flip_m(m)
      for i in range(len(m_flip)):
        if i + 1 < len(m_flip) and m_flip[i] == m_flip[i+1] and is_row_mirror(m_flip, i) == True:
          result += i+1

  return result

def is_row_mirror(m: list[list[str]], index: int) -> bool:
  index += 1
  j = index
  for i in reversed(range(index)):
    if i < 0 or j >= len(m):
      break

    if m[i] != m[j]:
      return False
    j += 1

  return True

def flip_m(m: list[list[str]]):
  return list(reversed(list(map(list, zip(*m)))[::-1]))

start_time = time.perf_counter()
a_result = a()
end_time = time.perf_counter()
print("day 11 a solution: %s in %s seconds!"%(a_result, round(end_time - start_time, 5)))