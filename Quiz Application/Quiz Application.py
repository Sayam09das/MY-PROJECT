import requests

class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def fetch_questions(self):
        # Fetch questions from Open Trivia Database API
        url = "https://opentdb.com/api.php?amount=10&difficulty=easy&type=multiple"
        response = requests.get(url)
        data = response.json()
        
        if data['response_code'] == 0:
            self.questions = data['results']
        else:
            print("Error fetching questions from the API.")
            exit()

    def start_quiz(self):
        print("Welcome to the Quiz! Let's test your knowledge.")
        for idx, question in enumerate(self.questions, 1):
            print(f"\nQuestion {idx}: {question['question']}")
            options = question['incorrect_answers'] + [question['correct_answer']]
            options.sort()  

            for i, option in enumerate(options, 1):
                print(f"{chr(64 + i)}) {option}") 

            user_answer = input("Your answer (A/B/C/D): ").upper()
            correct_answer = question['correct_answer']
            if user_answer == chr(64 + options.index(correct_answer) + 1):
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is {correct_answer}.")

        self.display_score()

    def display_score(self):
        print(f"\nYour final score is: {self.score}/{len(self.questions)}")
        if self.score == len(self.questions):
            print("Excellent! You got all questions right!")
        elif self.score >= len(self.questions) // 2:
            print("Good job! You passed the quiz!")
        else:
            print("Better luck next time!")

if __name__ == "__main__":
    quiz = Quiz()
    quiz.fetch_questions()
    quiz.start_quiz()
