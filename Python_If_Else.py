num = int(input())

if num % 2:
    print("Weird")
else:
    # if num >= 2 and num <= 5:
    if 2 <= num <= 5:
        print("Not Weird")
    # elif num >= 6 and num <= 20:
    elif 6 <= num <= 20:
        print("Weird")
    else:
        print("Not Weird")
