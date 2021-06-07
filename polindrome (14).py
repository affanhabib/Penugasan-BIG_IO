text = []
n = 0
while True:
    # print("Masukkan huruf: ")
    text.append(input())
    
    for x in text:
        print(x, end='')
    
    y = n-1
    while (y >= 0):
        print(text[y], end='')
        y = y-1

    print("\n", end='')
    n = n + 1 