import csv

f=open('faculty.csv')
csv_f = csv.reader(f)

degree=[]
full_title=[]
email=[]
domain_list=[]

for row in csv_f: 
	full_title.append(row[2])
	email.append(row[3])
	degree=degree+row[1].replace('.','').split()

#Q1:
degree=degree[1:]
degree_set=set(degree)
print "Number of different degrees: {} \n".format(len(degree_set))

for i in degree_set:
  if i.isalpha():
  	print "{}: {} \n".format(i,degree.count(i))
print '_'*50

#Q2:
full_title=full_title[1:]
title=[]
for item in full_title:
	title.append(item[0:item.index('Professor')+9])

title_set=set(title)
print "Number of different titles: {} \n".format(len(title_set))

for i in title_set:
  print "{}: {} \n".format(i,title.count(i)) 
print '_'*50

#Q3:
email=email[1:]
print "Email list: {} \n".format(email)
print '_'*50

#Q4:
for i in range(len(email)):
  domain=email[i][email[i].index('@')+1:]
  if domain not in domain_list:
    domain_list.append(domain)

print "Unique domains: {} \n".format(len(domain_list))
print domain_list
