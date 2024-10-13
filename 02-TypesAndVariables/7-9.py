#
# In many games, the numbers one and six on dice have special meaning. Write a program that displays the number of dice rolled and the value True if the number rolled is 1 or 6. Sample result:
# Dice rolled: 4
# Special number (1 or 6): False
#
import random
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
dice3 = random.randint(1,6)
dice4 = random.randint(1,6)
special = dice1 == 1 or dice1 == 6 or dice2 == 1 or dice2 == 6 or dice3 == 1 or dice3 == 6 or dice4 == 1 or dice4 == 6
print(f'Dice 1: {dice1}\nDice 2: {dice2}\nDice 3: {dice3}\nDice 4: {dice4}\nSpecial: {special}')
