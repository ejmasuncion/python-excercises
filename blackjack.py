import random
import os
# from art import logo

clear = lambda: os.system('cls')

def deal_card():
    card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(card_list)

def calculate_score(card_hand):
    value1 = sum(card_hand)
    if value1 == 21 and len(card_hand) == 2:
        return 0
    elif 11 in card_hand and value1 > 21:
        card_hand.remove(11)
        card_hand.append(1)
        return value1
    else:
        return value1

def compare(user_total, computer_total):
    if user_total == computer_total:
        print("Draw")
    elif computer_total == 0:
        print("Computer won.")
    elif user_total == 0:
        print("You won.")
    elif user_total > 21:
        print("Computer won.")
    elif computer_total > 21:
        print("You won.")
    else:
        if user_total > computer_total:
            print("You won.")
        else:
            print("Computer won")
    

def play_game():
    # print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for x in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while is_game_over == False:
        user_total = calculate_score(user_cards)
        computer_total = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_total}")
        print(f"   Computer first card: {computer_cards[0]}")

        if computer_total == 0 or user_total == 0 or user_total > 21:
            is_game_over = True
        else:
            user_draw_another = input("Do you want to draw another card? 'y' if yes and 'n' if no. ")
            if user_draw_another == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True


    while computer_total != 0 and computer_total < 17:
        computer_cards.append(deal_card())
        computer_total = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_total}")
    print(f"   Computer final hand: {computer_cards}, final score: {computer_total}")
    compare(user_total, computer_total)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    play_game()

