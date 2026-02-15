'''file=open("students.txt","w") #x is used to create a new file if it does not exist and if it exist then it will give an error
file.write("Alice,85\n")#write is used to write the data in the file and \n is used to move to the next line after writing the data
file.write("Bob,90\n")
file.write("Charlie,78\n")
file.write("Diana,95\n")
file.close()#close is used to close the file after writing the data in it

with open ("students.txt","r") as infile :
    line=infile.readlines()#readlines is used to read the data from the file and it returns a list of lines in the file
with open("output.txt","w") as outfile :
    #a is used to append the data in the file if it already exist and if it does not exist then it will create a new file
    for newlines in line:
        name,score=newlines.strip().split(",")
        #strip is used to remove the newline character from the end of the line and split is used to split the line into name and score using comma as a separator
        outfile.write(f"Student:{name},Score:{score}\n")
        #write is used to write the data in the file and \n is used to move to the next line after writing the data
     '''

with open("students.txt","a") as file :
    file.write("Eve,88\n")
with open ("activity.log","w") as log_file:
    log_file.write("Added new student: Eve\n")