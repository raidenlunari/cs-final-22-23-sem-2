class summerSchool:

    #default constructor
    def __init__(self):
        self.week = 0
        self.day = 0
        self.classInput = 0
        self.attendance = False

    #constructor with var
    def setStudent(self, week, day, classInput, attendance):
        self.week = week
        self.day = day
        self.classInput = classInput
        self.attendance = attendance

    def getWeek(self):
        return self.week

    def setWeek(self, week):
        self.week = week

    def getDay(self):
        return self.day

    def setDay(self, day):
        self.day = day

    def getClass(self):
        return self.classInput

    def setClass(self, classInput):
        self.classInput = classInput

def main():
    list = []
    access = 0
    repeat = True
    for i in range(5):
        list.append(summerSchool)
    while repeat:
        inputStudent = int(input("What student would you like to access [1-5]: "))
        list[inputStudent].getWeek()
        list[inputStudent].getDay()
        list[inputStudent].getClass()


