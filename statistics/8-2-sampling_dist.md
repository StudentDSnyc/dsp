[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

>> I used the "Estimate3" function in Chapter 8 as an outline to test the performance of estimators in an exponential distribution.  

```
Standard error for n=10: 0.797933104223  
90% confidence interval for n=10: (1.27088734575, 3.67116794771)  

Standard error for n=100: 0.2027817296  
90% confidence interval for n=100: (1.71527788073, 2.35676280105)  

Standard error for n=1000: 0.0629652521264  
90% confidence interval for n=1000: (1.89779889155, 2.10260597311)  

Standard error for n=10000: 0.0202863559181  
90% confidence interval for n=10000: (1.96784260279, 2.03396346047)  
```

![Sampling distribution](https://github.com/jmfradkin/dsp/blob/master/img/Ch8Ex2_SampDist10.png?raw=true)

![Standard error vs. sample size](https://github.com/jmfradkin/dsp/blob/master/img/Ch8Ex2_StdErr.png?raw=true)

```
import numpy
import thinkstats2
import thinkplot
import math
from estimation import RMSE, MeanError

def Estimate():
	lam=2
	m=1000
	n=[10,100,1000,10000]
	std_err=[]
	for i in range(len(n)):
		L_list=[]
		for _ in range(m):
			xs=numpy.random.exponential(1.0/lam,n[i])
			L=1/numpy.mean(xs)
			L_list.append(L)
	
		cdf=thinkstats2.Cdf(L_list)
		thinkplot.Cdf(cdf)
		thinkplot.Show(xlabel='Estimate L (n={})'.format(n[i]), ylabel='CDF')
	
		print 'Standard error for n={}: {}'.format(n[i],RMSE(L_list,lam))
		print '90% confidence interval for n={}: ({}, {})'.format(n[i],cdf.Percentile(5), cdf.Percentile(95))

		std_err.append(RMSE(L_list,lam))
	
	thinkplot.Scatter(n,std_err)
	thinkplot.Show(xlabel='Sample size "n"', ylabel='Standard error', axis=[-100,10500,0,1])
	
Estimate()
```
