x = 5

n = 1
y = 2 * x
for i in range(0, x):
    n = 1
    for j in range(0, i):
        print(n, end="")
        n = n + 1
    for k in range(0, y-1):
        print(end=" ")
    y = y - 2
    for l in range(0, i):
        print(n-1, end="")
        n = n - 1
    print("\r")

for i in range(0, x):
    print(n, end="")
    n = n + 1
for j in range(0, x-1):
    print(n-2, end="")
    n = n - 1
print("\r")

m = x - 1
o = x - 1
for i in range(1, x):
    n = 1
    for j in range(0, m):
        print(n, end="")
        n = n + 1
    m = m - 1
    for k in range(0, y+1):
        print(end=" ")
    y = y + 2
    for l in range(0, o):
        print(n-1, end="")
        n = n - 1
    o = o - 1
    print("\r")
