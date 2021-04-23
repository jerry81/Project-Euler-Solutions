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
    return "up yours"
  
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
def sameSuit(cards):
  pass

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
    print('newHand is ', newHand)
  processedHands = []
  for rawHand in handsRaw:
    p1 = rawHand[:5]
    p2 = rawHand[5:]
    processedHands.append(p1)
    processedHands.append(p2)
  return processedHands
  

@track_performance
def euler54():
  cards = prepare()
  print('cards are ', cards)
euler54()
