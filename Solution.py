length = int(input())
count = 1
counter = 1

while count <= length:
    print(('#' * counter).center(length * 2))
    counter += 2
    count += 1
