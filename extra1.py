print "this will run forever if you don't \n use ctrl+c"
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
