import random
from models import FlashCard
from seed import FlashCard 

def add_card():
    russian_word = input("Enter the Russian word: ")
    english_word = input("Enter the English word: ")
    hint = input("Enter a hint: ")
    card = FlashCard(russian_word=russian_word, english_word=english_word, hint=hint)
    card.save()
    print("Card added successfully!")

def study(num_cards):
    flashcards = list(FlashCard.select())
    random.shuffle(flashcards)
    
    correct = 0 
    incorrect = 0 
    
    for i in range(num_cards):
        flashcard = flashcards[i]
        front = flashcard.russian_word
        back = flashcard.english_word
        hint = flashcard.hint
       
        print(f"\nCard {i + 1} of {num_cards}:")
        print(f"Front: {front}")
        
        show_hint = input("Would you like a hint? (yes/no) ")
        if show_hint.lower() == "yes":  
            if hint is not None:
                print(f"Hint: {hint}") 
            else:
                print("Sorry, no hint available for this card.")
        
        
        user_input = input("Back: ")
        
        if user_input == back:
            print("Correct!")
            correct += 1
        else:
            print(f"Incorrect. The correct answer is '{back}'.")
            incorrect += 1
        
        flashcard.save()
      
while True:
    print("\nMenu:")
    print("1. Add new card")
    print("2. Start practice or study session")
    print("3. Quit")
    choice = input("Enter your choice (1, 2, or 3): ")
    if choice == "1":
         add_card()
    elif choice == "2":
        num_cards = int(input("Enter the number of flash cards you would like to review: "))
        study(num_cards)
    elif choice == "3":
        print("Thanks for studying the russian language flash cards!")
        break
    else:
        print("That is not a valid option. Please select a valid option (1, 2, or 3)")