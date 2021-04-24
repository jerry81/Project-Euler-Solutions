from utils.annotations import track_performance
import math
from utils.fileUtils import openAndSplitPlus

print('project euler problem 54')

CARD_FACES = range(13)

class Card:
  suit = "h" # s, c, d, h
  value = 0 # 2
  def __init__(self,s,v):
    self.suit = s
    self.value = v 
  def __str__(self):
    return f'suit {self.suit}, value {self.value}'

class H2HResult:
  rank: -1
  high: -1
  def __init__(self,r,h):
    self.rank = r
    self.high = h
  
VALUE_MAP = {
  '2': 2,
  '3': 3,
  '4': 4,
  '5': 5,
  '6': 6,
  '7': 7,  
  '8': 8,
  '9': 9,
  '10': 10,
  'J': 11,
  'Q': 12,
  'K': 13,
  'A': 14
} 
SUIT_MAP = {
  'C': 1,
  'D': 2,
  'H': 3,
  'S': 4
}
def getSameSuitHigh(cards):
  cards.sort(key=lambda x:VALUE_MAP[x.value])
  highCard = VALUE_MAP[cards[4].value]
  suit = cards[0].suit
  for card in cards:
    if suit != card.suit:
      return -1
  return highCard, cards # return sorted cards for further comparisons

def getStraightHigh(cards):
  cards.sort(key=lambda x:VALUE_MAP[x.value])
  highCard = VALUE_MAP[cards[0].value]
  for idx, item in enumerate(cards):
    if idx == 0: 
      continue
    curVal = VALUE_MAP[item.value]
    if curVal == highCard:
      return -1
    elif curVal != highCard + 1:
      return -1
    highCard = curVal
  return highCard, cards

def prepare():
  games = openAndSplitPlus('./resources/p054_poker.txt', '\n')
  cards = list(
    map(lambda card: card.split(' '), games)
  )
  filteredCards = list(
    filter(lambda hand: len(hand) > 1, cards)
  )
  handsRaw = []
  for hand in filteredCards:
    newHand = list(map(lambda c: Card(c[1], c[0]),hand))
    handsRaw.append(newHand)
  processedHands = []
  for rawHand in handsRaw:
    p1 = rawHand[:5]
    p2 = rawHand[5:]
    processedHands.append(p1)
    processedHands.append(p2)
  return processedHands

def getFreqMap(cards):
  freqMap = {}
  for card in cards:
    val = card.value 
    try:
      freqMap[val] += 1
    except:
      freqMap[val] = 1
  return freqMap

def getXOfAKind(cards, x):
  cards.sort(key=lambda x:VALUE_MAP[x.value])
  freqMap = getFreqMap(cards)
  for val, freq in freqMap.items():
    if freq == x:
      remainder = list(filter(lambda x: x != val, cards))
      return val, remainder
  return -1

def getPairs(cards):
  cards.sort(key=lambda x:VALUE_MAP[x.value])
  freqMap = getFreqMap(cards)
  pairs = []
  for val, freq in freqMap.items():
    if freq == 2:
      pairs.append(val)
  remainder = list(filter(lambda x: x not in pairs, cards))
  return pairs, remainder

def getFullHouse(cards):
  _3 = getXOfAKind(cards, 3)
  _2 = getPairs(cards)
  if (_3 != -1 and len(_2) == 1):
    return _3, _2
  return -1

def get2Pair(cards):
  pairs, remainder = getPairs(cards)
  if len(pairs) != 2:
    return -1
  return max(pairs), pairs, remainder

def testSameSuit():
  cards1 = []
  cards1.append(Card('H', '2'))
  cards1.append(Card('H', '3'))
  cards1.append(Card('H', '4'))
  cards1.append(Card('H', '5'))
  cards1.append(Card('H', '6'))
  
  cards2 = []
  cards2.append(Card('H', '2'))
  cards2.append(Card('S', '3'))
  cards2.append(Card('H', '4'))
  cards2.append(Card('H', '5'))
  cards2.append(Card('H', '6'))
  
  print('6 is ', getSameSuitHigh(cards1))
  print('-1 is ', getSameSuitHigh(cards2))

def testStraightHigh():
  cards1 = []
  cards1.append(Card('H', '7'))
  cards1.append(Card('H', '3'))
  cards1.append(Card('H', '4'))
  cards1.append(Card('H', '5'))
  cards1.append(Card('H', '6'))
  
  cards2 = []
  cards2.append(Card('H', '9'))
  cards2.append(Card('S', '3'))
  cards2.append(Card('H', '4'))
  cards2.append(Card('H', '5'))
  cards2.append(Card('H', '6'))

  print('7 is ', getStraightHigh(cards1))
  print('-1 is ', getStraightHigh(cards2))

