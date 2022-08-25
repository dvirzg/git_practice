import csv
import os

# can then add speaker, date, location to file and also add transcript, audio, video, picture once all is set up.
with open("C:/Users/dvirz/Desktop/Speeches & Essays/Lists/Top_20thCen_csv.csv", 'r') as file:
    database = csv.reader(file)
    for row in database:
        try:
            newpath = r"C:/Users/dvirz/Desktop/Speeches & Essays/Titles/" + row[0] 
            if not os.path.exists(newpath):
                os.makedirs(newpath)
        except (NotADirectoryError, OSError):
            print("didnt work: " + row[0])
            pass