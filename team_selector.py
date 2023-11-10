import random

players = ['Martin', 'Craig', 'Sue',
           'Claire', 'Dave', 'Alice',
           'Luciana', 'Harry', 'Jack',
           'Rose', 'Lexi', 'Maria',
           'Thomas', 'James', 'William',
           'Ada', 'Grace', 'Jean',
           'Marissa', 'Alan']

print('Welcome to the team/player allocation tool!')

while True:

  random.shuffle(players)

  typeofsport = input('\nIs it a team or individual sport? \
                        \nType t for team or i for individual: ')

  # Team Sport  
  if typeofsport == 't':
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
  # Invividual Sport
  else:
    # Go through the list of players, incrementing by 2 each time
    for i in range(0, 20, 2):
      print(players[i] + ' vs ' + players[i+1])
      # Pick a random player from this set of two players
      start = random.randrange(i, i+2)
      print(players[start] + ' starts.')
    
  response = input('\nPick teams again? (Type y or n): ')
  if response == 'n':
    break