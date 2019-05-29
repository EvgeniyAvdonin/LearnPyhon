#some_figures =[1,2,3,4,5,6,7,8,9,10]
#or figures in some_figures:
    #print(figures+1)

#some_letters = ['H','O','L','A','!']
#for letters in some_letters:
    #print(letters)


students_marks = [
    {'school_class': '4a', 'scores': [3,4,4,5,2]},
    {'school_class': '4b', 'scores': [5,4,4,2,2]},
    {'school_class': '4v', 'scores': [2,3,4,4,3]},
]
for index in range(len(students_marks)):
    #print(index)
    #print(students_marks[index])
    print(students_marks[index]['scores'])
    print(sum(students_marks[index]['scores'])/len(students_marks[index]['scores']))




#for school_class in students_marks:
# average = sum(students_marks['scores'])/len(students_marks['scores'])