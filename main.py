#
import random
from traceback import print_tb
print('************      Welcome to Rock-Paper-Scissors game, enjoy.     **********')
options = ['R', 'P', 'S']

playerpick = input('Pick "R","S" or "P" to play__').capitalize()


while playerpick in options:
    cpupick = random.choice(options)
    if cpupick == playerpick:
        print('Its a tie, less contunie')
        playerpick = input('Pick "R","S" or "P" to play...').capitalize()
        continue
    elif (cpupick == 'R' and playerpick == 'S') or (cpupick == 'S' and playerpick == 'P'):
        print('Player ' + '(' + playerpick +')' + ':' + 'CPU ' + '(' + cpupick + ')')
        print('Victor to CPU')
        break
    elif cpupick == 'P' and playerpick == 'R':
        print('Player ' + '(' + playerpick +')' + ':' + 'CPU ' + '(' + cpupick + ')')
        print('Victor to CPU')
        break
    elif (playerpick == 'R' and cpupick == 'S') or (playerpick == 'S' and cpupick == 'P'):
        print('Player '+ '(' + playerpick + ')' +':' + 'CPU ' + '(' + cpupick + ')')
        print('Victor to Player')
        break
    elif playerpick == 'P' and cpupick == 'R':
        print('Player '+ '(' + playerpick + ')' +':' + 'CPU ' + '(' + cpupick + ')')
        print('Victor to Player')
        break
else:
    while playerpick not in options:
        print('Error! Please try again')
        playerpick = input('Pick "R","S" or "P" to play...').capitalize()

            

