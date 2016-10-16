# takes %d value in a string
x = "There are %d types of people." % 10
# set values for binary and do_not as strings
binary = "binary"
do_not = "don't"
# uses variables inside a string
y = "Those who know %s and those who %s." % (binary, do_not) # 4

#prints thw whole thing
print x
print y

print "I said: %r." % x  # 2
print "I also said: '%s'." % y # 3

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" # 1

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e

lol = "olar "
hehe = "sua loka"

print lol + hehe
