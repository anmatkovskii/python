def task_one():
    file1 = open("1.txt", "r")
    file2 = open("2.txt", "r")

    data1 = file1.read()
    words1 = data1.split()
    data2 = file2.read()
    words2 = data2.split()

    print("Lines in file 1 but not in file 2: ", set(words1) - set(words2))
    print("Lines in file 2 but not in file 1: ", set(words2) - set(words1))

    file1.close()
    file2.close()


task_one()


def task_two():
    file1 = open("2.txt", "r")
    file2 = open("3.txt", "w")

    data = file1.read()
    lines_list = len(data.split('\n'))

    number_of_characters = f'Number of characters in text file: {len(data)}\n'
    file2.write(number_of_characters)
    lines = f"Lines in your file: {lines_list}\n"
    file2.write(lines)

    vowels = 0
    consonants = 0
    numbers = 0

    for i in data:
        if i in "aoeiu":
            vowels += 1
        elif i in "qwrtypsdfghjklzxcvbnm":
            consonants += 1
        elif i in "0123456789":
            numbers += 1

    file2.write(f"Vowels: {vowels}\n")
    file2.write(f"Consonants: {consonants}\n")
    file2.write(f"Numbers: {numbers}\n")

    file1.close()
    file2.close()


task_two()


def task_three():
    file1 = open("2.txt", "r")
    file2 = open("4.txt", "w")

    data1 = file1.read()
    words1 = data1.split()

    words1.pop()

    for i in words1:
        file2.write(i)
        file2.write("\n")

    file1.close()
    file2.close()


task_three()


def task_four():
    file = open("2.txt", "r")

    data = file.read()
    words = data.split()

    print(f"The biggest line has {len(max(words, key=len))} symbols")

    file.close()


task_four()


def task_five():
    file = open("1.txt", "r")

    frase = input("Enter frase to search:\n")
    print(file.read().count(frase))

    file.close()


task_five()


def task_six():
    file = open("1.txt", "r")

    data = file.read()

    frase = str(input("Enter frase to search:\n"))
    frase_replace = str(input("Enter frase to replace:\n"))

    data = data.replace(frase, frase_replace)
    file.close()
    file = open("1.txt", "w")
    file.write(data)

    file.close()


task_six()
