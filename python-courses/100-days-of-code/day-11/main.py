import random as r
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def win(pl_hand, pc_hand):
    pl=abs(21-sum(pl_hand))
    pc=abs(21-sum(pc_hand))
    pl_score=sum(pl_hand)
    pc_score=sum(pc_hand)
    if sum(pc_hand)>21:
        print("Opponent went over. You win 😁")
    elif pl == pc:
        print("Draw 🙃")
    elif pl<pc and pl_score != 21:
        print("You win 😃")
    elif pl<pc and pl_score == 21:
        print("Win with a Blackjack 😎")
    elif pc<pl and pc_score ==  21:
        print("opponent has Blackjack 😱 you lose")
    elif pc<pl and pc_score != 21:
        print(" You lose 😤")


def ace_control(hand):
    ace=False
    for i in hand:
        if i == 11:
            ace = True
    return ace
def display_hands(durum,pl_hand, pc_hand):
    if durum ==0:
        print(f"Your hand: {pl_hand}, current score: {sum(pl_hand)}")
        print(f"Computer's first card: {pc_hand}")
    elif durum ==1:
        print(f"Your final hand: {pl_hand}, final score: {sum(pl_hand)}")
        print(f"Computer's final hand: {pc_hand}, final score: {sum(pc_hand)}")
def hand_filler(kac_kere, hand):
    for i in range(kac_kere):
        hand.append(r.choice(cards))

def blackjack():
    want_to_play = True
    while want_to_play:
        computer_hand=[]
        player_hand=[]
        # ace_player=False
        # ace_computer=False

        def went_over():
            if sum(player_hand) > 21:
                display_hands(1,player_hand, computer_hand)
                print("You went over. You lose 😭")
                #blackjack()
                return True
            else :
                return False

        want_to_play=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if want_to_play != "n" and want_to_play != "y":
            while want_to_play != "n" and want_to_play != "y":
                want_to_play=input("invalid input. Please enter either 'y' or 'n': ").lower()
        if want_to_play=="n":
            want_to_play = False
            break
        print(art.logo)
        hand_filler(2, player_hand)
        hand_filler(1, computer_hand)

        if ace_control(player_hand):  #baslangıcta ıkı ace varsa bırını 1 e cevırıyoz
            if sum(player_hand) > 21:
                player_hand[0]=1
        display_hands(0,player_hand, computer_hand)




        cnt = True
        while cnt:
            choose=input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if choose == "y":
                hand_filler(1,player_hand)
                if sum(player_hand) > 21:
                    if 11 in player_hand:
                        while sum(player_hand) > 21:
                            player_hand[player_hand.index(11)]=1
                if went_over():
                    break
                display_hands(0,player_hand, computer_hand)
            elif choose == "n":
                cnt =False
                while sum(computer_hand) <17:
                    hand_filler(1, computer_hand)
                    if 11 in computer_hand:
                        if sum(computer_hand) > 21:
                            while sum(computer_hand) > 21 and 11 in computer_hand:
                                computer_hand[computer_hand.index(11)] = 1
                display_hands(1,player_hand,computer_hand)
                win(player_hand,computer_hand)














blackjack()