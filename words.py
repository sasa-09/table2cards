import random

from data import get_data, update_data


data = get_data()


def words_random():
    i = 0
    cotal = True
    while (cotal):
        rk = str(random.randint(1, len(data)))

        while (True):
            answer = input(f"Do you know that word? - {data[rk]["word"]} ")
            if data[rk]["know"] == None:
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


def words_list():
    unknow_list = []
    know_list = []
    for kw in data:
        if data[kw]["know"] == True:
            know_list.append(kw)
        elif data[kw]["know"] == False:
            unknow_list.append(kw)
    unknow_list = list(set(unknow_list))
    know_list = list(set(know_list))
    
    counter = f"{len(unknow_list) + len(know_list)}({len(know_list)})/{len(data)}"
    print(counter + ":\n")

    print("know_list:")
    for kw in know_list:
        print(f"{data[kw]["word"]} {data[kw]["transc"]} - {data[kw]["transl"]}")
    print("unknow_list:")
    for kw in unknow_list:
        print(f"{data[kw]["word"]} {data[kw]["transc"]} - {data[kw]["transl"]}")

