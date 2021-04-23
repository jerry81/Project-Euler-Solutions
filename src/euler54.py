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
  return highCard

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
  return highCard


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

def getFourOfAKind(cards):
  freqMap = getFreqMap(cards)
  for val, freq in freqMap.items():
    if freq == 4:
      return val
  return -1


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

  print('4oak 1, -1', getFourOfAKind(cards1))
  print('4oak 2, 9', getFourOfAKind(cards2))

@track_performance
def euler54():
  cards = prepare()
euler54()
testSameSuit()
testStraightHigh()
testFreqMap()
test4()