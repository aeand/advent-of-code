import time

# ---------------------------------------------------
# 19199
# ---------------------------------------------------
def a():
  with open("./input/day8.txt", "r") as file:
    raw_input = file.readlines()

  RL = []
  for c in list(raw_input[0].strip()):
    if c == "L":
      RL.append(0)
    else:
      RL.append(1)

  raw_input.pop(0)
  raw_input.pop(0)

  nodes = {}
  for line in raw_input:
    node = line.split(" = ")[0]
    target_nodes = line.split(" = ")[1].strip().split("(")[1].split(")")[0].split(", ")
    nodes[node] = target_nodes

  i = 0
  steps = 0
  start_node = "AAA"
  end_node = "ZZZ"
  while start_node != end_node:
    if i == len(RL):
      i = 0

    start_node = nodes.get(start_node)[RL[i]]

    steps += 1
    i += 1

  return steps

# ---------------------------------------------------
#
# ---------------------------------------------------
def b():
  with open("./input/day8.txt", "r") as file:
    raw_input = file.readlines()

  RL = []
  for c in list(raw_input[0].strip()):
    if c == "L":
      RL.append(0)
    else:
      RL.append(1)

  raw_input.pop(0)
  raw_input.pop(0)

  nodes = {}
  start_nodes = []
  end_node = []
  for line in raw_input:
    node = line.split(" = ")[0]

    if node[-1] == "A":
      start_nodes.append(node)
    elif node[-1] == "Z":
      end_node.append(node)

    target_nodes = line.split(" = ")[1].strip().split("(")[1].split(")")[0].split(", ")
    nodes[node] = target_nodes

  # need to use least common multiplier here because the numbers here get so large
  # lcm(a, b) = (a, b) / gcd(a, b)
  # modulo

  # find first occurenc of end for all start nodes
  # use math to figure out what lcm would be
  # find every starts first end. Count the steps to get there

  # in order to find a lcm I could find when the

  i = 0
  steps = 0
  end = False
  while end == False:
    if i == len(RL):
      i = 0

    j = 0
    for node in start_nodes:
      start_nodes[j] = nodes.get(node)[RL[i]]
      j += 1

    end = check_score(start_nodes)

    steps += 1
    i += 1

  return steps

def check_score(nodes):
  for node in nodes:
    if node[-1] != "Z":
      return False

  return True

start_time = time.perf_counter()
a_result = a()
end_time = time.perf_counter()
print("day 8 a solution: %s in %s seconds!"%(a_result, round(end_time - start_time, 5)))
#start_time = time.perf_counter()
#b_result = b()
#end_time = time.perf_counter()
#print("day 8 b solution: %s in %s seconds!"%(b_result, round(end_time - start_time, 5)))