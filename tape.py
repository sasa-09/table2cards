import random
from data import update_data
import datetime as d
from settings import data


def tape():
    i = 0
    today = str(d.date.today())
    cotal = True
    nl = []
    while (cotal and i < 3):
        kw = str(random.randint(1, len(data)))

        while (True):
            if data[kw]["know"] == None:
                answer = input(f"({i}/3) Do you know that word? - {data[kw]["word"]} ")
                if answer == "y":
                    data[kw]["know"] = True
                    break
                elif answer == "n":
                    data[kw]["know"] = False
                    i += 1
                    nl.append(kw)
                    data[kw]["rd"] = today
                    data[kw]["learn"] = 1
                    break
                elif answer == "q":
                    cotal = False
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

