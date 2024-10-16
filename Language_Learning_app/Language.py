import random

french_words = {
    "bonjour": "Hello",
    "merci": "Thank you",
    "au revoir": "Goodbye",
    "oui": "Yes",
    "non": "No",
    "s'il vous plaît": "Please",
    "excusez-moi": "Excuse me",
    "je suis désolé": "I am sorry",
    "comment ça va?": "How are you?",
    "ça va bien": "I am fine",
    "bonsoir": "Good evening",
    "bonne nuit": "Good night",
    "je t'aime": "I love you",
    "à bientôt": "See you soon",
    "pardon": "Pardon",
    "où": "Where",
    "quoi": "What",
    "qui": "Who",
    "pourquoi": "Why",
    "combien": "How much",
    "je comprends": "I understand",
    "je ne comprends pas": "I don’t understand",
    "parlez-vous anglais?": "Do you speak English?",
    "je m'appelle": "My name is",
    "quel âge as-tu?": "How old are you?",
    "j'ai faim": "I am hungry",
    "j'ai soif": "I am thirsty",
    "bien sûr": "Of course",
    "désolé": "Sorry",
    "bienvenue": "Welcome",
    "heureux": "Happy",
    "triste": "Sad",
    "fatigué": "Tired",
    "froid": "Cold",
    "chaud": "Hot",
    "j'ai besoin d'aide": "I need help",
    "où est...?": "Where is...?",
    "pouvez-vous m'aider?": "Can you help me?",
    "quel est votre nom?": "What is your name?",
    "je vous en prie": "You're welcome",
    "à demain": "See you tomorrow",
    "bonne journée": "Have a nice day",
    "je vais bien": "I am doing well",
    "je suis perdu": "I am lost",
    "peux-tu répéter?": "Can you repeat?",
    "c'est cher": "It's expensive",
    "c'est bon": "It's good",
    "je veux": "I want",
    "je ne veux pas": "I don’t want",
    "j'aime": "I like",
    "je n'aime pas": "I don't like",
    "comment": "How",
    "quand": "When",
    "ici": "Here",
    "là-bas": "There",
    "aujourd'hui": "Today",
    "demain": "Tomorrow",
    "hier": "Yesterday",
    "maintenant": "Now",
    "bientôt": "Soon",
    "jamais": "Never",
    "toujours": "Always",
    "souvent": "Often",
    "parfois": "Sometimes",
    "rarement": "Rarely",
    "beaucoup": "A lot",
    "un peu": "A little",
    "tout": "Everything",
    "rien": "Nothing",
    "tout le monde": "Everyone",
    "personne": "No one",
    "maison": "House",
    "voiture": "Car",
    "travail": "Work",
    "école": "School",
    "famille": "Family",
    "ami": "Friend",
    "enfant": "Child",
    "homme": "Man",
    "femme": "Woman",
    "garçon": "Boy",
    "fille": "Girl",
    "chien": "Dog",
    "chat": "Cat",
    "livre": "Book",
    "argent": "Money",
    "musique": "Music",
    "film": "Movie",
    "sport": "Sport",
    "vacances": "Vacation",
    "repas": "Meal",
    "boisson": "Drink",
    "pain": "Bread",
    "fromage": "Cheese",
    "eau": "Water",
    "café": "Coffee",
    "thé": "Tea",
    "vin": "Wine",
    "bière": "Beer",
    "fruit": "Fruit",
    "légume": "Vegetable",
    "sucre": "Sugar",
    "sel": "Salt",
    "poivre": "Pepper",
    "viande": "Meat",
    "poisson": "Fish"
}


def quiz_user(words):
    score = 0
    total_questions = len(words)
    
    shuffled_words = list(words.items())
    random.shuffle(shuffled_words)

    for french, english in shuffled_words:
        user_answer = input(f"What is the English word for '{french}'? ").lower()
        if user_answer == 'q' or user_answer == 'quit':
            print("You chose to quit the quiz.")
            break

        if user_answer == english.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is '{english}'.")
            print("You want to quit then press q.")
    
    print(f"\nYour final score is {score}/{total_questions}")

def main():
    print("Welcome to the French-English Dictionary Quiz!")
    input("Press Enter to start the quiz...")

    quiz_user(french_words)

if __name__ == "__main__":
    main()
