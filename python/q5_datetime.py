# Hint:  use Google to find python function

####a) 

from datetime import datetime 

date_start=datetime.strptime('01-02-2013', '%m-%d-%Y')
date_stop=datetime.strptime('07-28-2015', '%m-%d-%Y')
difference=date_stop-date_start

print difference.days
   

####b)  

from datetime import datetime

date_start=datetime.strptime('12312013', '%m%d%Y')
date_stop=datetime.strptime('05282015', '%m%d%Y')
difference=date_stop-date_start

print difference.days  

####c)  

from datetime import datetime

date_start=datetime.strptime('15-Jan-1994', '%d-%b-%Y')
date_stop=datetime.strptime('14-Jul-2015', '%d-%b-%Y')
difference=date_stop-date_start
print difference.days
