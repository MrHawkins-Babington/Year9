#year 9 code - 10 green bottles

#The complete code

num = 10

while num>0:
    print("There are ",num,"green bottles, hanging on the wall")
    print(num,"green bottles, hanging on the wall!")
    print("and if one green bottle should actually fall...")
    num = num - 1
    answer = int(input("How many green bottles will be hanging on the wall?"))
    if answer == num:
        print("There will be",num,"green bottles hanging on the wall!")
    else:
        while answer != num:
            answer = int(input("No, try again!"))
print("There are no green bottles, hanging on the wall!")