def testFreqMap():
  cards1 = []
  cards1.append(Card('H', '7'))
  cards1.append(Card('H', '3'))
  cards1.append(Card('H', '4'))
  cards1.append(Card('H', '5'))
  cards1.append(Card('H', '6'))
  
  cards2 = []
  cards2.append(Card('H', '9'))
  cards2.append(Card('S', '9'))
  cards2.append(Card('C', '9'))
  cards2.append(Card('H', '5'))
  cards2.append(Card('H', '6'))

  print('freqMap 1, 7 high', getFreqMap(cards1))
  print('freqMap 2, 3 nines', getFreqMap(cards2))

def test4():
  cards1 = []
  cards1.append(Card('H', '7'))
  cards1.append(Card('H', '3'))
  cards1.append(Card('H', '4'))
  cards1.append(Card('H', '5'))
  cards1.append(Card('H', '6'))
  
  cards2 = []
  cards2.append(Card('H', '9'))
  cards2.append(Card('S', '9'))
  cards2.append(Card('C', '9'))
  cards2.append(Card('H', '5'))
  cards2.append(Card('D', '9'))

  print('4oak 1, -1', getXOfAKind(cards1, 4))
  print('4oak 2, 9', getXOfAKind(cards2, 4))

def test3():
  cards1 = []
  cards1.append(Card('H', '7'))
  cards1.append(Card('H', '3'))
  cards1.append(Card('H', '4'))
  cards1.append(Card('H', '5'))
  cards1.append(Card('H', '6'))
  
  cards2 = []
  cards2.append(Card('H', '9'))
  cards2.append(Card('S', '9'))
  cards2.append(Card('C', '9'))
  cards2.append(Card('H', '5'))
  cards2.append(Card('D', 'K'))

  print('3oak 1, -1', getXOfAKind(cards1, 3))
  print('3oak 2, 9', getXOfAKind(cards2, 3))

def testPairs():
  cards1 = []
  cards1.append(Card('H', '7'))
  cards1.append(Card('H', '3'))
  cards1.append(Card('H', '4'))
  cards1.append(Card('H', '5'))
  cards1.append(Card('H', '6'))
  
  cards2 = []
  cards2.append(Card('H', '9'))
  cards2.append(Card('S', '9'))
  cards2.append(Card('C', '9'))
  cards2.append(Card('H', '5'))
  cards2.append(Card('D', 'K'))


  cards3 = []
  cards3.append(Card('H', '9'))
  cards3.append(Card('S', '9'))
  cards3.append(Card('C', 'A'))
  cards3.append(Card('H', '5'))
  cards3.append(Card('D', 'K'))


  cards4 = []
  cards4.append(Card('H', '9'))
  cards4.append(Card('S', '9'))
  cards4.append(Card('C', '10'))
  cards4.append(Card('H', '10'))
  cards4.append(Card('D', 'K'))

  print('pairs -1', getPairs(cards1))
  print('pairs -1', getPairs(cards2))
  print('pairs 9', getPairs(cards3))
  print('pairs 9, 10', getPairs(cards4))

def testFH():
  cards1 = []
  cards1.append(Card('H', '7'))
  cards1.append(Card('S', '7'))
  cards1.append(Card('D', '4'))
  cards1.append(Card('C', '4'))
  cards1.append(Card('H', '4'))
  
  cards2 = []
  cards2.append(Card('H', '9'))
  cards2.append(Card('S', '9'))
  cards2.append(Card('C', '9'))
  cards2.append(Card('H', '5'))
  cards2.append(Card('D', 'K'))

  print('FH: 4 is ', getFullHouse(cards1))
  print('FH: -1 is', getFullHouse(cards2))

def test2P():
  cards1 = []
  cards1.append(Card('H', '7'))
  cards1.append(Card('S', '7'))
  cards1.append(Card('D', '4'))
  cards1.append(Card('C', '4'))
  cards1.append(Card('H', '5'))
  
  cards2 = []
  cards2.append(Card('H', '9'))
  cards2.append(Card('S', '9'))
  cards2.append(Card('C', '9'))
  cards2.append(Card('H', '5'))
  cards2.append(Card('D', 'K'))

  print('2P: 7 is ', get2Pair(cards1))
  print('2P: -1 is', get2Pair(cards2))

@track_performance
def euler54():
  cards = prepare()
euler54()
testSameSuit()
testStraightHigh()
testFreqMap()
test4()
test3()
testPairs()
testFH()
test2P()