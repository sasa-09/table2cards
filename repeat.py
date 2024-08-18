import datetime as d

from data import update_data
from settings import data
from stats import words_list, repeat_list


def repeat():
    today = d.date.today()
    counter = len(repeat_list(str(today)))
    i = 0
    for key_word in words_list():
        if str(today) == data[key_word]["rd"] and data[key_word]["rd"] != data[key_word]["rdl"]:
            while (i < len(words_list())):
                answer = input(f"({i}/{counter}) Do you know that word? - {data[key_word]["word"]} ")
                data[key_word]["rdl"] = str(today)
                i += 1
                if answer == "y":
                    data[key_word]["known"] = True
                    data[key_word]["learn"] *= 2
                    break
                elif answer == "n":
                    data[key_word]["known"] = False
                    if data[key_word]["learn"] != 1:
                        data[key_word]["learn"] /= 2
                    break
                else:
                    print(f"{data[key_word]["word"]} {data[key_word]["transc"]} - {data[key_word]["transl"]}")
                    continue

            time_delta = d.timedelta(days=data[key_word]["learn"])
            repeat_date = today + time_delta
            data[key_word]["rd"] = str(repeat_date)
            update_data(data)
    else:
        print("\n")
        for key_word in words_list():
            if today == data[key_word]["rd"]:
                print(f"{data[key_word]["word"]} {data[key_word]["transc"]} - {data[key_word]["transl"]} (after {data[key_word]["learn"]} days)")
    update_data(data)