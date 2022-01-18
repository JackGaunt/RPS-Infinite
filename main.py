import random



# console back and forth to decide how the game will be played
def play_game():
    while (True):
        options = input("\nHow many different options for rps do you want?\n")
        try:
            options = int(options)
            print()
            if options % 2 == 0:
                print("Options must be odd")
            if options <= 1:
                print("Options must be greater than 1")
            if options > 2001:
                print("Options must be less than 2000")
            if options % 2 != 0 and 1 < options < 2000:
                break
        except:
            print("Options must be an integer\n")

    if options == 3:
        print("1 - Rock\n2 - Paper\n3 - Scissors")
    elif options == 5:
        print("1 - Rock\n2 - Spock\n3 - Paper\n4 - Lizard\n5 - Scissors")

    while True:
        h_move = input("What is your move?\n")
        try:
            h_move = int(h_move)
            if h_move <= 0 or h_move > options:
                print("Move out of range\n")
            else:
                break
        except:
            print("Move must be an integer")

    print(rps(h_move, options))
    
    again = input("Play again? (y/n)\n").lower()
    if again == "y" or again == "yes":
        play_game()
    else:
        print("Game End")
    


# see excel file for a visualization of how the code works
def rps(h_move, options):
    c_move = random.randint(1, options)
    c_move_calc = int(c_move * 2**((options-1)/2))
    decision = (c_move_calc + h_move) % options
    if decision == 0:
        outcome = "Draw"
    elif decision < options / 2:
        outcome = "Human wins with move #" + str(h_move) + " against computer move #" + str(c_move)
    elif decision > options / 2:
        outcome = "Computer wins with move #" + str(c_move) + " against computer move #" + str(h_move)
    else:
        outcome = "Oh no"
    return "\n" + outcome

if __name__ == "__main__":
    play_game()