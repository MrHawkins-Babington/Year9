#write a program to input a valid gamertag
#gamertag cannot be longer than 15 characters

valid_gamertag = True
while valid_gamertag == True:
    print("Gamertag cannot be longer than 15 characters")
    print("Gamertag cannot be shorter than 5 characters")
    print("Enter your new gamertag")
    gamertag = input()
    gamertag_length = len(gamertag)
    if gamertag_length > 15:
        print("Your gamertag is too long")
    elif gamertag_length <5:
        print("Your gamertag is too short")
    else:
        print("Gamertag accepted")
        valid_gamertag = False
