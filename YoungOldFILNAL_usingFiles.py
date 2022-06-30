#Search the youngest and oldest student
#L.Silaghi
#11/02/2021

print ("Welcome to my Youngest Oldest Student program")
print('***************Liviu Silaghi*****************')
input("\npress Enter to begin")

def readFile():
    #Import
    import csv

    input("Press Enter to read the files")

    #Opem file in read mode
    f=open("class list ages (1).csv")
    csvFile=csv.reader(f)

    #Create empty arrays
    firstnames=[]
    surnames=[]
    ages=[]

    #Loop through each row in the file
    for row in csvFile:
        #Append each item to arrays
        firstnames.append(row[0]) #colum A
        surnames.append(row[1]) #colom B
        ages.append(int(row[2])) #Ages

    #Close the file
    f.close()

    print("file handling success")
    return firstnames, surnames, ages


#find the lowest number
def findtheOldest(ages, firstnames):
    oldestAge= ages[0]
    oldestName=firstnames[0]

    for counter in range(1,len(firstnames)):
       if  ages[counter] > oldestAge:
           oldestAge=ages[counter]
           oldestName=firstnames[counter]
    return oldestAge, oldestName

#fint the highest number
def findtheYoungest(ages, firstnames):
    youngestAge= ages[0]
    youngestName=firstnames[0]

    for counter in range(1,len(firstnames)):
       if  ages[counter] < youngestAge:
           youngestAge=ages[counter]
           youngestName=firstnames[counter]
    return youngestAge, youngestName

#display
def display(oldestAge, oldestName, youngestAge, youngestName):
    print("The youngest student is:" ,youngestName,"",youngestAge, "years old")
    print("The oldest student is:" ,oldestName,"",oldestAge, "years old")

   
#run
firstnames, surnames, ages=readFile()
oldestAge, oldestName=findtheOldest(ages, firstnames)
youngestAge, youngestName=findtheYoungest(ages, firstnames)
display(oldestAge, oldestName, youngestAge, youngestName)

input("\npress Enter to exit")



