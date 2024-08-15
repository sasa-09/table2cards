from words import words_random
from stats import stats

while(True):
    message = """
    Hello! What do you want to do?:
    1. words_random
    2. words_stats 
    ...
    """
    answer = input(message)
    if answer == "1":
        words_random()
    elif answer == "2":
        stats()
    elif answer == "q":
        break
    else:
        continue




