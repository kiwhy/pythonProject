print("문자열입력")

first = input(str())
j = len(first)
last = []

for i in range(1, j+1):
    last += first[j-i]

print(last)