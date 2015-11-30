import csv

email=[]

c=csv.writer(open("emails.csv","wb"), dialect='excel')
f=open('faculty.csv')
csv_f = csv.reader(f)

for row in csv_f: 
	email.append(row[3])

email=email[1:]

for i in range(len(email)):
	c.writerow([email[i]])
