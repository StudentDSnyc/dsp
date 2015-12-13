# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>>*Both lists and tuples can be indexed by integers and can have values of any type. 
Lists are mutable, meaning that the entries can be reassigned in place. Tuples are immutable, so once they are created, the values cannot change. 
Tuples will work as keys in dictionaries and lists will not. This is because dictionary keys must be hashable. This property assigns hash values to store and find key-value pairs. Keys must be immutable so that the hash value will not be affected by modifying the key.*

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>>*Lists are mutable and ordered, while sets are immutable and unordered. Additionally, lists can have repeated elements, but the elements of sets must be distinct. Since lists are ordered, they support indexing and slicing. However, sets are unordered and do not allow these functions. Both lists and sets support "x in set", "len(set)", and "for x in set".
Finding an element of a set is faster than finding an element in a list. This is because sets require less memory since they are immutable and must contain distinct values.*

**Set example:**  
```
>>>set1 = {"apple", "banana", "pear"}  
>>set2 = {"orange", "apple", "peach", "pear", "plum"}  

>>>set1.union(set2)  
set(["pear", "apple", "banana", "plum", "orange", "peach"])  
```
**List example:**
```
>>>list1 = [10, 19, 1991]  
>>>list1.append(11.21)  
>>>list1  
[10, 19, 1991, 11.21]
```

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>>*Lambda creates an "anonymous function", which is a function that does not have a name and performs its task only where it is created. 
Lambda is useful for writing functions with a single expression that only need to be used in one location. 
Lambda can also be used as a part of "functional programming", meaning that lambda functions can be passed to other functions or used as return values for other functions.*

**Example 1:**
```
>>>pets = [("Fred", "rabbit", 17), ("George", "frog", 3), ("Tom", "cat", 8)]  
>>>sorted (pets, key = lambda animal: animal[2])  
[("George", "frog", 3), ("Tom", "cat", 8), ("Fred", "rabbit", 17)]  
```
**Example 2:**
```
>>>hypotenuse = lambda a,b : (a**2 + b**2)**0.5
```

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>>*List comprehensions apply simple expressions to construct lists, generally confined by a certain pattern, logic, and range.*

**List Comprehension example:**
```
>>>low_cubes = [ x**3 for x in range(5) ]
>>>low_cubes
[0, 1, 8, 27, 64]
```
**Equivalent with map:** 
```
>>>map(lambda x : x**3, [0,1,2,3,4] )
[0, 1, 8, 27, 64]
```
**Equivalent with filter:**
```
>>>cubes_list=[x**3 for x in range(11)]
>>>low_cubes = filter(lambda y: y<125, cubes_list)
>>>low_cubes
[0, 1, 8, 27, 64]
```

>>*Map() applies a function to each element of a list and returns the resulting list.  
Filter() filters the elements of a list with a filter function that returns True or False and the returned list contains the elements of the original list that evaluate True.*

**Set comprehension example:** 
```
>>low_cubes = { x**3 for x in range(5) }
>>low_cubes
set([0, 1, 8, 27, 64])
```

**Dictionary comprehension example:** 
```
>>low_cubes = {x: x**3 for x in range(5)}
>>low_cubes
{0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
```
---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> **937**

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> **513**

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> **7850**

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





