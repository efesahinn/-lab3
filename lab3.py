num = int(input("1 den büyük bir sayı girin "))
steps = 0
print(num, end="") #nromalde print de alt satıra geçiyor end aynı satırda devam ettirir

while num != 1:
    if num % 2 == 0:
        num = num // 2
    else:
        num = num * 3 + 1

    print(" →", num,end="")
    steps += 1

print("\n toplam adım:", steps)
#//////////////////////////////////////////////////////////// task 2
n = int(input("Enter a number between 10 and 100: "))

while n < 10 or n > 100:
    n = int(input("Invalid! Enter a number between 10 and 100: "))

fizz_count = 0
buzz_count = 0
fizzbuzz_count = 0

for i in range(1, n + 1):

    if i % 7 == 0:
        print(i,"skipped")
        continue

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        fizzbuzz_count += 1

    elif i % 3 == 0:
        print("Fizz")
        fizz_count += 1

    elif i % 5 == 0:
        print("Buzz")
        buzz_count += 1

    else:
        print(i)

print("Summary:")
print("Fizz:", fizz_count)
print("Buzz:", buzz_count)
print("FizzBuzz:", fizzbuzz_count)
#////////////////////////////////////////////////task3

nem = int(input("Enter a number between 3 and 9: "))
while nem < 3 or nem > 9:
    nem = int(input("Invalid! Enter a number between 3 and 9: "))


for i in range(1, nem + 1): #üst kısım
    print("*" * i)

for i in range(nem - 1, 0, -1): #alt kısım
    print("*" * i)

