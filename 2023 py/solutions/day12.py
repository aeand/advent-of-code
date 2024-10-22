import time

# ---------------------------------------------------
#
# ---------------------------------------------------
def a():
  with open('./input/day12.txt') as file:
    input = file.readlines()

  for line in input:
    #springs = list(filter(None, line.split()[0].split('.')))
    springs = line.split()[0]
    amount = list(map(int, line.split()[1].split(',')))

    converted_springs = ''

    index = 0
    j = 0
    for num in amount:
      # find first #
      for o in range(index + j, len(springs)):
        if springs[o] == '.':
          converted_springs += '.'
          index += 1
          continue
        else:
          break

      # get accurate substring
      i = 0
      s = springs[index:num + index]
      while '.' in s:
        i += 1
        if s[0] == '?':
          converted_springs += '.'
        else:
          converted_springs += s[0]
        s = springs[index + i:num + index + i]

      next_index = index+i+num
      # check if next is #
      j = 0
      while springs[next_index + j] == '#':
        j += 1
        converted_springs += '.'
        s = springs[index + j:num + index + j]

      next_index += j
      # check n' set next value
      if springs[next_index] == '?':
        springs = springs[:next_index] + '.' + springs[next_index + 1:]

      if '?' in s:
        s = s.replace('?', '#')

      # add s to a new string
      converted_springs += s
      index += i + num

    # add last characters
    converted_springs += springs[index:]

    # might be able to do this after I replace ? with # or .
    # for those that have on option
    q = len(amount) - line.split()[0].count('?')
    q *= 2 * q
    print(converted_springs)

  return q

start_time = time.perf_counter()
a_result = a()
end_time = time.perf_counter()
print("day 5 a solution: %s in %s seconds!"%(a_result, round(end_time - start_time, 5)))


# might be able to create a list of ['###', '##', '#'] from 3,2,1
# then map those elements to the line
# find possible new lines through that