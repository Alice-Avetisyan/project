class Employee:
    """This class contains information about a employee"""

    def __init__(self, theName, thePostition, theSalary, theWorkdays, theCompletedTaskNms):
        self.name = theName
        self.position = thePostition
        self.salary = theSalary
        self.workdays = theWorkdays
        self.completed_task_names = theCompletedTaskNms

    #  change position
    def changePosition(self, theChangedPosition):
        self.changed_position = theChangedPosition
        self.position = self.changed_position
    #  check if salary is higher than some threshold
    def ifHigherSalary(self, theThreshold):
        self.threshold = theThreshold
        if self.salary > self.threshold:
            print("The salary is higher than the threshold")
        else:
            print("The salary is not higher than the threshold")
            self.salary = self.threshold
    #  find if employee works on some specific weekday
    def workDays(self, theWorkdays):
        self.works_days = theWorkdays
        count = 0
        for workday in self.workdays:
            if self.works_days == workday:
                print("This employee does work on that day")
            else:
                print("This employee does not work on that day")

    def showEmployee(self):
        print("Employee name {0}; Position {1}; Salary {2}; Workdays {3}; Completed tasks: {4}".
              format(self.name, self.position, self.salary, self.workdays, self.completed_task_names))


workdays = ['Monday', 'Tuesday', 'Thursday', 'Friday', 'Saturday']
task_names = ['task1', 'task2', 'task3', 'task4']
print(len(workdays))
print("---------------Employee info---------------")
employee1 = Employee('Alex', 'Junior_Programmer', 550, workdays, task_names)
employee2 = Employee('Anna', 'Team_lead', 1500, workdays, task_names)

employee1.showEmployee()
employee2.showEmployee()

print("---------------Change position---------------")
employee1.changePosition('Mid_Programmer')

print("---------------Salary---------------")
employee2.ifHigherSalary(1501)

print("---------------Workdays---------------")
employee2.workDays('Tuesday')

