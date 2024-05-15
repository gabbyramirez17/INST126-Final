import random
import matplotlib.pyplot as plt

def roll_dice():
    '''Simulate rolling three dice'''
    return [random.randint(1,6) for _ in range(3)]

def tupled_out(dice):
    '''Check if all the three dice have the same number'''
    return len(set(dice)) == 1

def fixed_dice(dice):
    '''Check if two dice have the same value'''
    return len(set(dice)) == 2
def play_turn():
    '''Simulate a player's turn'''
    total_score = 0
    dice = roll_dice()
    print("You rolled:", dice)
    while True:
        if tupled_out(dice):
            print("Tupled out! You have no points scored!")
            return 0
        elif fixed_dice(dice):
            fixed_value = dice[0]
            print("Two dice have the same value:", fixed_value)
            choice = input("Do you want to roll the remaining dice? y or n:")
            if choice.lower() == 'n':
                total_score += sum(d for d in dice if d != fixed_value)
                print("Total Score for this turn is: ", total_score)
                return total_score
            else:
                dice = [fixed_value if d != fixed_value else random.randint(1,6) for d in dice]
                print("You rolled:", dice)
        else:
            choice = input("Do you want to roll again? y or n :")
            if choice.lower() == 'n':
                total_score += sum(dice)
                print("Total SCore for this turn is:", total_score)
                return total_score
            else: 
                dice = roll_dice()
                print("You rolled:", dice)
def main():
    print("Welcome to Tuple Out Dice Game!")
    num_players = int(input("Enter the number of players: "))
    scores = [0] * num_players

# insert a Data Frame in order to save scores
scores_df = pd.DataFrame(index= range(1,num_players + 1), columns=['Turn', 'Score'])
    
while  max(scores_df['Score']) < 50:
    for player in range(1, num_players + 1):
        print(f"\nPlayer {player}'s turn:")
        score = play_turn()
        scores_df.loc[player, 'Turn'] += 1
        scores_df.loc[player, 'Score'] += score
        print("Current Scores: \n", scores)
        if scores_df.loc[player,'Score'] >= 50:
            print(f"Player {player} wins!")
            break

# Plot the scores of each of the players
for player in range (1, num_players + 1):
    plt.plot(scores_df.loc[player, 'Turn'], scores_df.loc[player, 'Score'], label=f'Player {player}')

plt.xlabel('Turn')
plt.ylabel('Score')
plt.title('Game Progression')
plt.legend()
plt.show()

if __name__ == "__main__":
    main()

