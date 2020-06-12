
                            #//////////// AGE CALCULATOR //////////////

def after99(user):
    if len(user) == 4:
        user = int(user)
        age100 = user + 100
        if 1900 < user < 1920:
            if user < 1912:
                print(f"You were 100 years old in {age100}. You seems to be oldest man alive!")
            else: print(f"You were 100 years old in {age100}. ")
        elif 1919 < user < 2020:
            print(f"You will be 100 years old in {age100}.")
        elif 1898 < user < 1901:
            print(f"You're still alive..\nin {age100} you were 100 years old. You are the oldest man alive!")
        elif 1899 > user:
            print(f"You're not even alive..\nanyways in {age100} you were 100 years old Mr.GHOST.")
        else: print("You're not even born yet...")
    elif len(user) < 4:
        user = int(user)
        age100 = 2020 + 100 - user
        if 100 < user < 120:
            if user < 108:
             print(f"You were 100 years old in {age100}.")
            else: print(f"You were 100 years old in {age100}. You seems to be oldest man alive!")
        elif 0 < user < 101:
            print(f"You will be 100 years old in {age100}.")
        elif 119 < user < 123:
            print(f"You're still alive..\nin {age100} you were 100 years old. You are the oldest man alive!")
        elif 122 < user:
            print(f"You're not even alive..\nanyways in {age100} you were 100 years old Mr.GHOST.")
        else: print("You're not even born yet...")
    else: print("YOU're NOT FROM FUTURE DUM!\n ENTER THE CORRECT AGE OR BIRTH YEAR.")

def ageAfter(ageyear, user):
    # ageyear = int(input("enter year you waana see your age in : "))
    if len(user) == 4:
        user=int(user)
        currentAge = 2020 - user
        if ageyear > 2020:
            furage = currentAge+(ageyear-2020)
            print(f"You will be {furage} years old in {ageyear}.")
        else:
            furage = currentAge-(2020-ageyear)
            print(f"You were {furage} years old in {ageyear}.")
    elif len(user) < 4:
        user=int(user)
        if ageyear > 2020:
            furage = user+(ageyear-2020)
            print(f"You will be {furage} years old in {ageyear}.")
        else:
            furage = user-(2020-ageyear)
            print(f"You were {furage} years old in {ageyear}.")
    else: print("YOU're NOT FROM FUTURE DUM!\n ENTER THE CORRECT AGE OR BIRTH YEAR.")

if __name__ == '__main__':
    print("////////////////AGE CALCULATOR/////////////////")
    print("See the year you will or were 100 years old!")
    print("Please enter your age OR year of birth : ")
    user = input()
    after99(user)
    exit = False
    while exit is False:
        fur = input("wanna continue(y/n) : ")
        user = str(user)
        if fur == 'n':
            exit = True
        elif fur == 'y':
            ageyear = int(input("enter year you waana see your age in : "))
            ageAfter(ageyear, user)
        continue
