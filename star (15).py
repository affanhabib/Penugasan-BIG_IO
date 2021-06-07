while True:
    # print("Masukkan Jumlah: ")
    x = int(input())

    if x == "q":
        quit
    else:
        n = x - 1
        for i in range(0, n):
            for j in range(0, i):
                print(end=" ")
            for k in range(i, x):
                print("* ", end="")
            print("\r")
        for i in range(0, x):
            for j in range(0, n):
                print(end=" ")
            n = n - 1
            for k in range(1, i+2):
                print("* ", end="")
            print("\r")