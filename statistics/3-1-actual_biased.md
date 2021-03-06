[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

I used the code outlined in Chapter 3 to create the distributions, calculate means, and plot PMFs.

Actual PMF:  
0: 0.46617820227659301  
1: 0.21405207379301322  
2: 0.19625801386889966  
3: 0.087138558157791451  
4: 0.025644380478869556  
5: 0.010728771424833181  

**Actual distribution mean: 1.0242051550438309**

Biased PMF:  
0: 0.0  
1: 0.20899335717935616  
2: 0.38323965252938175  
3: 0.25523760858456823  
4: 0.10015329586101177  
5: 0.052376085845682166

**Biased distribution mean: 2.4036791006642821**

![PMF plot](https://github.com/jmfradkin/dsp/blob/master/img/Ch3Ex1_PMF.png?raw=true)

```
import nsfg
import thinkstats2
import chap01soln
import thinkplot

resp = chap01soln.ReadFemResp()
pmf=thinkstats2.Pmf(resp.numkdhh,label='Actual')

def BiasPmf(pmf,label):
	new_pmf=pmf.Copy(label=label)
	
	for x,p in pmf.Items():
		new_pmf.Mult(x,x)
	
	new_pmf.Normalize()
	return new_pmf

biased_pmf = BiasPmf(pmf,label='Biased')
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf,biased_pmf])
thinkplot.Show(xlabel='Number of Children in Household', ylabel='PMF')

print ('Actual PMF',pmf)
print ('Biased PMF',biased_pmf)


print ('Actual distribution mean',pmf.Mean())
print ('Biased distribution mean',biased_pmf.Mean())
```
