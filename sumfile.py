f = open('number.txt', 'r')
ans = 0
for line in f:
    try:
        ans += int(line.strip())
    except ValueError:
        pass

print("Summa all numbers in file is: " + str(ans))