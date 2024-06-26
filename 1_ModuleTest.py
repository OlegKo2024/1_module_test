grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Список grades содержит списки оценок для каждого ученика в алфавитном порядке
# Множество students содержит неупорядоченную последовательность имён всех учеников в классе
# Напишите программу, которая составляет словарь, используя grades и students, где ключом будет имя ученика,
# а значением - его средний балл. Пример: {'Aaron': 4.0, 'Bilbo': 2.25, 'Johhny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}

av_grades=((sum(grades[0]))/len(grades[0]), (sum(grades[1]))/len(grades[1]), (sum(grades[2]))/len(grades[2]),
           (sum(grades[3]))/len(grades[3]), (sum(grades[4]))/len(grades[0]))
print(av_grades)

list_students=(list(students))
print(list_students)
list_students.sort()
print(list_students)

st_dict={list_students[0]:av_grades[0],list_students[1]:av_grades[1],list_students[2]:av_grades[2],
         list_students[3]:av_grades[3],list_students[4]:av_grades[4]}
print(st_dict)