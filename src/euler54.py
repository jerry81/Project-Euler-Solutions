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

def getHighCard(cards):
  cards.sort(key=lambda x:VALUE_MAP[x.value])
  bigRank = '1'
  cards = list(map(lambda card: str(VALUE_MAP[card.value]), cards))
  cards.reverse()
  return bigRank, cards
  

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
      pairs.append(VALUE_MAP[val])
  remainder = list(filter(lambda x: VALUE_MAP[x.value] not in pairs, cards))
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
    return -1, -1, -1
  return max(pairs), pairs, remainder

def getPairRank(cards):
  pairs, remainder = getPairs(cards)
  bigRank = 0
  smallRankList = []
  if len(pairs) == 1 and int(pairs[0]) > 0:
    bigRank = '2'
    remainder = list(map(lambda card: str(VALUE_MAP[card.value]), remainder))
    remainder.reverse()
    smallRankList = [int(pairs[0]), *remainder]
  return bigRank, smallRankList

def get2PairRank(cards):
  maxPair, pairs, remainder = get2Pair(cards)
  bigRank = 0
  smallRankList = []
  if int(maxPair) > 0:
    bigRank = '3'
    remainder = list(map(lambda card: str(VALUE_MAP[card.value]), remainder))
    pairs.reverse()
    smallRankList = [*pairs, int(remainder[0])]
  return bigRank, smallRankList

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

def compareSmallRanks(arr1, arr2):
  total = len(arr1)
  for idx, item in enumerate(arr1):
    arr2Item = arr2[idx]
    if item > arr2Item:
      return 0
    if arr2Item > item:
      return 1

def getRank(cards):
  TESTERS = [
    getSraightFlushRank, 
    get4Rank,
    getFHRank,
    getFlushRank,
    getStraightRank,
    get3Rank,
    get2PairRank,
    getPairRank,
    getHighCard
  ]
  for fn in TESTERS:
    big, small = fn(cards)
    if (int(big) > 0):
      return big, small

def compareHands(hand1, hand2):
  big1, sm1 = getRank(hand1)
  big2, sm2 = getRank(hand2)
  if int(big1) > int(big2):
    return 0
  if int(big2) > int(big1):
    return 1
  return compareSmallRanks(sm1, sm2)

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

def test2PRank():
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
  cards2.append(Card('H', 'K'))
  cards2.append(Card('D', 'K'))

  print('2P rank: 0 [] is ', get2PairRank(cards1))
  print('2P rank: 3 KK,99,5 is', get2PairRank(cards2))

def testPairRank():
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
  cards2.append(Card('H', 'Q'))
  cards2.append(Card('D', 'K'))

  print('pair rank: 0 [] is ', getPairRank(cards1))
  print('pair rank: 2 99,K, Q, 5 is', getPairRank(cards2))

def testGetHighCard():
  cards1 = []
  cards1.append(Card('H', 'J'))
  cards1.append(Card('D', 'Q'))
  cards1.append(Card('H', 'K'))
  cards1.append(Card('C', '3'))
  cards1.append(Card('H', '10'))
  
  cards2 = []
  cards2.append(Card('H', '9'))
  cards2.append(Card('S', '9'))
  cards2.append(Card('C', '5'))
  cards2.append(Card('H', 'Q'))
  cards2.append(Card('D', 'K'))

  print('pair rank: 1 [KQJ 10 3] is ', getHighCard(cards1))
  print('pair rank: 1 [K Q 99 5]', getHighCard(cards2))

def testCompareSmallRanks():
  sm1 = [7, 5, 14]
  sm2 = [7, 2, 14]
  print('0 is ', compareSmallRanks(sm1, sm2))
  print('1 is ', compareSmallRanks(sm2, sm1))
  sm3 = ['14', '7', '7', '5', '5']
  sm4 = ['14', '7', '7', '5', '2']
  print('0 is ', compareSmallRanks(sm3, sm4))
  print('1 is ', compareSmallRanks(sm4, sm3))

def testCompareHands():
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
  cards2.append(Card('H', 'Q'))
  cards2.append(Card('D', 'K'))

  cards3 = []
  cards3.append(Card('H', '9'))
  cards3.append(Card('S', '9'))
  cards3.append(Card('C', 'A'))
  cards3.append(Card('H', 'Q'))
  cards3.append(Card('D', 'K'))

  print('compare hands: 0 is ', compareHands(cards1, cards2))
  print('compare hands: 1 is ', compareHands(cards2, cards3))

def testGetRank():
  cards1 = []
  cards1.append(Card('H', 'J'))
  cards1.append(Card('D', 'Q'))
  cards1.append(Card('H', 'K'))
  cards1.append(Card('C', '3'))
  cards1.append(Card('H', '10'))
  
  cards2 = []
  cards2.append(Card('H', '9'))
  cards2.append(Card('H', '10'))
  cards2.append(Card('H', 'J'))
  cards2.append(Card('H', 'Q'))
  cards2.append(Card('H', 'K'))

  cards3 = []
  cards3.append(Card('D', '9'))
  cards3.append(Card('H', '9'))
  cards3.append(Card('C', '9'))
  cards3.append(Card('S', '9'))
  cards3.append(Card('H', 'K'))

  cards4 = []
  cards4.append(Card('H', '7'))
  cards4.append(Card('S', '7'))
  cards4.append(Card('D', '7'))
  cards4.append(Card('C', '5'))
  cards4.append(Card('H', '5'))

  cards5 = []
  cards5.append(Card('S', 'A'))
  cards5.append(Card('S', '7'))
  cards5.append(Card('S', '7'))
  cards5.append(Card('S', '5'))
  cards5.append(Card('S', '5'))

  cards6 = []
  cards6.append(Card('H', '2'))
  cards6.append(Card('S', '3'))
  cards6.append(Card('D', '4'))
  cards6.append(Card('C', '5'))
  cards6.append(Card('H', '6'))

  cards7 = []
  cards7.append(Card('H', '7'))
  cards7.append(Card('S', '7'))
  cards7.append(Card('D', '7'))
  cards7.append(Card('C', '5'))
  cards7.append(Card('H', '6'))

  cards8 = []
  cards8.append(Card('S', 'A'))
  cards8.append(Card('S', '7'))
  cards8.append(Card('D', '7'))
  cards8.append(Card('S', '5'))
  cards8.append(Card('S', '5'))

  cards9 = []
  cards9.append(Card('H', '2'))
  cards9.append(Card('S', '2'))
  cards9.append(Card('D', '4'))
  cards9.append(Card('C', '5'))
  cards9.append(Card('H', '6'))

  print('rank: 1 is ', getRank(cards1))
  print('rank: 9 is ', getRank(cards2))
  print('rank: 8 is ', getRank(cards3))
  print('rank: 7 is ', getRank(cards4))
  print('rank: 6 is ', getRank(cards5))
  print('rank: 5 is ', getRank(cards6))
  print('rank: 4 is ', getRank(cards7))
  print('rank: 3 is ', getRank(cards8))
  print('rank: 2 is ', getRank(cards9))

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
test2PRank()
testPairRank()
testGetHighCard()
testGetRank()
testCompareSmallRanks()
testCompareHands()