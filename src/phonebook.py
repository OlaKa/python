#!/usr/bin/python
#
#A simple phonebook using write and get
import os


class Phonebook:

    def __init__(self):
       self.name=""
       self.phonenr=""
       self.email=""
       self.dirtofile="/tmp"
       self.filename="phonebook.txt"

    def getinputfromuser(self):
        choice = raw_input("This is your phonebook. Please choose to add a user [enter 1] or see the content [enter 2] or lookup name [enter 3}:")
        print choice
        if int(choice) == 2:
            self.display_phonebook(self.filename)
        elif int(choice) == 1 :
            self.name = raw_input("Enter name:")
            self.phonenr = raw_input("Enter phone number:")
            self.email =  raw_input("Enter email:")
            #Check if file exist or not 
            if self._does_file_exist(dirtofile,filename):
                #Append to file
                with open(filename, 'a') as myfile:
                    myfile.write("Name:%s\tPhone:%s\tEmail:%s" % (self.name, self.phonenr,self.email))
            else:
                 with open(filename, 'w') as myfile:
                    myfile.write("Name:%s\tPhone:%s\tEmail:%s" % (self.name, self.phonenr,self.email))
        elif int(choice) == 3:
             name = raw_input("Enter a name [press enter]:")
             print self.lookup_name(name)
        else:
           print "Wrong input"           
    
    def display_phonebook(self,name):
        '''Displays all entries in phonebook'''
        filename = '%s' % name
        with open(filename, 'r') as f:
            print "Your content is:\n%s" %(f.read())

    def _does_file_exist(self,file,path):
        datafile=dirtofile + filename
        try:
            with open(datafile) as f: pass
        except IOError as e:
            print("Error: %s not found." % datafile)
    
    def lookup_name(self, name):
        filename = '%s' % self.filename
        with open(filename, 'r') as f:
            for line in f:
                if name in line:
                    return line
        
phone = Phonebook()
phone.getinputfromuser()

