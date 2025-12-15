def h(n, a, b, c):
    if n > 0:
        h(n - 1, a, c, b)
        print(a, "->", c)
        h(n - 1, b, a, c)

n = int(input("Enter number of disks: "))
h(n, 'A', 'B', 'C')
                
