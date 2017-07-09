 jabber = open("C:\\Users\\Ola\\Documents\\sample.txt")

 for line in jabber:
     print(line,end='')

 jabber.close()

 # alternative printing
 with open("C:\\Users\\Ola\\Documents\\sample.txt") as jabber:
     line = jabber.readline()
     while line:
         print(line,end='')
         line = jabber.readline()

 # alternative printing 2

with open("C:\\Users\\Ola\\Documents\\sample.txt",'r') as jabber:
    lines = jabber.readlines()
for line in lines:
    print(line, end='')

# alternative printing 3

with open("C:\\Users\\Ola\\Documents\\sample.txt",'r') as jabber:
     lines = jabber.readlines()
for line in lines[::-1]:
     print(line, end='')
     
