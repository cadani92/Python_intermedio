def read():
    numbers = []
    with open("./archivo/number.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
            print(numbers)


def write():
    names = ["Miguel", "Mario", "Ana"]
    with open("./archivo/names.txt", "w") as f:
        for name in names:
            f.write(name)
            f.write("/n")


def run():
    write()
    pass




if __name__ == '__main__':
    run()