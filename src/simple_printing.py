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
  
# read from file and remove \n

list = ['Ola','Karlsson','Melania', 'Trump']
conc_list = []
with open('names.txt','w') as name_list:
    for names in list:
        print(names, file=name_list)

with open('names.txt', 'r') as file:
    for line in file:
        conc_list.append(line)


strip_list = [item.strip() for item in conc_list]

print(strip_list)
     
