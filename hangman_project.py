import random  
import hangman_stages
from replit import clear
print(hangman_stages.logo)
choosen_word=random.choice(hangman_stages.word_list)
print(choosen_word)
word_length=len(choosen_word)
display=[]
for _ in range(word_length):
    display.append("_")
print(display)
end_of_game=False
lives=6
while not end_of_game:
            guess=input("guess the letter\n").lower()
            clear ()
            if guess in display:
                print(f"You already guessed this letter '{guess}'")
            for position in range(word_length):
                letter=choosen_word[position]
                if letter==guess:
                    display[position]= letter
            if guess not in choosen_word:
                print(f"you guessd {guess},that's not in the word. you loose a life ")
                lives-=1
                if lives==0:
                    end_of_game=True
                    print("you are out of lives\n YOU LOOSE")
            print(f"{' '.join(display)}")
            end_of_game=True
                print("YOU WIN")
            print(hangman_stages.stages[lives])
