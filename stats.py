from settings import data

def words_list(atr = None):
    unknown_list = []
    know_list = []
    for kw in data:
        if data[kw]["known"] == True:
            know_list.append(kw)
        elif data[kw]["known"] == False:
            unknown_list.append(kw)
    if atr == 0:
        return unknown_list
    elif atr == 1:
        return know_list
    elif atr == None:
        all_list = unknown_list + know_list
        return all_list


def repeat_list(date):
    repeat_list = []
    for kw in words_list():
        if data[kw]["rd"] == date:
            repeat_list.append(kw)
    return repeat_list


def stats():
    catalyst = True
    while(catalyst):
        catalyst_2 = True
        message = f"""
        All words: {len(data)}
        1. Known words: {len(words_list(1))}
        2. Unknown words: {len(words_list(0))}
        3. Repeat words: {len(words_list())}
        """
        message
        while(catalyst_2):
            answer = input(message)
            if answer == "1":
                print("\nknown_list:")
                for kw in words_list(1):
                    print(f"{data[kw]["word"]} {data[kw]["transc"]} - {data[kw]["transl"]}")
                break
            elif answer == "2":
                print("\nunknown_list:")
                for kw in words_list(0):
                    print(f"{data[kw]["word"]} {data[kw]["transc"]} - {data[kw]["transl"]}")
                break
            elif answer == "3":
                print("\nrepeat_list:")
                while (True):
                    date = input("enter date: ")
                    if date == "all":
                        for kw in words_list():
                            print(f"{data[kw]["word"]} - {data[kw]["rd"]}")
                    elif date == "q":
                        catalyst_2 = False
                        break
                    else:
                        if repeat_list(date) == []:
                            continue
                        else:
                            catalyst_2 = False
                            for kw in  repeat_list(date):
                                print(f"{data[kw]["word"]} - {data[kw]["rd"]}")
                            break
            elif answer == "q":
                catalyst = False
                break
            else:
                continue