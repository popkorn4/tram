import random, string
def game(play,money):
    # list of cards
    
    card_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
    # value of each card
    
    card_value = {"A": 1,
                  "2": 2,
                  "3": 3,
                  "4": 4,
                  "5": 5,
                  "6": 6,
                  "7": 7,
                  "8": 8,
                  "9": 9,
                  "10": 0,
                  "J": 0,
                  "Q": 0,
                  "K": 0}
    
    # the range of money that players can bet
    
    money_range = 100000000000000000000000000000000000000
    
    
    player = "p"
    banker = "b"
    tie = "t"
    
    
    
    print( "Guide:\ntype p for Player, t for Tie and b for Banker and q to quit the game" )
    
    
    player_cards = random.sample(card_list,2)
    banker_cards = random.sample(card_list,2)
    
    
    
    
    ferst_card_p = player_cards[0]
    second_card_p = player_cards[1]
    
    ferst_card_b = banker_cards[0]
    second_card_b = banker_cards[1]
    
    a=card_value[ferst_card_p] + card_value[second_card_p]
    b=card_value[ferst_card_b] + card_value[second_card_b]
    player_cost=a%10
    banker_cost=b%10
    
    if player_cost < 6:
        add_player_card = random.choice(card_list)
        player_cards.append(add_player_card)
        third_card_p=player_cards[2]
        a=card_value[third_card_p]+card_value[ferst_card_p] + card_value[second_card_p]
        player_cost=a%10
    if banker_cost < 6:
        add_banker_card = random.choice(card_list)
        banker_cards.append(add_banker_card)
        third_card_b=banker_cards[2]
        b=card_value[third_card_b]+card_value[ferst_card_b] + card_value[second_card_b]
        banker_cost=b%10
    
    
    while True:
        if play in ("p", "P"):
            print("you bet on Player")
            break
        elif play in ("t", "T"):
            print("you bet on Tie")
            break
        elif play in ("b", "B"):
            print("you bet on Banker")
            break
        elif play in ("q", "Q"):
            print("Thanks for playing Baccarat.")
            break
        else:
            print("Please type P for Player, T for Tie or B for Banker")
        
    
    
    
    def bet_amount():
        Vova=""
        while True:
            # money = int(input("How much money do you want to bet on:" ))
            if 1 <= money <= 1000000000:
                print("You bet {} on {}".format(money, play))
                print("Player's cards", player_cards)
                print("Player's cost:", player_cost)
                print("Banker's cards", banker_cards)
                print("Banker's cost:", banker_cost)
                break
            
            
            elif money > money_range or money < 1:
                print("please type a number between 1 and 10000")
                break
            elif money in ("q", "Q"):
                print("Thanks for playing Baccarat.")
                break
        a=0  
        
        while a<1:
            if player_cost>banker_cost and play == "p":
                Vova="Вы выйграли!!!"
                a+=1
            elif player_cost<banker_cost and play == "p":
                Vova="Вы проиграли :("
                a+=1
            break
        while a<1:
            if player_cost<banker_cost and play == "b":
               Vova="Вы выйграли!!!"
               a+=1
            elif player_cost>banker_cost and play == "b":
                Vova="Вы проиграли :("
                a+=1
            break
        while a<1:
            if player_cost==banker_cost and play == "t":
                Vova="Вы выйграли!!!"
                a+=1
            else:
                Vova="Вы проиграли :("
                a+=1
        return Vova
    net=bet_amount()
    game_info={
        "player_cards":player_cards,
        "banker_cards":banker_cards,
        "net":net,
        "player_cost":player_cost,
        "banker_cost":banker_cost
    }
    return game_info
    
    
    