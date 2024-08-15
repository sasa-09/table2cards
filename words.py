import random

from data import get_data, update_data


data = get_data()


def words_random():
    i = 0
    cotal = True
    while (cotal):
        rk = str(random.randint(1, len(data)))

        while (True):
            if data[rk]["know"] == None:
                answer = input(f"Do you know that word? - {data[rk]["word"]} ")
                if answer == "y":
                    data[rk]["know"] = True
                    break
                elif answer == "n":
                    data[rk]["know"] = False
                    i += 1
                    break
                elif answer == "q":
                    cotal = False
                    break
                else:
                    print(f"{data[rk]["word"]} {data[rk]["transc"]} - {data[rk]["transl"]}")
                    continue
            else:
                rk = str(random.randint(1, len(data)))
        update_data(data)


