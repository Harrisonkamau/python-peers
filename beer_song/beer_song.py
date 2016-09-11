
beerNum = 99
word = "bottles"


while beerNum > 0:
    if beerNum == 1:
        word = "bottle"

    print str(beerNum) + " " + word + " of beer on the wall"
    print str(beerNum) + " " + word + " of beer"
    print"Take one down."
    print "Pass it around."
    beerNum -= 1

    if beerNum > 0:
        print str(beerNum) + " " + word + " of beer on the wall\n"
    else:
        print "\nNo more bottles of beer on the wall, no more bottles of beer.\n" \
              "Go to the store and buy some more, 99 bottles of beer on the wall."
