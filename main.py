from data import data
from stats import stats
from tape import tape
from repeat import repeat, repeat_list

def main():
    nl = tape()
    print("learn these words:")
    for kw in nl:
        print(f"{data[kw]["word"]} {data[kw]["transc"]} - {data[kw]["transl"]}")
    print("\nrepeat these words:")
    repeat()
    print("\nnext repeat:")
    repeat_list()

    

while(True):
    message = """
    Hello! What do you want to do?:
    0. main
    1. type
    2. stats
    3. repeat
    4. repeat_list
    ...
    """
    answer = input(message)
    if answer == "0":
        main()
    elif answer == "1":
        tape()
    elif answer == "2":
        stats()
    elif answer == "3":
        repeat()
    elif answer == "4":
        repeat_list()
    elif answer == "q":
        break
    else:
        continue




