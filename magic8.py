import random

name = "User"
question = input("Ask a question: (Please do not forget to put '?' after your question) ")
answer = ""
random_number = random.randint(1, 9)

if random_number == 1:
    answer = "Yes - definitely."
elif random_number == 2:
    answer = "It is decidedly so."
elif random_number == 3:
    answer = "Without a doubt."
elif random_number == 4:
    answer = "Reply hazy, try again."
elif random_number == 5:
    answer = "Ask again later."
elif random_number == 6:
    answer = "Better not to tell you know."
elif random_number == 7:
    answer = "My sources say no."
elif random_number == 8:
    answer = "Outlook not so good."
elif random_number == 9:
    answer = "Very doubtful."
else:
    answer = "Error."

if len(question) == 0 or "?" not in question:
    print("The Magic 8-Ball can not provide a fortune unless you ask it something.")
else:
    print("Magic 8-Ball's answer: " + answer)
