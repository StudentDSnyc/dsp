[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>>I used Downey's nsfg.py file to read the pregnancy data and the CohenEffectSize() method referenced in Chapter 2 to complete this exercise.  
>>Cohen's d for totalwgt_lb between first babies and others is -0.0887 standard deviations, indicating that first babies are lighter than others.  
>>Conversely, Cohen's d for prglngth between first babies and others is 0.0289, indicating that the length of pregnancy is longer for first babies than others. 

```
import nsfg
import math

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]

firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

def CohenEffectSize(group1,group2):
    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return round(d,4)

print "\nCohen's D for Total Weight between first babies and others: {}".format(CohenEffectSize(firsts.totalwgt_lb,others.totalwgt_lb))
print "Cohen's D for Pregnancy Length between first babies and others: {}".format(CohenEffectSize(firsts.prglngth, others.prglngth))
```

