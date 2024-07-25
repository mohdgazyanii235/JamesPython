MAX = int(input("How many numbers do you want to see: "))

old_i = 0
i = 1


for n in range(0, MAX):
    temporary = old_i + i
    old_i = i
    i = temporary
    print(temporary)

print("DONE")