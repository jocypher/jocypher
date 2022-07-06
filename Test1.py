from Exams import question
test_prompt = [
    "1.In which continent are chile and Brazil?\n(a)North America\n(b)South America\n(c)Asia\n(d)Europe\n\n",
    "2.What measurement scale is used to determine wind speed?\n(a)Beaufort scale\n(b)Richter scale\n(c)Synoptic scale\n(d)Gusting scale\n\n",
    "3.In which city were the 1992 summer olympics held?\n(a)Atlanta\n(b)Barcelona\n(c)Seoul\n(d)Accra\n\n",
    "4.How many sides does a Dodecahedron have?\n(a)12\n(b)24\n(c)14\n(d)20\n\n",
    "5.The Statue of Liberty was a gift to the United States from which European country?\n(a)France\n(b)Spain\n(c)Belgium\n(d)Germany\n\n",
    "6.What other country, besides the US, uses the US dollar as its official currency?\n(a)Ecuador\n(b)Canada\n(c)Mexico\n(d)United Kingdom\n\n",
    "7.The human body is made up of approximately how much water?\n(a)40%\n(b)70%\n(c)50%\n(d)60%\n\n",
    "8.What is the world's fastest species of bird?\n(a)Golden Bird\n(b)Peregrine Falcon\n(c)Frigate Bird\n(d)Penguin\n\n",
    "9.Which of the following languages has the longest alphabet?\n(a)Greek\n(b)Russia\n(c)Arabic\n(d)French\n\n",
    "10.What spirit is used in making a Tom collins?\n(a)Vodka\n(b)Rum\n(c)Gin\n(d)Club\n\n"
]

tests =[
    question(test_prompt[0], "b"),
    question(test_prompt[1], "a"),
    question(test_prompt[2], "b"),
    question(test_prompt[3], "a"),
    question(test_prompt[4], "a"),
    question(test_prompt[5], "b"),
    question(test_prompt[6], "b"),
    question(test_prompt[7], "b"),
    question(test_prompt[8], "b"),
    question(test_prompt[9], "c")
    
] 

def run_test(tests):
    user_name = input("Please Input your name: ")
    score = 0
    for test in tests:
        answer= input(test.prompt)
        if answer == test.answer:
            score += 1
    if score == 10:
        print(f"Congratulations {user_name} you had a perfect score.")
    elif score <=5 :
        print(f"Oops your score was {score}/{len(tests)} {user_name} too bad try again")
    else:
        print(f"Your score was {score}/{len(tests)} {user_name} ")

run_test(tests)
     