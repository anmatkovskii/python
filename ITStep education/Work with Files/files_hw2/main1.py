from transliterate import translit, get_available_language_codes


def task_one():
    file1 = open("task1.txt", "r")
    file2 = open("task1-2.txt", "r")

    data1 = file1.read()
    words = data1.split()
    data2 = file2.read()
    banned_words = data2.split()

    for i in words:
        if i in banned_words:
            words.remove(i)

    file1.close()
    file2.close()
    file1 = open("task1.txt", "w")

    for i in words:
        file1.write(i)
        file1.write(" ")

    file1.close()


# task_one()


def task_two():
    file1 = open("task1.txt", "r", encoding='utf-8')
    file2 = open("task2.txt", "w", encoding='utf-8')
    data1 = file1.read()

    file1.close()

    lang_choice = int(input("Type of translit: 1 - En->Ru, 2 - Ru-En"))
    if lang_choice == 1:
        file2.write(translit(data1, 'ru'))
    elif lang_choice == 2:
        file2.write(translit(data1, 'en'))
    else:
        print("Error")

    file2.close()


# task_two()


def task_three():
    files_to_join = []
    while True:
        file_choice = input("Enter new file's name, or print 'Quit' to exit program:\n")
        if file_choice == "Quit":
            break
        else:
            files_to_join.append(file_choice)

    file1 = open("task3-4.txt", "w")

    for i in files_to_join:
        file = open(i, "r")
        data = file.read()
        if files_to_join.index(i) != 0 and data[0] != " ":
            file1.write(" ")
        file1.write(data)
        file.close()

    file1.close()


# task_three()


def task_four():
    files_to_join = []
    while True:
        file_choice = input("Enter new file's name, or print 'Quit' to exit program:\n")
        if file_choice == "Quit":
            break
        else:
            files_to_join.append(file_choice)

    file1 = open("task4.txt", "w")

    for i in files_to_join:
        file = open(i, "r")
        data = file.read()
        for j in data:
            if j in "~!@#$%^&*()_-+=`'\"<>,./?[]{};':":
                file1.write(j)
                file1.write(" ")
        file.close()

    file1.close()


# task_four()