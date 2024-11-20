def ask_question(question, options, correct_answer, file):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    while True:
        try:
            answer = int(input("Your answer (1-4): "))
            if 1 <= answer <= 4:
                break
            else:
                print("Choose a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 4.")
    
    if options[answer - 1].lower() == correct_answer.lower():
        file.write(f"Question: {question}\nYour Answer: {options[answer - 1]} (Correct)\n\n")
        return 1
    else:
        file.write(f"Question: {question}\nYour Answer: {options[answer - 1]} (Incorrect)\n\n")
        return 0

def quiz():
    with open("quiz_results.txt", "a") as file:
        score = 0
        questions = [
            ("What is the keyword used to define a function in Python?", ["def", "func", "function", "lambda"], "def"),
            ("Which function is used to get the length of a list?", ["length", "len", "size", "count"], "len"),
            ("How do you start a comment in Python?", ["//", "#", "/*", "--"], "#"),
            ("Which of these is the correct syntax to create a list?", ["[]", "{}", "()", "<>"], "[]"),
            ("Which function is used to read input from the user in Python?", ["input", "read", "get", "ask"], "input")
        ]
        
        for question, options, correct_answer in questions:
            score += ask_question(question, options, correct_answer, file)
        
        file.write(f"Final Score: {score}/{len(questions)}\n")
        file.write("="*30 + "\n")
        print(f"\nYour final score is: {score}/{len(questions)}")
        print("Your answers have been saved to 'quiz_results.txt'.")

quiz()
