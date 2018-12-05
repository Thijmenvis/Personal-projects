def cheeseAndCrackers(cheeseCount, boxesOfCrackers):
    print "you have %d cheeses!" % cheeseCount
    print "you have %d boxes of crackers!" % boxesOfCrackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheeseAndCrackers(20, 30)

print "Or we can use variables from our script:"
amountOfCheese = 10
amountofCrackers = 50

cheeseAndCrackers(amountOfCheese, amountofCrackers)

print "We can even do math inside too:"
cheeseAndCrackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheeseAndCrackers(amountOfCheese + 100, amountofCrackers + 1000)
