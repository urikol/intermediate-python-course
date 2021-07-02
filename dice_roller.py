import random

def main():

  f = open("Count.txt")
  count = f.readlines()
  f.close()

  dice_rolls=int(input('How many dice would you like to roll? '))
  dice_size = int(input('How many sides are the dice? '))
  team_num=int(input('How many teams are playing? '))


  dice_sum = [0]*team_num

  teams=[]
  for i in range(0,team_num):
      teams.append(input('What is the name of the {} team? '.format(count[i].strip())))

  for j in range(0,team_num):
      input(f'{teams[j]}, roll the dice by pressing Enter')
      for i in range(0,dice_rolls):
          roll = random.randint(1,dice_size)
          dice_sum[j] = dice_sum[j] + roll
          if roll == 1:
            print(f'You rolled a {roll}! Critical Fail')
          elif roll == dice_size:
            print(f'You rolled a {roll}! Critical Success!')
          else:
            print(f'You rolled a {roll}')
      print(f'You have rolled a total of {dice_sum[j]}')

  winner=[0]
  win_num=1
  winner_score=dice_sum[0]

  for j in range(1,team_num):
      if dice_sum[j] > winner_score:
        winner=[j]
        winner_score=dice_sum[j]
      elif dice_sum[j] == winner_score:
        winner.append(j)
        win_num+=1


  if win_num == 1:
      print(f'The winner is {teams[winner[0]]}!')
  else:
      print(f'The winners are:')
      for j in range(0,win_num):
          print(f'{teams[winner[j]]}')

if __name__== "__main__":
  main()
