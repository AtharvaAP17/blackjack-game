import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

computer = []
user = []
computer_score = 0
user_score = 0
hit = True
continue_game = True

def user_draws_a_card():
    return random.choice(cards)

def computer_draws_a_card():
    return random.choice(cards)

def compare_score():
    if user_score == 21:
        print(f"You have {user} which equals {user_score}\nThe dealer has {computer} which equals {sum(computer)}\nYou Won! 😎")
    elif user_score > computer_score:
        print(f"You have {user} which equals {user_score}\nThe dealer has {computer} which equals {sum(computer)}\nYou Won! 😎")
    elif user_score == computer_score:
        print(f"You have {user} which equals {user_score}\nThe dealer has {computer} which equals {sum(computer)}\nIt's a Draw.-_-")
    elif computer_score > 21:
        print(f"The Dealer has {computer} which equals {computer_score}\nIt's a BUST!\nYou Won! 😎")
    else:
        print(f"You have {user} which equals {user_score}\nThe dealer has {computer} which equals {sum(computer)}\nYou Lose! 😭")

while continue_game:
    play_game = input("Do you want to play a game of BlackJack? 'y' or 'n'\n").lower()
    if play_game == 'y':
        computer.clear()
        user.clear()
        computer_score = 0
        user_score = 0
        hit = True
        print("\n" * 50)
        print(art.logo)
        #Drawing 2 cards each for the computer and the user
        computer.append(random.choice(cards))
        computer.append(random.choice(cards))
        user.append(random.choice(cards))
        user.append(random.choice(cards))

        # 2 Ace in the first draw condition
        if computer[0] == 11  and computer[1] == 11:
            computer[1] = 1
        if user[0] == 11 and user[1] == 22:
            computer[1] = 1

        print(f"Dealer has: {computer[0]}, ?, \nYou have: {user}")

        #Initial BlackJack Check
        if sum(user) == 21:
            print(f"BlackJack!! 🤯 {user} = {sum(user)}\nYou Won! 😎")
        elif sum(computer) == 21:
            print(f"BlackJack!! 🤯 {computer} = {sum(computer)}\nYou Lose! 😭")
        else:
            while hit and user_score <= 21 :
                hit_or_stand = input("Hit or stand? Press 'y' to hit or 'n' to stand. ").lower()
                if hit_or_stand == 'y':
                    computer_score = sum(computer)
                    user_score = sum(user)
                    user_card = user_draws_a_card()
                    if user_card == 11:
                        if (user_score + user_card) > 21:
                            user_card = 1
                            user.append(user_card)
                            user_score = sum(user)
                            print(f"You drew {user_card}\nYou now have {user} = {user_score}")
                        else:
                            user_card = 11
                            user.append(user_card)
                            user_score = sum(user)
                            print(f"You drew {user_card}\nYou now have {user} = {user_score}")
                    elif 11 in user and ((user_score + user_card) > 21):
                        user.append(user_card)
                        user_score = sum(user)
                        print(f"You drew {user_card}\nYou now have {user} = {user_score}")
                        user_ace_index = user.index(11)
                        user[user_ace_index] = 1
                        user_score = sum(user)
                        print(f"Your Ace hand(11) got converted to '1'\nYou now have {user} = {user_score}")
                    else:
                        user.append(user_card)
                        user_score = sum(user)
                        print(f"You drew {user_card}\nYou now have {user} = {user_score}")
                    if user_score > 21:
                        print(f"You have {user} which equals {user_score}\nIt's a BUST!\nYou Lose! 😭")
                        hit = False
                    elif user_score == 21:
                        compare_score()
                        hit = False
                elif hit_or_stand == 'n':
                    hit = False
                    computer_score = sum(computer)
                    user_score = sum(user)
                    if computer_score < 17:
                        while computer_score < 17:
                            computer_card = computer_draws_a_card()
                            if computer_card == 11:
                                if (computer_score + computer_card) > 21:
                                    computer_card = 1
                                    computer.append(computer_card)
                                    computer_score = sum(computer)
                                    print(f"The Dealer draws {computer_card}\nThe Dealer now has{computer} = {computer_score}")
                                else:
                                    computer_card = 11
                                    computer.append(computer_card)
                                    computer_score = sum(computer)
                                    print(f"The Dealer draws {computer_card}\nThe Dealer now has{computer} = {computer_score}")
                            elif 11 in computer and ((computer_score + computer_card) > 21):
                                computer.append(computer_card)
                                computer_score = sum(computer)
                                print(f"The Dealer drew {computer_card}\nThe Dealer has{computer} = {computer_score}")
                                computer_ace_index = computer.index(11)
                                computer[computer_ace_index] = 1
                                computer_score = sum(computer)
                                print(f"The Dealer's Ace hand(11) got converted to '1'\nThe Dealer now has {computer} = {computer_score}")
                            else:
                                computer.append(computer_card)
                                computer_score = sum(computer)
                                print(f"The Dealer draws {computer_card}\nThe Dealer now has{computer} = {computer_score}")
                        compare_score()
                    elif  computer_score >= 17 and computer_score <= 21:
                        compare_score()
                    else:
                        compare_score()
    else:
        print("Goodbye!")
        continue_game = False