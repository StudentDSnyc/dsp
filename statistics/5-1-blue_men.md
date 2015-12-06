[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

I used scipy.stats.norm.cdf to determine the percentage of the US male population with heights between 5'10" and 6'1":  
**34.2%**

```
import scipy.stats

mu=178
sigma=7.7
range_low=177.8
range_high=185.4

print "Percentage between 177.8cm-185.42cm: {}".format(scipy.stats.norm.cdf(range_high,loc=mu,scale=sigma)-scipy.stats.norm.cdf(range_low,loc=mu,scale=sigma))

```
