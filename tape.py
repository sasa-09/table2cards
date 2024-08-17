import random
from data import update_data
import datetime as d
from settings import data, max_words


def tape():
    i = 0
    today = d.date.today()
    catalyst = True
    nl = []
    while (catalyst and i < max_words):
        kw = str(random.randint(1, len(data)))

        while (True):
            if data[kw]["known"] == None:
                answer = input(f"({i}/{max_words}) Do you know that word? - {data[kw]["word"]} ")
                if answer == "y":
                    data[kw]["known"] = True
                    data[kw]["learn"] = 30
                    data[kw]["rd"] = str(today + d.timedelta(days=data[kw]["learn"]))
                    update_data(data)
                    break
                elif answer == "n":
                    data[kw]["known"] = False
                    data[kw]["learn"] = 1
                    data[kw]["rd"] = str(today)
                    nl.append(kw)
                    i += 1
                    update_data(data)
                    break
                elif answer == "q":
                    catalyst = False
                    break
                else:
                    print(f"{data[kw]["word"]} {data[kw]["transc"]} - {data[kw]["transl"]}")
                    continue
            else:
                kw = str(random.randint(1, len(data)))
            update_data(data)   
        
    else:
        print(f"({i}/3)\n")
    return nl

