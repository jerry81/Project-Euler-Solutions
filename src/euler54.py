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
  'A': 14,
  '0': 0
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
      return -1, [0]
  return highCard, cards # return sorted cards for further comparisons

def getStraightHigh(cards):
  cards.sort(key=lambda x:VALUE_MAP[x.value])
  highCard = VALUE_MAP[cards[0].value]
  for idx, item in enumerate(cards):
    if idx == 0: 
      continue
    curVal = VALUE_MAP[item.value]
    if curVal == highCard:
      return -1, [-1]
    elif curVal != highCard + 1:
      return -1, [-1]
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
  return -1, [0]

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
  _3, _ = getXOfAKind(cards, 3)
  _2, _ = getPairs(cards)
  if (_3 != -1 and len(_2) == 1):
    return _3, _2
  return -1, -1

def get2Pair(cards):
  pairs, remainder = getPairs(cards)
  if len(pairs) != 2:
    return -1
  return max(pairs), pairs, remainder

def getSraightFlushRank(cards):
  sameHigh, sortedCards = getSameSuitHigh(cards)
  straightHigh, _ = getStraightHigh(cards)
  bigRank = 0
  smallRankList = []
  if (sameHigh > 0 and straightHigh > 0):
    bigRank = '9'
    smallRankList = list(map(lambda card: str(VALUE_MAP[card.value]), sortedCards))
    smallRankList.reverse()
  return bigRank, smallRankList

def get4Rank(cards):
  fourHigh, remainingSameHigh = getXOfAKind(cards, 4)
  bigRank = 0
  smallRankList = []
  if (int(fourHigh) > 0):
    bigRank = '8'
    smallRankList = list(map(lambda card: str(VALUE_MAP[card.value]), remainingSameHigh))
    remaining = list(filter(lambda x: x != fourHigh, smallRankList))
    remaining.reverse()
    repeated = list(filter(lambda x: x == fourHigh, smallRankList))
    smallRankList = [*repeated, *remaining]
  return bigRank, smallRankList

def getFHRank(cards):
  triple, pair = getFullHouse(cards)
  bigRank = 0
  smallRank = []
  if (int(triple) > 0):
    bigRank = '7'
    smallRank = [triple, pair[0]]
  return bigRank, smallRank

def getFlushRank(cards):
  sameHigh, sortedCards = getSameSuitHigh(cards)
  straightHigh, _ = getStraightHigh(cards)
  bigRank = 0
  smallRankList = []
  # TODO: extract (getStraightFlushRank getStraightRank)
  if (sameHigh > 0 and straightHigh < 0):
    bigRank = '6'
    smallRankList = list(map(lambda card: str(VALUE_MAP[card.value]), sortedCards))
    smallRankList.reverse()
  return bigRank, smallRankList

def getStraightRank(cards):
  sameHigh, _ = getSameSuitHigh(cards)
  straightHigh, sortedCards = getStraightHigh(cards)
  bigRank = 0
  smallRankList = []
  # TODO: extract (getStraightFlushRank getStraightRank)
  if (sameHigh < 0 and straightHigh > 0):
    bigRank = '5'
    smallRankList = list(map(lambda card: str(VALUE_MAP[card.value]), sortedCards))
    smallRankList.reverse()
  return bigRank, smallRankList

def get3Rank(cards):
  #TODO: extract (repeats with get4Rank)
  threeHigh, remainingSameHigh = getXOfAKind(cards, 3)
  bigRank = 0
  smallRankList = []
  if (int(threeHigh) > 0):
    bigRank = '4'
    smallRankList = list(map(lambda card: str(VALUE_MAP[card.value]), remainingSameHigh))
    remaining = list(filter(lambda x: x != threeHigh, smallRankList))
    remaining.reverse()
    repeated = list(filter(lambda x: x == threeHigh, smallRankList))
    smallRankList = [*repeated, *remaining]
  return bigRank, smallRankList

