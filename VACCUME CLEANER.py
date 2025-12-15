l = input().split()
pos = input()

cost = 0
for i in range(len(l)):
    if str(i) == pos:
        if l[i] == 'D':
            l[i] = 'C'
            cost += 1
        else:
            cost += 1

    if l[i] == 'D':
        cost += 1

print("Updated list:", l)
print("Cost:", cost)
