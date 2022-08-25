import csv
import os

# can then add speaker, date, location to file and also add transcript, audio, video, picture once all is set up.
with open("C:/Users/dvirz/Desktop/Speeches & Essays/Lists/unclean_list.csv", 'r') as file:
    database = csv.reader(file)
    with open("cleaned_20th.csv", 'w') as clean_file:
        csvwriter = csv.writer(clean_file)  
        for row in database:
            for actual_row in row:
                x = actual_row.find("by")
                date = actual_row[0:4]
                title = actual_row[6:x]
                speaker = actual_row[x+3:]
            #print("date: " + date + "\n" + "title: " + title.replace(".", "") + "\n" + "speaker: " + speaker.replace(".", "") + "\n---------------")
            i = [date, title, speaker]               
            csvwriter.writerow(i)
    print("Done!")

# changes done in first_branch