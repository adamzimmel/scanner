import csv

with open("CityInv.csv", 'r') as scoreFile:
    csvReader = csv.reader(scoreFile)
    Asset = input("Enter Asset:")
    for row in csvReader:
        if row[0] == Asset:
            print(row[14])
                