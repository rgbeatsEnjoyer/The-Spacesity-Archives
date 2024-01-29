# Questionair v1.1 By Spacesity

# Questions

score = 0

print("How many legs does a cat have? A) 2 B)4 C)9")
question1=input('Answer:')
if question1.strip().lower() == "b":
    print("Answer is correct")
    score = score + 1
else:
    print("Answer is A")

print("How many legs does a human have? A)2 B)1 C)1")
question2=input('Answer:')
if question2.strip().lower() == "a":
    print("Answer is correct")
    score = score + 1
else:
    print("Answer is C")

print("Who was president of the USA in 2018? A)Obama B)Trump C)Washington")
question3=input('Answer:')
if question3.strip().lower() == "b":
    print("Answer is correct")
    score = score + 1
else:
    print("Answer is B")

# Score total

print("Score:",score)

# Questionair v1.2 By Spacesity

# Question stuff code thingy

questiontable = {'Question1': "How many legs does a cat have? A) 2 B)4 C)9",
                 'Question2': "How many legs does a human have? A)2 B)1 C)1",
                 'Question3': "Who was president of the USA in 2018? A)Obama B)Trump C)Washington"}

answertable = ['b','a','b']


for x in range(1,4):
    print(questiontable['Question' + str(x)])
    question=input('Answer:')
    if question.strip().lower() == answertable[x - 1]:
        print("Answer is correct")
        score = score + 1
    else:
        print("Incorrect")

# Score total

print("Score:",score)





