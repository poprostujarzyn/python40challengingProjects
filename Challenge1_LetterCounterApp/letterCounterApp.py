# def countLetterOccurances(letter, message):

#     occurances = 0

#     for letterInMessage in message:
#         if letter == letterInMessage:
#             occurances += 1

#     return occurances


print("Welcome to the Letter Counter App\n")


userName = input("What is your name? ").strip().capitalize()
print("Hello " + userName + "!")
print('I will count the number of times that a specific letter occurs in a message.\n')
userMessage = input("Please enter a message: ").lower()
theLetter = input("Which letter would you like to count the occurrences of: ").lower()

# print(userName + ", your message has ", countLetterOccurances(theLetter, userMessage), theLetter + "'s in it")
print(userName + ", your message has ", userMessage.count(theLetter), theLetter + "'s in it")

      

