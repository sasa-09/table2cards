from settings import data

def words_list(atr):
    unknow_list = []
    know_list = []
    for kw in data:
        if data[kw]["know"] == True:
            know_list.append(kw)
        elif data[kw]["know"] == False:
            unknow_list.append(kw)
    unknow_list = list(set(unknow_list))
    know_list = list(set(know_list))
    if atr == 0:
        return unknow_list
    elif atr == 1:
        return know_list


def stats():
    cotal = True
    while(cotal):
        message = f"""
        All words: {len(data)}
        1. Know words: {len(words_list(1))}
        2. Unknow words: {len(words_list(0))}
        3. Repeat words: {len(words_list(0))}
        """
        print(message)
        answer = input()
        while(True):
            if answer == "1":
                print("\nknow_list:")
                for kw in words_list(1):
                    print(f"{data[kw]["word"]} {data[kw]["transc"]} - {data[kw]["transl"]}")
                break
            elif answer == "2":
                print("\nunknow_list:")
                for kw in words_list(0):
                    print(f"{data[kw]["word"]} {data[kw]["transc"]} - {data[kw]["transl"]}")
                break
            elif answer == "3":
                print("\nrepeat_list:")
                for kw in words_list(0): 
                    print(f"{data[kw]["word"]} - {data[kw]["rd"]}")
                break

            elif answer == "q":
                cotal = False
                break
            else:
                continue