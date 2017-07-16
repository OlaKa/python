#!/usr/bin/python
########################################################################
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc
########################################################################
#Caveat:a+b+c=10^2,18^2,24^2 but NOT a^2+b^2=c^2
import math

def tripleornot(list):
    """Function to test Pythagorean triplet"""
    first=list[0]
    last=list[1]
    if first>last:
        print "Range must be from lowest to highest (lo hi)!"
    for i in range (int(first),int(last)):
            for x in range (int(first),int(last)):
                for y in range (int(first),int(last)):
                    a=math.pow(int(i),2)
                    b=math.pow(int(x),2)
                    c=math.pow(int(y),2)
                    sum=a + b + c
                    if sum == 1000.0:
                        print "Got it! Numbers are: %s,%s,%s" %(i,x,y)
                        return

if __name__ == '__main__':                   
    list=raw_input("Give me a range to test Pythagorean triplet (lo hi):")
    splist=list.split()
    tripleornot(splist)

