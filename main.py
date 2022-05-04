print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Adventure Island.")
print("Your mission is to find the hidden treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

Mission1 = input('You are at a crossroad. Where do you want to go? Type "left" or "right":\n').lower()
if Mission1 == "left":
  Mission2 = input('You\'ve come to a lake.There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
  if Mission2 == "wait":
    Mission3 = input("You arrive at the island unharmed. Hurray! Now, here is a cave with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
    if Mission3 == "red":
      print("It's a room full of fire. Game Over.")
      print(r'''   


    ,.   (   .      )        .      "
   ("     )  )'     ,'        )  . (`     '`
 .; )  ' (( (" )    ;(,     ((  (  ;)  "  )"
 _"., ,._'_.,)_(..,( . )_  _' )_') (. _..( '..jb
            

''')           
             
      
    elif Mission3 == "yellow":
      print("You found the treasure chest! You Win!")
      
      print(r'''       _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
''')
      
        
    elif Mission3 == "blue":
      print("You enter a room of beasts! Game Over.")
      print(r'''

       {}           {}
         \  _---_  /
          \/     \/
           |() ()|
            \ + /
ejm 96     / HHH  \
          /  \_/   \
        {}          {}

   ''')  


      
    else:
      print("You chose a door that doesn't exist. Game Over.")
      print(r'''

      
            __________
           |  __  __  |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |  __  __()|
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
ejm        |__________| ''')

    

            
  else:
    print("You get attacked by a shark! Game Over!!")
    print(r''' 



                     ^`.                     o
     ^_              \  \                  o  o
     \ \             {   \                 o
     {  \           /     `~~~--__
     {   \___----~~'              `~~-_     ______          _____
      \                         /// a  `~._(_||___)________/___
      / /~~~~-, ,__.    ,      ///  __,,,,)      o  ______/    \
      \/      \/    `~~~;   ,---~~-_`~= \ \------o-'            \
                       /   /            / /
                      '._.'           _/_/
                                      ';|\     ''')
    

else:
  print("You get attacked by an angry bird! Game Over!!")
  
  print(r'''   

    
,_.                                                          ,_.
'\cXX.==- __                                        __ -==,XXv/`
    ~=_X7~ ,/~!g=-,_.                      ,_.-=s!~L. ~TX_=~
       ~=c. = /- T--e'T|=v._  ....   _,v=!7`z--\ -\ = ,v=~
          ~=c` ./ ,-`,/ /i/Z\/~~~~\/Z\i\ \.'-. \, 'v=~
             ~\s,/ ,/ ,/ Y]`/ @/\@ \'[Y \. \. \.g/~
                '`Yc.v`,/Vs)-  \/  -(sV\.'c,v+'`
                     ~~]mZczTV '` VTevZm[~~
                  ,=-T|--2Y [      ] Y2--!T-=.
                  'i`_ -|-'i!      !i`-!- _'i`
                    '-s|.cf ,!]\/[!. 1v,!g-`
                        ~Y/v/vv..vv\v\Y~
                         ^            ^ ''')
       




# choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
# if choice1 == "left":
#   choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
#   if choice2 == "wait":
#     choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
#     if choice3 == "red":
#       print("It's a room full of fire. Game Over.")
#     elif choice3 == "yellow":
#       print("You found the treasure! You Win!")
#     elif choice3 == "blue":
#       print("You enter a room of beasts. Game Over.")
#     else:
#       print("You chose a door that doesn't exist. Game Over.")
# #   else:
#     print("You get attacked by an angry trout. Game Over.")
# else:
#   print("You fell into a hole. Game Over.")
 # print(r'''    ''')