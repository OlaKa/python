#!/usr/bin/python
#
#A simple phonebook using write and get


class Phonebook:

    def __init__(self):
       self.name=""
       self.phonenr=""
       self.email=""

    def getinputfromuser(self):
        choice = raw_input("This is your phonebook. Please choose to add a user [Write 1] or see the content [Write 2]:")
        print choice
        if int(choice) == 2:
            self._display_phonebook("phonebook")
        elif int(choice) == 1 :
            self.name = raw_input("Enter name:")
            self.phonenr = raw_input("Enter phone number:")
            self.email =  raw_input("Enter email:")
            #Open file
            f = open("phonebook.txt", 'w')
            f.write( "Name:%s\tPhone:%s\tEmail:%s" % (self.name, self.phonenr,self.email))
        else:
           print "Wrong input"           
    
    def _display_phonebook(self,name):
        '''Displays all entries in phonebook'''
        filename = '%s.txt' % name
        f = open(filename, 'r')
        print "Your content is:\n%s" %(f.read())
        f.close()  
    
    def lookup_name(self, name):
        filename = '%s.txt' % name
        f = open(filename, 'r')
        with open(filename, 'r') as f:
            for line in f:
                print line.strip().split('\t')     
        
phone = Phonebook()
phone.getinputfromuser()

