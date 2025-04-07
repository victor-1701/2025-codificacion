def tabla_ascci():
    for i in range(33, 1025):
        print(str(i).ljust(5), "-" + chr(i), end="      ")
        if i % 4 == 0:
            print()


tabla_ascci()
