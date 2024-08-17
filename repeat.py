import datetime as d

from data import update_data
from settings import data
from stats import words_list, repeat_list


def repeat():
    today = d.date.today()
    counter = len(repeat_list(str(today)))
    i = 0
    for kw in words_list():
        if str(today) == data[kw]["rd"] and data[kw]["rd"] != data[kw]["rdl"]:
            while (i < len(words_list())):
                answer = input(f"({i}/{counter}) Do you know that word? - {data[kw]["word"]} ")
                data[kw]["rdl"] = str(today)
                i += 1
                if answer == "y":
                    data[kw]["known"] = True
                    data[kw]["learn"] *= 2
                    break
                elif answer == "n":
                    data[kw]["known"] = False
                    if data[kw]["learn"] != 1:
                        data[kw]["learn"] /= 2
                    break
                else:
                    print(f"{data[kw]["word"]} {data[kw]["transc"]} - {data[kw]["transl"]}")
                    continue

            time_delta = d.timedelta(days=data[kw]["learn"])
            repeat_date = today + time_delta
            data[kw]["rd"] = str(repeat_date)
            update_data(data)
    else:
        print("\n")
        for kw in words_list():
            if today == data[kw]["rd"]:
                print(f"{data[kw]["word"]} {data[kw]["transc"]} - {data[kw]["transl"]} (after {data[kw]["learn"]} days)")
    update_data(data)