def getRank(cards):
  pass
  # 10 big ranks
  #   High Card: Highest value card.
  # One Pair: Two cards of the same value.
  # Two Pairs: Two different pairs.
  # Three of a Kind: Three cards of the same value.
  # Straight: All cards are consecutive values. - done
  # Flush: All cards of the same suit. - done
  # Full House: Three of a kind and a pair. - done 
  # Four of a Kind: Four cards of the same value. - done 
  # Straight Flush: All cards are consecutive values of same suit. - done 
  # Royal Flush: Ten, Jack, Queen, King, Ace, in same suit. - done

def testStraightFlushRank():
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

  rank1 = getSraightFlushRank(cards1)
  rank2 = getSraightFlushRank(cards2)

  print('SF rank expected: 9.65432', rank1)
  print('SF rank expected: 0', rank2)

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

def test4Rank():
  cards1 = []
  cards1.append(Card('H', '7'))
  cards1.append(Card('S', '7'))
  cards1.append(Card('D', '7'))
  cards1.append(Card('C', '7'))
  cards1.append(Card('H', 'A'))
  
  cards2 = []
  cards2.append(Card('H', '9'))
  cards2.append(Card('S', '9'))
  cards2.append(Card('C', '9'))
  cards2.append(Card('H', '5'))
  cards2.append(Card('D', 'K'))

  print('4oakRank: 8 [7777, 14] is ', get4Rank(cards1))
  print('4oakRank: 0.0 is', get4Rank(cards2))

def test3Rank():
  cards1 = []
  cards1.append(Card('H', '7'))
  cards1.append(Card('S', '7'))
  cards1.append(Card('D', '7'))
  cards1.append(Card('C', 'A'))
  cards1.append(Card('H', '5'))
  
  cards2 = []
  cards2.append(Card('H', '9'))
  cards2.append(Card('S', '9'))
  cards2.append(Card('C', 'Q'))
  cards2.append(Card('H', '5'))
  cards2.append(Card('D', 'K'))

  print('3 rank: 4 [7,7,7,14,5] is ', get3Rank(cards1))
  print('3 rank: 0 [] is', get3Rank(cards2))

def testFHRank():
  cards1 = []
  cards1.append(Card('H', '7'))
  cards1.append(Card('S', '7'))
  cards1.append(Card('D', '7'))
  cards1.append(Card('C', '5'))
  cards1.append(Card('H', '5'))
  
  cards2 = []
  cards2.append(Card('H', '9'))
  cards2.append(Card('S', '9'))
  cards2.append(Card('C', '5'))
  cards2.append(Card('H', '5'))
  cards2.append(Card('D', 'K'))

  print('fhRank: 7.75 is ', getFHRank(cards1))
  print('fhRank: 0.0 is', getFHRank(cards2))

def testFlushRank():
  cards1 = []
  cards1.append(Card('H', 'J'))
  cards1.append(Card('H', 'Q'))
  cards1.append(Card('H', 'K'))
  cards1.append(Card('H', 'A'))
  cards1.append(Card('H', '5'))
  
  cards2 = []
  cards2.append(Card('H', '9'))
  cards2.append(Card('S', '9'))
  cards2.append(Card('C', '5'))
  cards2.append(Card('H', '5'))
  cards2.append(Card('D', 'K'))

  print('flush rank: 6.141312115 is ', getFlushRank(cards1))
  print('flush rank: 0.0 is', getFlushRank(cards2))

def testStraightRank():
  cards1 = []
  cards1.append(Card('H', 'J'))
  cards1.append(Card('D', 'Q'))
  cards1.append(Card('H', 'K'))
  cards1.append(Card('C', '9'))
  cards1.append(Card('H', '10'))
  
  cards2 = []
  cards2.append(Card('H', '9'))
  cards2.append(Card('S', '9'))
  cards2.append(Card('C', '5'))
  cards2.append(Card('H', '5'))
  cards2.append(Card('D', 'K'))

  print('straight rank: 5.131211109 is ', getStraightRank(cards1))
  print('straight rank: 0.0 is', getStraightRank(cards2))

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
testStraightFlushRank()
test4Rank()
testFHRank()
testFlushRank()
testStraightRank()
test3Rank()