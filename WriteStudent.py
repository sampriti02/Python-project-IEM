import csv  

header = ['Student ID', 'Name', 'Class Roll Number', 'Batch ID']
data = [
    ['CSE2201', 'Raima Sen', '01', 'CSE22'],
    ['CSE2101', 'Ritam Kundu', '01', 'CSE21'],
    ['ECE2201', 'Sushil Ghosh', '01', 'ECE22'],
    ['ECE2202', 'Sampriti Haldar', '02', 'ECE22']
    ]

with open('Students.csv', 'w', encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)
    # write the data
    writer.writerows(data)
    f.close()
    
with open('Students.csv', encoding="utf8") as f:
    csv_reader = csv.reader(f)
    for line_no, line in enumerate(csv_reader, 1):
        if line_no == 1:
            print('Header:')
            print(line)  # header
            print('Data:')
        else:
            print(line) 
    f.close()
    quit()
    
