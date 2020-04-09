def validateNumber(msg, min, max, minMsg, maxMsg):
    number = int(input(msg + ": "))
    while True:
        if number < min:
            print(minMsg)
            number = int(input(msg + ": "))
        elif number > max:
            print(maxMsg)
            number = int(input(msg + ": "))            
        else:
            return number

def printUserStatistics():
    gradesCount = len(studentGrades)
    gradesAvg = sum(studentGrades)/gradesCount
    print(f"{studentName}, you have {gradesCount} grades and your average is {gradesAvg}")


print("Welcome to the Grade Sorter App\n")

studentName = input("Type your name: ").strip().capitalize()
print(f"Hello, {studentName}!\n")
studentGrades = []
gradesCount = validateNumber("How many grades do you have", 
    1, 
    100, 
    "You have to have at least 1", 
    "Noone has more than 100") + 1



for i in range(1, gradesCount):
    
    if i == 1:
        ending = "st"
    elif i == 2:
        ending = "nd"
    elif i == 3:
        ending = "rd"
    else:
        ending = "th"
    



    studentGrades.append(validateNumber(
        f"What is your {i}'{ending} grade (0-100)", 
        0, 
        100, 
        "You can not do less than 0!", 
        "Noone has more than 100!")
    )
    

print("\nYour grades are", studentGrades)
studentGrades.sort(reverse = True)

print("\nYour grades from highest to lowest are:", studentGrades)
printUserStatistics()



print("\n")
gradesToDelete = validateNumber(
    "How many bad grades do you want to delete", 
    0, 
    gradesCount, 
    "You can not do less than 0!", 
    "You don't have this many grades"
)

for i in range(0, gradesToDelete):
    print(studentGrades.pop(), "deleted")

print("\nYour grades are now:", studentGrades)
printUserStatistics()
print("Well done", studentName + "!!")



# def repeatUserInput(number, min, max, minMsg, maxMsg):
#     while userInput = validateNumber(number,, min, max, minMsg, maxMsg)
#         number = input()
#     return userInput




