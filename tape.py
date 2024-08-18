import random
from data import update_data
import datetime as d
from settings import data, max_words

def tape_data_update(key_word, known, learn):
    data[key_word]["known"] = known
    data[key_word]["learn"] = learn
    if not known:
        learn = 0
    repeat_date = str(d.datetime.today() + d.timedelta(days=learn)) 
    repeat_date = repeat_date.split()
    data[key_word]["rd"] = repeat_date[0]
    update_data(data)


def print_answer(key_word):
    print(f"{data[key_word]["word"]} {data[key_word]["transc"]} - {data[key_word]["transl"]}")


def tape():
    i = 0
    catalyst = True
    while (catalyst and i < max_words):
        key_word = str(random.randint(1, len(data)))
        while (True):
            if data[key_word]["known"] == None:
                answer = input(f"({i}/{max_words}) Do you know that word? - {data[key_word]["word"]} ")
                if answer == "y":
                    tape_data_update(key_word, True, 30)
                    break
                elif answer == "n":
                    tape_data_update(key_word, False, 1)
                    i += 1
                    break
                elif answer == "q":
                    catalyst = False
                    break
                else:
                    print_answer(key_word)
                    continue
            else:
                key_word = str(random.randint(1, len(data)))
            update_data(data)   
        
    else:
        print(f"({i}/3)\n")

