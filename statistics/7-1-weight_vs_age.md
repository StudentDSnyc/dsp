[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

>> 
```
Pearson's correlation: 0.0688339703541
Spearman's correlation: 0.0946100410966
```

>>The scatter plot does not show a clear correlation between the 2 variables.  
Similarly, Pearson's correlation indicates that there is very little correlation between these variables, since the value is much closer to 0 than 1.  
Spearman's correlation, which should not be influenced by outliers or skewed distributions, is also close to 0 and reaffirms the lack of correlation.  
The plot of percentiles for birth weight and mother's age shows a non-linear relationship between the variables, especially beyond the age of 25.

![Scatter plot](https://github.com/jmfradkin/dsp/blob/master/img/Ch7Ex1_Scatter.png?raw=true)
![Percentile plot](https://github.com/jmfradkin/dsp/blob/master/img/Ch7Ex1_Percentile.png?raw=true)

```
import nsfg
import thinkplot
import numpy
import thinkstats2
import first

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
live=live.dropna(subset=['agepreg','totalwgt_lb'])
ages=live.agepreg
birthweights=live.totalwgt_lb

print 'Pearson\'s correlation: {}'.format(thinkstats2.Corr(ages,birthweights))
print 'Spearman\'s correlation: {}'.format(thinkstats2.SpearmanCorr(ages,birthweights))

thinkplot.Scatter(ages,birthweights)
thinkplot.Show(xlabel='Birth weight (lb)', ylabel='Mother age (yrs)', axis=[10,45,0,15])

df=nsfg.ReadFemPreg()
df = df.dropna(subset=['agepreg', 'totalwgt_lb'])
bins = numpy.arange(10,48,3)
indices = numpy.digitize(df.agepreg, bins)
groups = df.groupby(indices)

mother_ages=[group.agepreg.mean() for i, group in groups]
cdfs=[thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups]

for percent in [75, 50, 25]:
	weights=[cdf.Percentile(percent) for cdf in cdfs]
	label='{}th'.format(percent)
	thinkplot.Plot(mother_ages,weights,label=label)

thinkplot.Show(xlabel='Birth weight (lb)', ylabel='Mother age (yrs)', axis=[15,40,6,8.5])
```
