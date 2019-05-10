print ">>> WORD SCRAMBLER HACK"
print ">>> USEFUL FOR ALL WORD SCRAMBLE GAMES e.g WORD COOKIES"
print ">>> Courtesy of mieliestronk.com\n\n"


probability = []
main_words = set()
clean = set()

letter = raw_input("Input a word to be scrambled:\n")
#open a file
file = open("english1.txt","r")
text=file.read()
texts = text.split("\n")
#convert words from file to lowercase
for v in texts:
    r=v.lower()
#remove any symbols
    symbols = "!@#$%^&*()_-+=<,>.?/:;{}[]\"'"
    for i in range(len(symbols)):
        r=r.replace(symbols[i],"")
#add to set created
        main_words.add(r)

for i in letter:
    letter0 = list(letter)
    letter0.remove(i)
    #print letter0
    for o in letter0:
        new = i
        new+=o

        probability.append(new)


for some in probability:
            letter1 = list(letter)
            check = list(some)
            #print check
            #print letter0
            for x in check:
                letter1.remove(x)

            for z in letter1:
                var = some+z
                #print var
                probability.append(var)



for words in probability:
    may= words.lower()
    clean.add(may)
for word in clean:
    if word in main_words:
        print word


file.close()
print"\n\n>>> N.B:This is not 100% accurate"
print">>> Made BY:Daniel Ogbuti"














