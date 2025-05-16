# #KBC

name = input("Enter your name: ")
print("Hello, " + name + "!")
print("Welcome to Kaun Banega Crorepati!")

ques = ["What is the capital of India?", 
        "Who is the father of our nation?",
        "Who is the prime minister of India?", 
        "Who is the president of India?"]

opts = [["a)Delhi", "b)Mumbai", "c)Kolkata", "d)Chennai"],
        ["a)Mahatma Gandhi", "b)Jawaharlal Nehru", "c)Subhash Chandra Bose", "d)Bhagat Singh"],
        ["a)Narendra Modi", "b)Rahul Gandhi", "c)Amit Shah", "d)Manmohan Singh"],
        ["a)Ram Nath Kovind", "b)Pranab Mukherjee", "c)APJ Abdul Kalam", "d)Rajendra Prasad"]]

for i in range(len(ques)):
    print(ques[i])
    for opt in opts[i]:
        print(opt)
    ans = input("Enter your answer: ")
    if ans == "a":
        print("Correct answer!")
        print("You have won Rs. 1000")
    else:
        print("Incorrect answer")
        break


