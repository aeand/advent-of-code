import time

# ---------------------------------------------------
# 249483956
# ---------------------------------------------------
def checkFiveOfAKind(cards: str):
  matches = getCardAmounts(cards)
  has_matches = False

  for key in matches:
    if matches[key] == 5:
      has_matches = True

  return has_matches

def checkFourOfAKind(cards: str):
  matches = getCardAmounts(cards)
  has_matches = False

  for key in matches:
    if matches[key] == 4:
      has_matches = True

  return has_matches

def checkThreeOfAKind(cards: str):
  matches = getCardAmounts(cards)
  has_three_matches = False
  has_two_matches = False

  for key in matches:
    if matches[key] == 3:
      has_three_matches = True

  for key in matches:
    if matches[key] == 2:
      has_two_matches = True

  return has_three_matches and not has_two_matches

def checkFullHouse(cards: str):
  matches = getCardAmounts(cards)
  has_three_matches = False
  has_two_matches = False

  for key in matches:
    if matches[key] == 3:
      has_three_matches = True

  for key in matches:
    if matches[key] == 2:
      has_two_matches = True

  return has_three_matches and has_two_matches

def checkTwoPair(cards: str):
  matches = getCardAmounts(cards)
  has_matches = []

  for key in matches:
    if matches[key] == 2:
      has_matches.append(1)

  return len(has_matches) == 2

def checkOnePair(cards: str):
  matches = getCardAmounts(cards)
  has_one_matches = []
  has_three_matches = False

  for key in matches:
    if matches[key] == 2:
      has_one_matches.append(1)

  for key in matches:
    if matches[key] == 3:
      has_three_matches = True

  return len(has_one_matches) == 1 and not has_three_matches

def checkHighCard(cards: str):
  matches = getCardAmounts(cards)
  is_high_cards = True

  for key in matches:
    if matches[key] != 1:
      is_high_cards = False

  return is_high_cards

def getCardAmounts(cards: str):
  letters = list(cards)
  matches = {}
  for letter in letters:
    if matches.get(letter) == None:
      matches[letter] = 0

    matches[letter] += 1

  return matches

def convert_hand_to_ranked_letters(hand: str):
  ranked_letters = {
        "A": "A",
        "K": "B",
        "Q": "C",
        "J": "D",
        "T": "E",
        "9": "F",
        "8": "G",
        "7": "H",
        "6": "I",
        "5": "J",
        "4": "K",
        "3": "L",
        "2": "M",
  }

  new_hand = ""
  for letter in list(hand):
    new_hand += ranked_letters.get(letter)

  return new_hand

def a():
  input_dict = {}

  fiveOfAKindArr = []
  fourOfAKindArr = []
  threeOfAKindArr = []
  fullHouseArr = []
  twoPairArr = []
  onePairArr = []
  highCardArr = []

  with open("./input/day7.txt", "r") as file:
    raw_input = file.readlines()

  input = []
  for line in raw_input:
    hand = convert_hand_to_ranked_letters(line.split(" ")[0])
    bet = line.split(" ")[1].split("\n")[0]
    input_dict[hand] = int(bet)
    input.append(hand)

  for hand in input:
    if checkFiveOfAKind(hand):
        fiveOfAKindArr.append(hand)

    elif checkFourOfAKind(hand):
        fourOfAKindArr.append(hand)

    elif checkFullHouse(hand):
        fullHouseArr.append(hand)

    elif checkThreeOfAKind(hand):
        threeOfAKindArr.append(hand)

    elif checkTwoPair(hand):
        twoPairArr.append(hand)

    elif checkOnePair(hand):
        onePairArr.append(hand)

    elif checkHighCard(hand):
        highCardArr.append(hand)

  fiveOfAKindArr.sort()
  fourOfAKindArr.sort()
  fullHouseArr.sort()
  threeOfAKindArr.sort()
  twoPairArr.sort()
  onePairArr.sort()
  highCardArr.sort()

  list = fiveOfAKindArr + fourOfAKindArr + fullHouseArr + threeOfAKindArr + twoPairArr + onePairArr + highCardArr
  list.reverse()

  result = 0

  index = 1
  for hand in list:
    result += input_dict.get(hand) * index
    index += 1

  return result

# ---------------------------------------------------
# b 251893583, too low
# ---------------------------------------------------
def checkFiveOfAKind_b(cards: str):
  matches = getCardAmounts_b(cards)
  has_matches = False

  for key in matches:
    if matches[key] == 5:
      has_matches = True

  return has_matches

def checkFourOfAKind_b(cards: str):
  matches = getCardAmounts_b(cards)
  has_matches = False

  for key in matches:
    if matches[key] == 4:
      has_matches = True

  return has_matches

