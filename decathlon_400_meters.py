from Die import Die
def game():
    '''decathlon_400_meters() -> int
    plays a solitare version of Reiner Knizia's 400 Meters
    returns final score'''
    # initializes rerolls, score, and dice
    score = 0
    rerolls = 5
    d1 = Die(6,[1,2,3,4,5,-6])
    d2 = Die(6,[1,2,3,4,5,-6])
    # play 4 rounds
    for gameround in range(1,5):
        print("Your total score so far is "+str(score))
        print("Round " + str(gameround) + " -- you have " + \
              str(rerolls) + " rerolls left.")
        while True:
            # roll the dice
            input("Press enter to roll.")
            d1.roll()
            d2.roll()
            roundscore = d1.getTop() + d2.getTop()
            print("You rolled " + str(d1.getTop()) + " and " + \
                  str(d2.getTop()) + " for a total of " + str(roundscore))
            # if the player has no rerolls, they're stuck with this
            if rerolls==0:
                print("You're out of rerolls so you have to keep this.")
                break
            # see if they want to reroll
            response = 'x'
            while response.lower() not in ['y','n']:
                response = input("Do you want to reroll (y/n)? ")
            if response.lower() == 'n':
                break  # keeping this roll, move on the the next roll
            # they're using a reroll
            rerolls -= 1
            print("OK, you have "+str(rerolls)+" rerolls left.")
        score += roundscore  # update the score
    return score

def print_score():
    print("Your final score is: "+str(game()))

def play_again():
    while True:
        print("------------------------------------")
        response = 'x'
        while response not in ['y','n']:
            response = input("Do you want to play again (y/n)? ").lower()
        if response == 'n':
            break
        print("------------------------------------")
        print_score()
         
print_score()
play_again()
