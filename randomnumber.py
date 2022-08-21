import time
import sys
import random
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
def rem_lst_lne():
    sys.stdout.write('\x1b[1A')

    sys.stdout.write('\x1b[2K')
def gen():
    rem_lst_lne()
        while True:
            rem_lst_lne()
            input("Welcome to the Random Number Generator.")
            rem_lst_lne()
            choice1 = input("From: ")
            rem_lst_lne()
            choice2 = input("To: ")         
            gen = input("Press Enter To Generate or O to open menu: ")
            if gen == "":
                rem_lst_lne()
                randint = random.randint(float(choice1), float(choice2))
                print(randint)
                
                continue
            else:
                rem_lst_lne()
                ask = input("What do you want to do Generate or Exit: (G/e) ")
                if ask == "":
                    rem_lst_lne()
                    continue
                elif ask == "G":
                    rem_lst_lne()
                    continue
                elif ask == "g":
                    rem_lst_lne()
                    continue
                elif ask == "e":
                    rem_lst_lne()
                    return
                elif ask == "E":
                    rem_lst_lne()
                    return
                else:
                    rem_lst_lne()
                    print(color.BOLD + color.RED + "Error Did Not Understand Command")
                    continue

gen()