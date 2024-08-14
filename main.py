from words import words_list, words_random


while(True):
    message = """
    Hello! What do you want to do?:
    1. words_random
    2. words_list 
    ...
    """
    answer = input(message)
    if answer == "1":
        words_random()
    elif answer == "2":
        words_list()
    elif answer == "q":
        break
    else:
        continue




