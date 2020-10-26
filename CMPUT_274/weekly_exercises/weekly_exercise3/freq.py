#--------------------------------------------
#   Name: Samir Raza
#   ID: 1627182
#   CMPUT 274, Fall 2020
#
#   Weekly Exercise 3: Word Frequency
#-------------------------------------------- 


import sys

#This function takes command line input as an argument and it opens
#a file with the same name, and it has error messages
def command_line():

    #Error Messages when argument is too long, too short, or if the 
    #file does not exist

    if len(sys.argv) > 2:
        print("There are too many command-line arguments :(")
        print("Here is an example of the correct use of the program:")
        print("")
        print("python3 freq.py <input_file_name>")
        print("")
        print("Where <input_file_name> is replaced by the name of an")
        print("input file in the same directory as freq.py")
        exit()

    if len(sys.argv) < 2:
        print("There are too few command-line arguments :(")
        print("Here is an example of the correct use of the program:")
        print("")
        print("python3 freq.py <input_file_name>")
        print("")
        print("Where <input_file_name> is replaced by the name of an")
        print("input file in the same directory as freq.py")
        exit()

    #Turning a file into a list so that the program can take in the data
    #from the list and produce desired output file
    try:
        readfile = (open(sys.argv[1],"r")).read()
        listfile = readfile.split()
    except:
        print("The inputed argument is not a file in the same directory")
        print("as freq.py")
        exit()


    #creating a variable out of the argument for easy access
    filename = sys.argv[1]

    return filename, listfile

pass

#This function generates a sorted list
def generate_list(listfile):
    #empty dictionary used to store data
    dic = {}
    i = 0
    count = 0

    #Generating counts of each word and storing them in a
    #dictionary for easy access and matching it with its
    #word. So the word is the key, and the count is its
    #value
    while i < len(listfile):
        j = listfile[i]
        count = count + (listfile).count(j)
        dic[listfile[i]] = count
        i = i + 1
        count = 0

    diclist = []

    #Using the count from the dictionary to create frequency
    #of each word and creating a string with the key of the 
    #dictionary, the value, and the frequency that was  
    #calculated
    for k in dic:
        x = str(dic[k])
        x = int(x)
        x = float(x)
        y = len(listfile)
        y = float(y)
        z = x/y
        z = round(z, 3)
        dicstring = str(k) + " " + str(dic[k]) + " " + str(z)
        diclist.append(dicstring)

    #sorting in lexicographical order
    diclist = sorted(diclist)    
    return diclist
pass

#This function outputs our list into a file
def output(diclist, filename):

    #making an output file
    outName = filename + ".out"

    outF = open(outName, "w")
    for line in diclist:
        outF.write(line)
        outF.write("\n")
    outF.close()
pass

if __name__ == "__main__":	
	
	(filename, listfile) = command_line()
	(diclist) = generate_list(listfile)
	output(diclist, filename)
pass