
import random
stages=["""
   _________
    |/        
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    """,

"""
   _________       
    |/   |              
    |   (_)
    |                         
    |                       
    |                         
    |                          
    |___                       
    HA""",

"""
   ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |    |                    
    |                           
    |                            
    |___                    
    HAN""",

"""
   _________              
    |/   |                     
    |   (_)                     
    |   /|\                    
    |    |                       
    |                             
    |                            
    |___                          
    HANGM""",


"""
   ________
    |/   |     
    |   (_)    
    |   /|\           
    |    |        
    |   / \        
    |               
    |___           
"""]
end_of_game=False
word_list=["vijay","simha","reddy"]
choose_word=random.choice(word_list).upper()
lives=5
print(f'pssst,the solution is {choose_word}.')

display=[]
for _ in range(len(choose_word)):
    display+="_"
print(display)

while not end_of_game:
    guess=input("Guess a letter:").upper()
    for position in range(len(choose_word)):
        letter=choose_word[position]
        if letter == guess:
            display[position]=letter
    if guess not in choose_word:
        lives-=1
        print(stages[4-lives])
        if lives==0:
          end_of_game=True
          print("You lose")
          print(f"Answer is {choose_word}")

    print(f"{''.join(display)}")
    if "_" not in display:
      end_of_game=True
      print("You Win")
