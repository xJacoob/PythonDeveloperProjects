# write your code here
import random
import math


def tasks_level_one():
    number_1 = random.randint(2, 9)
    number_2 = random.randint(2, 9)
    operations = ["+", "-", "*"]
    choice = random.choice(operations)
    equation = ' '.join(str(number_1) + choice + str(number_2))
    return equation

def tasks_level_two():
    return random.randint(11, 29)

def test_level():
    while True:
        try:
            level = int(input("Which level do you want? Enter a number: "))
            if level in [1 ,2]:
                break
            else:
                print("Incorrect format.")
        except ValueError:
            print("Incorrect format.")
    return level

def level_one():
    correct_ans = 0
    for _ in range(5):
        equation_ = tasks_level_one()
        print(equation_)
        while True:
            try:
                answer = int(input())
                if "+" in equation_:
                    result = int(equation_[0]) + int(equation_[4])
                elif "-" in equation_:
                    result = int(equation_[0]) - int(equation_[4])
                else:
                    result = int(equation_[0]) * int(equation_[4])

                if result == answer:
                    print("Right!")
                    correct_ans += 1
                else:
                    print("Wrong!")

                break

            except ValueError:
                print("Incorrect format.")
    return correct_ans

def level_two():
    correct_ans = 0
    for _ in range(5):
        equation_ = tasks_level_two()
        print(equation_)
        while True:
            try:
                answer = int(input())
                result = math.pow(int(equation_), 2)

                if result == answer:
                    print("Right!")
                    correct_ans += 1
                else:
                    print("Wrong!")

                break

            except ValueError:
                print("Incorrect format.")
    return correct_ans

def save(correct_answers, lvl):
    print(f"Your mark is {correct_answers}/5. Would you like to save your result to the file? Enter yes or no.")
    if lvl == 1:
        desc = "simple operations with numbers 2-9"
    else:
        desc = "integral squares 11-29"
    ans = input()
    if ans in ["yes", "YES", "y", "Yes"]:
        name = input("What is your name? ")

        with open("results.txt", "a") as file:
            file.write(f"{name}: {correct_answers}/5 in level {lvl} {desc}\n")
            print("The results are saved in \"results.txt\".")
    else:
        exit()

lvl_ = test_level()
if lvl_ == 1:
    results = level_one()
    save(results, lvl_)
elif lvl_ == 2:
    results = level_two()
    save(results, lvl_)


