class Student:
    def __init__ (my,name,matricule,dept,):
        my.name=name
        my.matricule=matricule
        my.dept=dept
        my.courses=['math','physics','chemistry']
    

    def addCourses (my,*courses):
            my.courses.append(courses)

    def displayCourses (my):
                print(my.coruses) 
                for course in (my.courses):
                    print(course)

    def delCourses(my,courseindex):
        my.courses.remove.courseindex


c1= Student ('hubert','uba24ph001','CEN',)
c2= Student ('pride','uba24ph001','CEN',)
c1.courses.append('biology')


                    