from settings import data

def words_list(atr = None):
    unknown_list = []
    know_list = []
    for key_word in data:
        if data[key_word]["known"] == True:
            know_list.append(key_word)
        elif data[key_word]["known"] == False:
            unknown_list.append(key_word)
    if atr == 0:
        return unknown_list
    elif atr == 1:
        return know_list
    elif atr == None:
        all_list = unknown_list + know_list
        return all_list


def repeat_list(date):
    repeat_list = []
    for key_word in words_list():
        if data[key_word]["rd"] == date:
            repeat_list.append(key_word)
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
                for key_word in words_list(1):
                    print(f"{data[key_word]["word"]} {data[key_word]["transc"]} - {data[key_word]["transl"]}")
                break
            elif answer == "2":
                print("\nunknown_list:")
                for key_word in words_list(0):
                    print(f"{data[key_word]["word"]} {data[key_word]["transc"]} - {data[key_word]["transl"]}")
                break
            elif answer == "3":
                print("\nrepeat_list:")
                while (True):
                    date = input("enter date: ")
                    if date == "all":
                        for key_word in words_list():
                            print(f"{data[key_word]["word"]} - {data[key_word]["rd"]}")
                    elif date == "q":
                        catalyst_2 = False
                        break
                    else:
                        if repeat_list(date) == []:
                            continue
                        else:
                            catalyst_2 = False
                            for key_word in  repeat_list(date):
                                print(f"{data[key_word]["word"]} - {data[key_word]["rd"]}")
                            break
            elif answer == "q":
                catalyst = False
                break
            else:
                continue