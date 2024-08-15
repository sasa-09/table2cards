import datetime as d
from data import data, update_data
from stats import words_list
from test import test


def repeat_list():

    for kw in words_list(0):
        current_data = d.date.today()
        time_delta = d.timedelta(days=data[kw]["learn"])
        repeat_date = current_data + time_delta
        data[kw]["rd"] = str(repeat_date)
        print(f"{data[kw]["word"]} - {data[kw]["rd"]}")

# repeat_list()



def repeat():
    i = 0
    for kw in words_list(0):
        if str(d.date.today()) == data[kw]["rd"]:
            while (i < len(words_list(0))):
                answer = input(f"({i}/?) Do you know that word? - {data[kw]["word"]} ")
                i += 1
                if answer == "y":
                    data[kw]["learn"] *= 2
                    break
                elif answer == "n":
                    if data[kw]["learn"] != 1:
                        data[kw]["learn"] /= 2
                    break
                else:
                    print(f"{data[kw]["word"]} {data[kw]["transc"]} - {data[kw]["transl"]}")
                    continue
    else:
        print("\n")
        for kw in words_list(0):
            if str(d.date.today()) == data[kw]["rd"]:
                print(f"{data[kw]["word"]} {data[kw]["transc"]} - {data[kw]["transl"]} ({data[kw]["learn"]})")
    update_data(data)


    # for kw in words_list(0):
    #     if str(d.date.today()) == data[kw]["rd"]:
    #         print(data[kw]["rd"])