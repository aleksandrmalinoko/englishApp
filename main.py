import random

if __name__ == '__main__':
    with open('2000full.txt', 'r', encoding='utf8') as f:  # открываем базовый словарь для чтения
        words = f.readlines()  # загоняем в переменную прочтенную строку
    for word in words:
        if word == "\n" or word == "\n " or word == "\n  ":
            words.remove(word)
    known = unknown = 0
    unknown_list = []
    while True:
        if len(unknown_list) == 0:
            temp_value = ""
            current_word, current_answer = words[random.randint(0, len(words))].split("\t", 1)
        else:
            rand_idx = random.randint(0, len(unknown_list) - 1)
            temp_value = unknown_list[rand_idx]
            current_word = temp_value[0]
            current_answer = temp_value[1]
        print(current_word)
        answer = input()
        if answer == '+':
            print(current_answer)
            known += 1
            if temp_value != "":
                unknown_list.remove(temp_value)
        elif answer == '-':
            print(current_answer)
            unknown += 1
            unknown_list.append([current_word, current_answer])
        else:
            break
    print("+ ", known, "; -", unknown)
