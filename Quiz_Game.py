print(" ******* WELLCOME TO COMPUTER QUIZ !! *******\n")
play = input(" Do you want to play? yes or no : ")
if play.lower() == "yes":
    print(" \nOkay Let's begin the game.\n ")
elif play.lower() == "no":
    print("Thank You !! Have a great day ahead...")
    quit()
else:
    print("Invalid Entery")
    quit()
score = 0
answer =input("DOS stands for _______?	?\n")
if answer.lower() == "disk operating system":
    print("Correct Answer")
    score +=1
else:
    print("Sorry! wrong answer.")

answer =input("In a computer, most processing takes place in _______? \n")
if answer.lower() == "cpu":
    print("Correct Answer")
    score +=1
else:
    print("Sorry! wrong answer.")

answer =input("Which command is used to select the whole document ?\n")
if answer.lower() == "ctrl+a":
    print("Correct Answer")
    score +=1
else:
    print("Sorry! wrong answer.")

answer =input("AI stands for _______?\n")
if answer.lower() == "artificial intelligence":
    print("Correct Answer")
    score +=1

else:
    print("Sorry! wrong answer.")

answer =input("Unwanted repetitious messages, such as unsolicited bulk e-mail is known as _______?	\n")
if answer.lower() == "spam":
    print("Correct Answer")
    score +=1
else:
    print("Sorry! wrong answer.")

answer =input("Which is most common tool used to restrict access to computer system?\n")
if answer.lower() == "password" :
    print("Correct Answer")
    score +=1
else:
    print("Sorry! wrong answer.")

answer =input("What kind of memory is both static and non-volatile?	\n")
if answer.lower() == "rom":
    print("Correct Answer")
    score +=1
else:
    print("Sorry! wrong answer.")

answer =input("Full form of LAN?\n")
if answer.lower() == "local area network":
    print("Correct Answer")
    score +=1
else:
    print("Sorry! wrong answer.")

answer =input("Where are the CPU and memory located ?\n")
if answer.lower() == "motherboard":
    print("Correct Answer")
    score +=1
else:
    print("Sorry! wrong answer.")

answer =input("Full form of NOS ?\n")
if answer.lower() == "network operating system":
    print("Correct Answer")
    score +=1
else:
    print("Sorry! wrong answer.")

answer =input("A fault in a computer program which prevents it from working correctly is known as _______?\n")
if answer.lower() == "bug":
    print("Correct Answer")
    score +=1
else:
    print("Sorry! wrong answer.")

answer =input("Who is the full form of CD ?\n")
if answer.lower() == "compact disk":
    print("Correct Answer")
    score +=1
else:
    print("Sorry! wrong answer.")

    print("Sorry! wrong answer.")

print(f"\nYou got {score} questions correct. \n You score is {(score/10)*100} %.")
if score == 10:
    print("\n     ****HURRAY! CONGRATULATION YOU WON THE QUIZ. *****")
elif score == 9 or score == 8:
    print("\nYou are very close to win , let's try once more time.")
else:
    print("\nButter luck next time.")