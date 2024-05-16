import random
import pandas as pd
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
    # A dictionary to hold player scores
    all_scores = {"Player" : [num for num in range(1, num_players + 1)],
                  "Turn" : [0] * num_players,
                  "Score" : [0] * num_players }
    current_turn = 0 
    while max(all_scores['Score']) < 50:
        current_turn += 1
        for player in range(1, num_players + 1):
            print(f"\nPlayer {player}'s turn:")
            turn_score = play_turn()
            all_scores['Player'].append(player)
            all_scores['Turn'].append(current_turn)
            cumulative_score = all_scores['Score'][-1 * num_players] + turn_score
            all_scores['Score'].append(cumulative_score)
             #print("Current Scores: \n", all_scores)
            if cumulative_score >= 50:
                print(f"Player {player} wins!")
                break
    scores_df = pd.DataFrame(all_scores)

# Plot the scores of each of the players
    for player in range (1, num_players + 1):
        plt.plot(scores_df.loc[scores_df["Player"] == player,'Turn'],
                 scores_df.loc[scores_df["Player"] == player,'Score'])
    plt.xlabel('Turn')
    plt.ylabel('Score')
    plt.title('Game Progression')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
