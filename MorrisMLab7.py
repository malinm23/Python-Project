# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 15:30:17 2023

@author: mjm10
"""

print("Part A:")
print()

def lettergrade(totalAverage):
    if totalAverage >= 90:
        lettergrade = 'A'
    if totalAverage >= 80:
        lettergrade = 'B'
    if totalAverage >= 70:
        lettergrade = 'C'
    if totalAverage >= 60:
        lettergrade = 'D'
    if totalAverage >= 59:
        lettergrade = 'F'
        return lettergrade
    
Grades = {
    'Joe':[56,89,91],
    'Amanda':[88,45,99],
    'Jim':[88,99,87],
    'Mitchell':[75,88,70],
    }

for name, grades in Grades.items():
    lettergrades = lettergrade(sum(grades)/len(grades))
    print(f"Average for {name} is {sum(grades)/len(grades):.2f} with a letter grade of {lettergrades}")
    
print()

####ASSIGNMENT B
print("Part B:")
print()

print("First set of comparisons: (colors)")
colorset1 = {'red','green','blue'}
colorset2 = {'cyan','green','blue','magenta','red'}

print("First set of colors: ", colorset1)
print("Second set of colors: ", colorset2)
print()

print("Less than:", colorset1 < colorset2)
print("Less than or equal to:", colorset1 <= colorset2)
print("Greater than:", colorset1 > colorset2)
print("Greater than or equal to:", colorset1 >= colorset2)
print("Equal to:", colorset1 == colorset2)
print("Not equal to:", colorset1 != colorset2)
print("Union operator:", colorset1 | colorset2)
print("Difference operator:", colorset1 - colorset2)
print("Symmetric Difference operator:", colorset1 ^ colorset2)
print("Disjoint operator:", (colorset1).isdisjoint(colorset2))


print()
print("Second set of comparisons: (Numbers)")
numberset1 = {1,3,5,6}
numberset2 = {2,4,5,6}

print("First set of numbers: ", numberset1)
print("Second set of numbers: ", numberset2)
print()

print("Less than:", numberset1 < numberset2)
print("Less than or equal to:", numberset1 <= numberset2)
print("Greater than:", numberset1 > numberset2)
print("Greater than or equal to:", numberset1 >= numberset2)
print("Equal to:", numberset1 == numberset2)
print("Not equal to:", numberset1 != numberset2)
print("Union operator:", numberset1 | numberset2)
print("Difference operator:", numberset1 - numberset2)
print("Symmetric Difference operator:", numberset1 ^ numberset2)
print("Disjoint operator:", (numberset1).isdisjoint(numberset2))
      
      