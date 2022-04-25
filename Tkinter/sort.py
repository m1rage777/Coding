# sort() method    = used with lists
# sort() functions = used with iterables

students = (("Squidward", "F", 60), # [] массив
            ("Sandy", "A", 33),
            ('Spangebob',"D", 20),
            ("NeverMind", "A", 33),
            ('Patrick',"C", 36),
            ("Mr.Crabs", "B", 78),
            ('Incognito',"D", 99))

age = lambda ages:ages[2] # сортировка по грейдам

#students.sort(key=grade)
sorted_students = sorted(students, key=age)
for i in sorted_students:
    print(i)

