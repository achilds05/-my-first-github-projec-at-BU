import random
responses = [
    "Cool!",
    "Nice!",
    "Wow, great!"
]

def ask_question(question):
    answer = input(question + " ")
    print(random.choice(responses))
    print()  # For spacing between question

questions = [
    "What's your favoritehobby?",
    # Example questiongood
    "What's your name?", 
     "When's your birthday?", 
     "How has your day been?",

]

def icebreaker():
    print("Let's break the ice! I'll ask you two random questions:")
    selected_questions= random.sample(questions, 2)  # Randomly select 2 question
    for question in selected_questions:
        ask_question(question)

icebreaker()
