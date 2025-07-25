# ask the user to choose its movment ('Paper','Rock','Scissor')
# the pc will choose its movment randomly form the same list 
#if the user movment eqaul to pc " it is a tie!"
#if the user movment and pc as follow : (user == 'Paper' and pc =='Rock' )(user == 'Scissor' and pc =='Paper' )(user == 'Rock' and pc =='Scissor' ) : the user is the winner 
# else the above condition user lose ! 

import random

option = ['Paper','Rock','Scissor']
user = input ("Welcome to Paper Rock Scissor game\nTo start the game, Please insert( Paper or Rock or Scissor ) :\n  ").capitalize()
pc = random.choice(option)

if user not in option : 
    print("Invalid input. Please choose one of the following: Paper - Rock - Scissor")
else :
    print( f" The user choose : {user}" )
print( f" The PC choose : {pc}" )

if user == pc : 
    print ("It's a Tie ")

elif (user == 'Paper' and pc =='Rock') or \
    (user == 'Scissor' and pc =='Paper') or \
    (user == 'Rock' and pc =='Scissor') :
   
   print (" You win ")

else : 
    print ( " the pc won | you lose ") 
