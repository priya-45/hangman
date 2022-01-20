import random
print("play Hangman  Game!")
print("Lets Start Now!")
word_list=["priya","sonam","rakhi","laxmi","gudia","shivani","kirti","kiran","ganeskh","kumar"]
chose_word=random.choice(word_list)
word_length=len(chose_word)
display=[]
for _ in range(word_length):
    display+="_"
print(display)
lives=5
game_over=False
while not game_over:
    guess=input("enter guess:")
    for i in range(word_length):
        letter=chose_word[i]
        if letter==guess:
            display[i]=letter
    if guess not in chose_word:
        lives-=1
        if lives==4:
            print("only",lives,"chance")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
        if lives==3:
            print("only",lives,"chance")
            print("_____________")
            print("|")
            print("|")
            print("|")
            print("|")
            print("|")
        if lives==2:
            print("only",lives,"chance")
            print("_____________")
            print("|","       ","|")
            print("|","       ","|")  
            print("|""       ","/O\\")
            print("|")
            print("|")
        if lives==1:
            print("only",lives,"chance")
            print("_____________")
            print("|","       ","|")
            print("|","       ","|")  
            print("|""       ","/O\\")
            print("|""        ","|")
            print("|""        ","|")
    print(display)
    if lives==0:
        # game_over=True
        print("your chance is finished")
        print("oops!you are looser")
    # print(display)
    if "_"not in display:
        # game_over=True
        print("wow!you are winner")
    