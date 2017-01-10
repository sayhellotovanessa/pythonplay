from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I am the %s script." % (user_name, script)
print "How are you, %s?" % (user_name)
feels = raw_input(prompt)

print "I have a few questions for you."
print "Do you like me, %s?" % user_name
likes = raw_input(prompt)

print "Where do you live, %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you use?"
computer = raw_input(prompt)

print """
You are feeling %r.
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (feels, likes, lives, computer)
