#Drew Childs, Program 4, 10/21/19
import csv

info = []
while True:
    while True:     #This while loop decides if you entered a valid file or decided to quit
        try:        #It also opens the desired file and reads all info into info
            file = str(input("Enter the name of the file (quit to exit) ==> "))
            with open(file, "r") as file_read:
                reader = csv.reader(file_read)
                info = list(reader)
            break
        except:
            if file == "Quit" or file == "quit":
                break
            else:
                print("Could not open the file, please enter another.")
    if file == "Quit" or file == "quit":
        break

    file_write = open("Students_grade.csv", "w")    #Opens file to write to
    print("Reading data and outputting to Students_grade...")

    info_write = []
    counter = 0         #This counter is just to itterate through every person currently in the input file
    for each in info:
        info_write = []
        
        info_write.append(str(info[counter][0]))        #This block writes the student's name and
        info_write.append(str(info[counter][1]))        #previous scores
        info_write.append(str(info[counter][2]))
        info_write.append(str(info[counter][3]))
        info_write.append(str(info[counter][4]))
        
        ex1 = (float(info[counter][1]) * 0.10)          #Finds exam one percentage
        info_write.append(str(ex1))
        
        ex2 = (float(info[counter][2]) * 0.10)          #Finds exam two percentage
        info_write.append(str(ex2))
        
        as1 = (float(info[counter][3]) * 0.05)          #finds assignment one percentage
        info_write.append(str(as1))
            
        as2 = (float(info[counter][4]) * 0.05)          #finds assignment two percentage
        info_write.append(str(as2))
        
        per30 = ex1 + ex2 + as1 + as2                   #finds the total out of 30%
        info_write.append(str(per30))
            
        per100 = (per30 / 30) * 100                     #Finds the total out of 100%
        info_write.append(str(per100))
                        
        grade = ""                                      #Calculates letter grade
        if per100 >= 91:
            grade = "A"
        elif per100 >= 81:
            grade = "B"
        elif per100 >= 71:
            grade = "B-"
        elif per100 >= 61:
            grade = "C"
        elif per100<= 60:
            grade = "F"
        info_write.append(grade)                        #writes to csv file
        counter += 1
        writer = csv.writer(file_write)
        writer.writerow(info_write)
    file_read.close()                                   #Closes files
    file_write.close()
