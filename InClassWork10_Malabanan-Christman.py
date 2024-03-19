CREDIT_MAX = 20

class Student:
    def __init__(self,Name,Age,Courses_Taken=[],Current_Classes=[]):
        self.Name = Name #Initializes all variables
        self.Age = Age
        self.Major = ""
        self.Courses = Courses_Taken
        self.current = Current_Classes
    def Toprint(self):
        print("Student information:", self.Name, self.Age, self.Major) #Shows the info about the student
    def addCourse(self,course):
        if course not in self.Courses(): #If the course isn't already in the list of their taken courses
            self.Courses.append(course) #Adds a course to the student's taken classes (this does not enroll the student in the actual course)
            print("Class added to previously taken courses.")
        else:
            print("Error: Class already in previously taken courses.")
    def drop(self,course):
        if course in self.current:
            self.current.remove(course.Name) #Removes a course from the student's current classes
            course.enrollment.remove(self.Name) #Removes the student from the course's enrollment
            print("Class dropped.")
        else:
            print("Error: Student not taking class.") #If they try to drop a class they aren't in
    def enroll(self,course):
        if course.add_student(self): #Tries to add the student to the course, and if successful, will see true
            self.current.append(course) #Adds the class to the student's current classes
            print("Enrolled in class.")
        else:
            print("Error: One or more prerequisites not met.")
    def currentcredits(self):
        sum = 0
        for i in self.Current_Classes:
            sum += i.Credits
        return sum
    def currenttimes(self):
        tor = [[],[],[],[],[]] #Creates an empty list of lists for each day of the week
        for i in range(0,len(self.Current_Classes)): #For each current class
            for j in range(0,6): #For each day
                if len(self.Current_Classes[i][j]) > 0: #If the class meets this day
                    tor[i].append(self.Current_Classes[i][j]) #Adds the class times to the student's current times
        return tor #Returns the two dimensional list
            
class EEMajor(Student):
    def __init__(self,Name,Age,Courses_Taken=[],Current_Classes=[]):
        super.__init__(self,Name,Age,Courses_Taken=[],Current_Classes=[])
        self.Major = "EE"

class CHMEMajor(Student):
    def __init__(self, Name, Age, Courses_Taken=[],Current_Classes=[]):
        super.__init__(self, Name, Age, Courses_Taken=[],Current_Classes=[])
        self.Major = "CHME"
    
class CIVEMajor(Student):
    def __init__(self, Name, Age, Courses_Taken=[],Current_Classes=[]):
        super.__init__(self, Name, Age, Courses_Taken=[],Current_Classes=[])
        self.Major = "CIVE"
    
class ENVMajor(Student):
    def __init__(self, Name, Age, Courses_Taken=[],Current_Classes=[])
        super.__init__(self, Name, Age, Courses_Taken=[],Current_Classes=[])
        self.Major = "ENV"
    
class CEMajor(Student):
    def __init__(self, Name, Age, Courses_Taken=[],Current_Classes=[])
        super.__init__(self, Name, Age, Courses_Taken=[],Current_Classes=[])
        self.Major = "CE"

class CSMajor(Student):
    def __init__(self, Name, Age, Courses_Taken=[],Current_Classes=[]):
        super.__init__(self, Name, Age, Courses_Taken=[],Current_Classes=[])
        self.Major = "CS"

class PHYSMajor(Student):
    def __init__(self, Name, Age, Courses_Taken=[],Current_Classes=[]):
        super.__init__(self, Name, Age, Courses_Taken=[],Current_Classes=[])
        self.Major = "PHYS"
        
class Course:
    def __init__(self,Name,Code,Prerequisites,Max,Credits,enrollment=[],times=[[],[],[],[],[]]): #Times is a list of lists representing the start and end times for each day. For example, a course meating MWR 1:00 pm to 2:30 pm would be [[13,14.3],[],[13,14.3],[13,14.3],[]]
        self.Name = Name #Initializes all variables
        self.Code = Code
        self.enrollment = enrollment
        self.Prereqs = Prerequisites
        self.Max = Max
        self.times = times
        self.Credits = Credits
    def add_student(self,student):
        toApply = True #All the requirements are currently met
        if student.currentcredits() + self.Credits > CREDIT_MAX:
            toApply=False
        for i in self.Prereqs:  
            if i not in student.Courses: #If the student hasn't taken a prereq
                toApply = False #The requirements are no longer met
        if toApply and len(self.enrollment) < self.Max: #If the requirements are met and the class isn't full
            self.enrollment.append(student) #Adds the student to the current enrollment
            student.current.append(self) #Adds the course to the student's current classes
            return True #Communicates that the student was successfully added
    def toPrint(self):
        print(self.enrollment) #Prints the enrollment of the class
    def add_prereq(self,toAdd):
        if toAdd not in self.Prereqs:
            self.Prereqs.append(toAdd) #Adds a prerequisite
            print("Prerequisite added.")
        else:
            print("Error: Prerequisite already in course")
    def check_time_conflict(self,student):
        studentlist = student.currenttimes()
        for i in range(0,len(self.times)): #For each day in the week:
            for j in studentlist[i]: #For each class the student has this day:
                if self.times[i][0] < i[1] or self.times[i][1] > i[0]: #If the current class starts before the student's class ends or ends after the student's class starts
                    return True #Returns that there is a time conflict
        return False #There is no conflict

class EECE2150(Course):
    def __init__(self, Prerequisites):
        super.__init__(self,Prerequisites)
    def prereqs(self):
        self.Prerequisites = ["GE1111"] + ["MATH2341"] + ["PHYS1165"] + ["EECE2140"]

class EECE2520(Course):
    def __init__(self, Prerequisites):
        super.__init__(self,Prerequisites)
    def prereqs(self):
        self.Prerequisites = ["EECE2150"] + ["MATH2341"]

class EECE2530(Course):
    def __init__(self, Prerequisites):
        super.__init__(self,Prerequisites)
    def prereqs(self):
        self.Prerequisites = ["EECE2150"] + ["MATH2341"] + ["PHYS1165"]
    
class EECE2531(Course):
    def __init__(self, Prerequisites):
        super.__init__(self,Prerequisites)
    def prereqs(self):
        self.Prerequisites = ["EECE2150"] + ["MATH2341"] + ["PHYS1165"]
    
class EECE2540(Course):
    def __init__(self, Prerequisites):
        super.__init__(self,Prerequisites)
    def prereqs(self):
        self.Prerequisites = ["EECE2140"]
