import csv

f=open('football.csv')
csv_f = csv.reader(f)

teams=[]
goals=[]
allowed=[]
difference=[]

for row in csv_f:
	teams.append(row[0])
	goals.append(row[5])
	allowed.append(row[6])

for i in range(1,len(goals)):
	difference.append(abs(int(goals[i])-int(allowed[i])))
	
idx=difference.index(min(difference))
print teams[idx+1]


