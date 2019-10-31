# Egyptian Fractions
Every positive fraction can be represented as sum of unique unit fractions. A fraction is unit fraction if numerator is 1 and denominator is a positive integer, for example 1/3 is a unit fraction. Such a representation is called Egyptian Fraction as it was used by ancient Egyptians.

We will use _Greedy Method_ to tackle this problem.

## Following are few examples:
- Egyptian Fraction Representation of 2/3 is 1/2 + 1/6

- Egyptian Fraction Representation of 6/14 is 1/3 + 1/11 + 1/231

- Egyptian Fraction Representation of 12/13 is 1/2 + 1/3 + 1/12 + 1/156

### Input Format
- In the first line, input will be the **Numerator** of the fraction.
  
- In the second line, input will be the **Denominator** of the fraction.



### Output Format
The Egyptian Fraction of %Numerator /%Denominator is:

The Egyptian Fraction representation of the input fraction is now printed.


### Sample Input
```
Enter the Numerator: 2
Enter the Denominator: 3
```

### Sample Output
```
The Egyptian Fraction of 2/3 is: 1/2 + 1/6
```
### Implemented in:
- [Python](egyptianfractions.py)


