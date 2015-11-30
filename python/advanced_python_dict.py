import csv
from pprint import pprint
from collections import OrderedDict

f=open('faculty.csv')
csv_f = csv.reader(f)

name=[]
last_name=[]
first_name=[]
full_title=[]
degree=[]
email=[]
faculty_dict={}
professor_dict={}

for row in csv_f:
	name.append(row[0])
	full_title.append(row[2])
	degree.append(row[1]) 
	email.append(row[3])

degree=degree[1:]
full_title=full_title[1:]
email=email[1:]

title=[]
for item in full_title:
	title.append(item[0:item.index('Professor')+9])
	
name=name[1:]
for full_name in name:
	full_name=full_name.split()
	last_name.append(full_name[len(full_name)-1])
	if len(full_name)>2:
		first_name.append((' ').join(full_name[0:len(full_name)-1]))
	else:
		first_name.append(full_name[0])

indices=[]
for last in last_name:
	faculty_dict.setdefault(last,[])
	first=first_name[last_name.index(last)]
	professor_dict.setdefault((first,last),[])
	if last_name.count(last)>1:
		index=[i for i, x in enumerate(last_name) if x==last]
		if index not in indices:
			indices.append(index)
			for entry in index:
				faculty_dict[last].append([degree[entry],title[entry],email[entry]])
				professor_dict[(first,last)].append([degree[entry],title[entry],email[entry]])
	else:
		last_idx=last_name.index(last)
		faculty_dict[last].append([degree[last_idx],title[last_idx],email[last_idx]])
		professor_dict[(first,last)].append([degree[last_idx],title[last_idx],email[last_idx]])
		
pprint (faculty_dict)

print '_'*50

pprint (professor_dict)

print '_'*50

items_sorted = (sorted(professor_dict.items(), key=lambda x: x[0][1]))
print '_'*50

pprint (items_sorted)
	
	

	


