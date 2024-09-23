grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students=sorted(students)
grades1 = [5, 3, 3, 5, 4]
grades1 = sum(grades1)/len(grades1)
grades2 =[2, 2, 2, 3]
grades2= sum(grades2)/len(grades2)
grades3 = [4, 5, 5, 2]
grades3=  sum(grades3)/len(grades3)
grades4 = [4, 4, 3]
grades4=  sum(grades4)/len(grades4)
grades5 = [5, 5, 5, 4, 5]
grades5=  sum(grades5)/len(grades5)
grades= (grades1,grades2,grades3,grades4,grades5)
dict= {students[0]:grades[0],students[1]:grades[1],students[2]:grades[2],students[3]:grades[3],students[4]:grades[4],}
print (dict)