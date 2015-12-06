[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

After creating the list of 1000 random values between 0 and 1, I used the code from the Chapter 3 exercise to create the PMF and a similar structure to create the CDF.  

The PMF shows that the distribution is uniform, since each random value corresponds to a probability of approximately 1/1000. Similarly, the CDF shows a uniform distribution, as evidenced by the straight line in the plot.

```
import random
import thinkplot
import thinkstats2

numlist=[]
for i in range(0,1000):
	numlist.append(random.random())

pmf=thinkstats2.Pmf(numlist)
thinkplot.Pmf(pmf,linewidth=0.1)
thinkplot.Show(xlabel='Random values', ylabel='PMF')

cdf=thinkstats2.Cdf(numlist)
thinkplot.Cdf(cdf)
thinkplot.Show(xlabel='Random values',ylabel='CDF')
```
