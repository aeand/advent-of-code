import os

for i in range(1, 12):
  with open("solutions/day" + str(i) + ".py") as file:
    exec(file.read())