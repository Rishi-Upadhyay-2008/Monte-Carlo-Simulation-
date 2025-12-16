import random
import matplotlib
import matplotlib.pyplot as plt


# Def rolldice is there basis and is the main thing the bettor is well betting on 


def rollDice():
  roll = random.randint(1,100) # As shown when rolled it picks a number between 1 and 100
  if roll==100:
    #print (roll,"You rolled a 100, You lose") << For debugging purposes
    return False 
  elif roll<=50:
    #print (roll,"You rolled between 1-5, You lose") << same applies here
    return False
  elif 100>roll>50:
    #print (roll,"You rolled between 51-99, You win") << and here 
    return True


def bettor_1(capital, Amount_Wagered, Wager_Count):
  value = capital
  wager = Amount_Wagered

  Wx = []
  Vy = []

  currentWager = 1

  while currentWager <= Wager_Count:
    if rollDice():
      value += wager
      Wx.append(currentWager)
      Vy.append(value)
    else :
     value -= wager
     Wx.append(currentWager)
     Vy.append(value)

    currentWager += 1

  if value <= 0:
    value = 'brokie',value
  #print ("Capital Earned :", value) << once again
  plt.plot(Wx,Vy)

x = 0

while x < 1000:
  bettor_1(100000,1000,100)
  x+=1


plt.ylabel('Capital Earned')
plt.xlabel('Wager Count')
plt.show()
