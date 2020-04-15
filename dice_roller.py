def main():
    import random
    number_of_players = int(input('How many players are playing? '))
    dice_rolls = int(input('How many dice would you like to roll? '))
    dice_size = int(input('How many sides are the dice? '))
    score_list = []
    for j in range(0,number_of_players):
        dice_sum = 0
        for i in range (0,dice_rolls):
            roll = random.randint(1,dice_size)
            dice_sum = dice_sum + roll
            if roll == 1:
                print(f'Player{j} rolled a {roll}! Critical Fail')
            elif roll == dice_size:
                print(f'Player{j} rolled a {roll}! Critical Success!')
            else:
                print(f'Player{j} rolled a {roll}')
                print(f'Player{j} have rolled a total of {dice_sum}')
        score_list.append(j+1)
        score_list.append(dice_sum)
    max_roll = max(score_list)
    print(f'Final score: {score_list}, Winning score is: {max_roll}, Winner is Player{score_list[score_list.index(max_roll)-1]}')

if __name__== "__main__":
    main()
