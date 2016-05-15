guesscheck = 0
correct = 0
tempright = 0
tempwrong = 0
totwrong = 0
letternum = 0
letterprint = 0

letter1 = "X"
letter2 = "X"
letter3 = "X"
letter4 = "X"
letter5 = "X"
letter6 = "X"
letter7 = "X"
letter8 = "X"
letter9 = "X"
letter10 = "X"


print ("Welcome to Hangman ")
name1 = input("Player 1, enter your first name ")
name2 = input("Player 2, enter your first name ")
print(name2 + " look away")
word = input (name1 + " Enter your word ")
wordlen = len(word)
while 1 > wordlen > 10:
    word = input("Please enter a word between 1 and 10 characters ")
    wordlen = len(word)

print (name1 + ", thank you for entering a valid word ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")


while (correct < wordlen) or (totwrong < wordlength):

        guescheck = 0

        tempright = 0
                                    
        if wordlen == 1:
        
            print(letter1)

        if wordlen == 2:

            print (letter1 + letter2)

        if wordlen == 3:

            print (letter1 + letter2 + letter3)
            
        if wordlen == 4:

            print (letter1 + letter2 + letter3 + letter4)
            
        if wordlen == 5:

            print (letter1 + letter2 + letter3 + letter4 + letter5)
                        
        if wordlen == 6:

            print (letter1 + letter2 + letter3 + letter4 + letter5 + letter6)
                                    
        if wordlen == 7:

            print (letter1 + letter2 + letter3 + letter4 + letter5 + letter6 + letter7)
                                   
        if wordlen == 8:

            print (letter1 + letter2 + letter3 + letter4 + letter5 + letter6 + letter7 + letter8)
                                    
        if wordlen == 9:

            print (letter1 + letter2 + letter3 + letter4 + letter5 + letter6 + letter7 + letter8 + letter9)
                                    
        if wordlen == 10:

            print (letter1 + letter2 + letter3 + letter4 + letter5 + letter6 + letter7 + letter8 + letter9 + letter10)
            


        p2guess = input (name2 + " enter a 1 letter guess: ")

        while guesscheck < wordlen:
            

            if p2guess == word[guesscheck]:
                tempright = tempright + 1

                print(tempright)

            else:
                
                tempwrong = tempwrong + 1

            if tempwrong == wordlen:
                totwrong = totwrong + 1

            guesscheck = guesscheck + 1



        if tempright > 0:
            print("you got " + str(tempright) + " letters right")

        else:
            print ("You got no letters right")

            totwrong = totwrong + 1

        correct = correct + tempright

        print("you have " + str(correct) + " total letter(s) right")






