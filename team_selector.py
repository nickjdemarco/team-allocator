import random

players = ['Martin', 'Craig', 'Sue',
           'Claire', 'Dave', 'Alice',
           'Luciana', 'Harry', 'Jack',
           'Rose', 'Lexi', 'Maria',
           'Thomas', 'James', 'William',
           'Ada', 'Grace', 'Jean',
           'Marissa', 'Alan']

print('Welcome to the team allocation tool!')

while True:

    random.shuffle(players)

    # Form 1st Team
    team1 = players[:len(players)//2]

    print('Team 1 Captain: ' + random.choice(team1))

    print('Team 1:')
    for player in team1:
        print(player)

    # Form 2nd Team
    team2 = players[len(players)//2:]

    print('\nTeam 2 Captain: ' + random.choice(team2))

    print('Team 2:')
    for player in team2:
        print(player)

    response = input('\nPick teams again? (Type y or n): ')
    if response == 'n':
      break