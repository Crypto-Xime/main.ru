                                    # History: rivalry between two teams
                                     # - Code Masters and Data Wizards.

def game_results(first_team: str, first_score: int, second_team: str, second_score: int):
    """
    Determine the result of a game between two teams.

    :param first_team: Name of the first team
    :param first_score: Score of the first team
    :param second_team: Name of the second team
    :param second_score: Score of the second team
    :return: The result of the game, formatted string
    """

# Determine the game result

    if first_score > second_score:
        challenge_result = f"Victory for the {first_team} team!"
    elif first_score < second_score:
        challenge_result = f"Victory for the {second_team} team!"
    else:
        challenge_result = "Draw!"

    return challenge_result

# Input data
team1_name = "Code Master"
team2_name = "Data Wizards"
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

# Get the game results from the Function in use

challenge_result = game_results(team1_name, score_1, team2_name, score_2)

# Formatting using % operator
print("Using % formatting:")

# 1. Number of members in the first team
print("There are %d participants in the Code Masters team!" % team1_num)

# 1.1 Number of members in the second team
print("There are %d participants in the Data Wizards team!" % team2_num)

# 2. Total participants in both teams
print("Total today in the teams of participants: % and %d!" % (team1_num, team2_num))

# Formatting using format()
print("\nUsing format() formatting:")

# 3 Number of problems solved by team 1
print("The Code Masters team solved {} problems!".format(score_1))

# 3.1 Number of problems solved by team 2
print("The Data Wizards team solved {} problems!".format(score_2))

# 4 Time for which team 1 solve the problem
print("The Code Masters team solve problems in {} seconds!".format(team1_time))

# 4.1 Time for Which team 2 solve the problem
print("The Data Wizards team solve problems in {} seconds!".format(team2_time))

# Formatting using f-strings
print("\nUsing f-strings formatting")

# 5. Number of solved problems by both teams
print(f"Teams solved {score_1} and {score_2} problems")

# 6. Competition Results Shown
print(f"Battle Results: {challenge_result}")

# 7. Total number of tasks and average solution time taken
print(f"Today {tasks_total} problems were solved by the teams, on average it took {time_avg} seconds"
      f"\nper problem! Congratulations for the effort!")