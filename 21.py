from games import boom as boomy

name = "tomer"
if name == "tomer":
    print("Your name is tomer")
elif name == "kopel":
    print("your name is kopel")
else:
    print("your name is not tomer and not kopel")

listOfNumbers = [1, 2, 3]
if listOfNumbers == [1, 2, 3]:
    print("same list")
if type(listOfNumbers == list):
    if 3 in listOfNumbers:
        print("3 is in numbers")
print(len(listOfNumbers))

rangeOfNumbers = range(3)
print(rangeOfNumbers)
for number in rangeOfNumbers:
    print(number)

x = 0
while x < 10:
    x += 1
    if x == 4:
        continue
    if x == 6:
        break
    print(f"still counting... {x}")

somethingToImplement = True
if somethingToImplement:
    pass

maxNum = input("Enter a number: ")
boomy(int(maxNum))
