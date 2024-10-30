my_sum = 0
for number in range(1, 101):
    if number % 2 == 0:
        my_sum += number

print(f"Sum of even number from 1 to 100 is: {my_sum}")

for number in range(1, 301):
    if number % 7 == 0 and number % 3 == 0:
        print("Charlie Brown")
    elif number % 7 == 0:
        print("Charlie")
    elif number % 3 == 0:
        print("Brown")
    else:
        print(number)
