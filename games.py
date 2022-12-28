def boom(maxNumber):
    rangeOf1toNum = range(1, maxNumber+1)
    for num in rangeOf1toNum:
        #if num % 7 == 0 or int(num/10) == 7 or num % 10 == 7:
        if num % 7 == 0 or '7' in str(num):
            print("BOOM!")
        else:
            print(num)