def checkThreeOfAKind_b(cards: str):
  matches = getCardAmounts_b(cards)
  has_three_matches = False
  has_two_matches = False

  for key in matches:
    if matches[key] == 3:
      has_three_matches = True

  for key in matches:
    if matches[key] == 2:
      has_two_matches = True

  return has_three_matches and not has_two_matches

def checkFullHouse_b(cards: str):
  matches = getCardAmounts_b(cards)
  has_three_matches = False
  has_two_matches = False

  for key in matches:
    if matches[key] == 3:
      has_three_matches = True

  for key in matches:
    if matches[key] == 2:
      has_two_matches = True

  return has_three_matches and has_two_matches

def checkTwoPair_b(cards: str):
  matches = getCardAmounts_b(cards)
  has_matches = []

  for key in matches:
    if matches[key] == 2:
      has_matches.append(1)

  return len(has_matches) == 2

def checkOnePair_b(cards: str):
  matches = getCardAmounts_b(cards)
  has_one_matches = []
  has_three_matches = False

  for key in matches:
    if matches[key] == 2:
      has_one_matches.append(1)

  for key in matches:
    if matches[key] == 3:
      has_three_matches = True

  return len(has_one_matches) == 1 and not has_three_matches

def checkHighCard_b(cards: str):
  matches = getCardAmounts_b(cards)
  is_high_cards = True

  for key in matches:
    if matches[key] != 1:
      is_high_cards = False

  return is_high_cards

def count_d(hand):
  count = 0
  for char in hand:
    if char == "D":
      count += 1
  return count

def getCardAmounts_b(cards: str):
  letters = list(cards)
  matches = {}
  for letter in letters:
    if matches.get(letter) == None:
      matches[letter] = 0

    matches[letter] += 1

  d_count = count_d(cards)

  letter_to_change = ""
  if d_count > 0:
    num = 0
    for letter in letters:
      if matches[letter] > num:
        num = matches[letter]
        letter_to_change = letter

    # need to consider when there are multiple joker cards. e.g. LMDDD
    # might be better to find a best card for the hand
    # if num = 4. go 4
    # if num = 3. Could be full house or tripple
    # if num = 2. two pair
    # if num = 1. one pair

    matches[letter_to_change] += d_count # need to check what to add to. In a better way 

  return matches

def convert_hand_to_ranked_letters_b(hand: str):
  ranked_letters = {
        "A": "A",
        "K": "B",
        "Q": "C",
        "J": "D",
        "T": "E",
        "9": "F",
        "8": "G",
        "7": "H",
        "6": "I",
        "5": "J",
        "4": "K",
        "3": "L",
        "2": "M",
  }

  new_hand = ""
  for letter in list(hand):
    new_hand += ranked_letters.get(letter)

  return new_hand

def b():
  input_dict = {}

  fiveOfAKindArr = []
  fourOfAKindArr = []
  fullHouseArr = []
  threeOfAKindArr = []
  twoPairArr = []
  onePairArr = []
  highCardArr = []

  with open("./input/day7.txt", "r") as file:
    raw_input = file.readlines()

  input = []
  for line in raw_input:
    hand = convert_hand_to_ranked_letters_b(line.split(" ")[0])
    bet = line.split(" ")[1].split("\n")[0]
    input_dict[hand] = int(bet)
    input.append(hand)

  for hand in input:
    if checkFiveOfAKind_b(hand):
        fiveOfAKindArr.append(hand)

    elif checkFourOfAKind_b(hand):
        fourOfAKindArr.append(hand)

    elif checkFullHouse_b(hand):
        fullHouseArr.append(hand)

    elif checkThreeOfAKind_b(hand):
        threeOfAKindArr.append(hand)

    elif checkTwoPair_b(hand):
        twoPairArr.append(hand)

    elif checkOnePair_b(hand):
        onePairArr.append(hand)

    elif checkHighCard_b(hand):
        highCardArr.append(hand)

  fiveOfAKindArr.sort()
  fourOfAKindArr.sort()
  fullHouseArr.sort()
  threeOfAKindArr.sort()
  twoPairArr.sort()
  onePairArr.sort()
  highCardArr.sort()

  list = fiveOfAKindArr + fourOfAKindArr + fullHouseArr + threeOfAKindArr + twoPairArr + onePairArr + highCardArr
  list.reverse()

  result = 0

  index = 1
  for hand in list:
    result += input_dict.get(hand) * index
    index += 1

  return result

start_time = time.perf_counter()
a_result = a()
end_time = time.perf_counter()
print("day 7 a solution: %s in %s seconds!"%(a_result, round(end_time - start_time, 5)))
#start_time = time.perf_counter()
#b_result = b()
#end_time = time.perf_counter()
#print("day 7 b solution: %s in %s seconds!"%(b_result, round(end_time - start_time, 5)))