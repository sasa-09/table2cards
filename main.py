from settings import data

from tape import tape
from stats import stats
from repeat import repeat
from conversion import conversion
from data import update_data


while(True):
    message = """
    Hello! What do you want to do?:
    1. type
    2. stats
    3. repeat
    4. conversion
    ...
    """
    answer = input(message)
    if answer == "1":
        tape()
    elif answer == "2":
        stats()
    elif answer == "3":
        repeat()
    elif answer == "4":
        update_data(conversion())
    elif answer == "q":
        break
    else:
        continue