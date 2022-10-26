import random

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Takes a list of cards and returns the score."""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  """Compares cards between the user and computer."""
  if user_score > 21 and computer_score > 21:
    return "You lose! You went over 21!"

  if user_score == computer_score:
    return "Draw!"
  elif computer_score == 0:
    return "You lose! Opponent has blackjack!"
  elif user_score == 0:
    return "You win! Blackjack!"
  elif user_score > 21:
    return "You lose! You went over 21!"
  elif computer_score > 21:
    return "You win! Opponent went over 21!"
  elif user_score > computer_score:
    return "You win! You were closer to 21!"
  else:
    return "You lose! Opponent was closer to 21!"

user_cards = []
computer_cards = []
is_game_over = False

for _ in range(2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())

while not is_game_over:
  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)
  print(f"Your cards: {user_cards}, Your score: {user_score}")
  print(f"Opponents first card: {computer_cards[0]}")

  if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True
  else:
    user_draw_again = input('Type "y" to get another card, type "n" to pass: ')
    if user_draw_again == 'y':
      user_cards.append(deal_card())
    elif user_draw_again == 'n':
      is_game_over = True
  
while computer_score != 0 and computer_score < 17:
  computer_cards.append(deal_card())
  computer_score = calculate_score(computer_cards)

print(f"Your final hand: {user_cards}, final score: {user_score}")
print(f"Opponents final hand: {user_cards}, opponents final score: {user_score}")
print(compare(user_score, computer_score))
