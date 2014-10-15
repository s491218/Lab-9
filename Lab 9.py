print "Welcome to the celcius to fahrenheit calculator!"
print "What is your number in celcius?"
celcius = int(raw_input())
fahrenhit = celcius * 9 / 5 + 32
print fahrenhit

myList = [102,106,98,99,104,95,101]
newList = []
for x in myList:
    if x >= 100:
        newList.append(x)
print newList
    
