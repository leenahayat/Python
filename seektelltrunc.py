with open("file1.txt", "r+") as f:

    f.seek(3)
    print(f.tell())

    f.seek(5)
    print(f.read())

    f.truncate(4)


         