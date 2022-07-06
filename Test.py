from Question import Question
question_prompt = [
    "What is the first color in Ghana flag? \n(a)black \n(b)green \n(c)red\n\n",
    "Who is regarded as the father of computers? \n(a)Charles Babbage \n(b)Ada Lovelace \n(c)Alan Turing\n\n",
    "Which programming language is mostly used for Data Science? \n(a)C++ \n(b)Javascript \n(c)R\n\n",
    "Which programming language is mostly used for Backend Development? \n(a)C# \n(b)Php \n(c)Julia\n\n"
]

questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "a"),
    Question(question_prompt[2], "c"),
    Question(question_prompt[3], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1 
    print(f"You got {score} / {len(questions)}")

run_test(questions)