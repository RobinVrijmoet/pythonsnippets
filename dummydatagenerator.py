from random import randint
from datetime import *

weeknumbers = 52
bookingsperweek = 10
year = 2018
classrooms = ["WD.1.016","WD.1.003","WD.1.019","H.2.318","H.3.403","H.3.306","H.4.308","H.4.312","WD.1.022","WN.1.014"]
lessons = ["SEN01","SEN02","ICTLAB","INFAN02","INFAN03","INF04","DSN01","SLC04","SCRT02","ATM3","ETC3","ADHD","FIFA","WOW2","COD3","LoLGG"]
usernames = ["GIACF","COSTG","SCHMN","BUSAL","ABBAM","SALMG","MUILL","OMAR"]
reservationid= 1;
# dates = ["02-01-2018-"]
def dayslotsunbooked():
    return {1:False,2:False,3:False,4:False,5:False,6:False,7:False,8:False,9:False,10:False,11:False,12:False,13:False,14:False,15:False}

def GenerateWeekSchedule():
    return {1:dayslotsunbooked(),2:dayslotsunbooked(),3:dayslotsunbooked(),4:dayslotsunbooked(),5:dayslotsunbooked()}

def GenerateWeekly():
    return GenerateWeekSchedule()


timeslots = {
    1:(time(8,30,00),time(9,20,00)),
    2:(time(9,20,00),time(10,10,00)),
    3:(time(10,30,00),time(11,20,00)),
    4:(time(11,20,00),time(12,10,00)),
    5:(time(12,10,00),time(13,00,00)),
    6:(time(13,00,00),time(13,50,00)),
    7:(time(13,50,00),time(14,40,00)),
    8:(time(15,00,00),time(15,50,00)),
    9:(time(15,50,00),time(16,40,00)),
    10:(time(17,00,00),time(17,50,00)),
    11:(time(17,50,00),time(18,40,00)),
    12:(time(18,40,00),time(19,30,00)),
    13:(time(19,30,00),time(20,20,00)),
    14:(time(20,20,00),time(21,10,00)),
    15:(time(21,10,00),time(22,00,00)),
}


class classroom():
    def __init__(self, inputname):
        self.classname = inputname
        self.schedule = GenerateWeekSchedule()

classobjects = []

for f in classrooms:
    classobjects.insert(len(classobjects),classroom(f))


sql = "INSERT INTO [TABLENAME] (reservationid,timeslotfrom,timeslotto,timefrom,timeto,date,username,lesson,room,weeknummer) VALUES "
currentweek = 1
currentiteration = 1
first = True;
while currentweek <= weeknumbers:

    while currentiteration != bookingsperweek:
        room = classobjects[randint(0,len(classobjects)-1)]
        randomtimeslot = randint(1,15)
        randomday = randint(1,5)
        if(not room.schedule[randomday][randomtimeslot]):
            randomteacher = usernames[randint(0,len(usernames)-1)]
            randomlesson = lessons[randint(0,len(lessons)-1)]

            d = str(year)+"-W"+str(currentweek)
            date = datetime.strptime(d + '-0', "%Y-W%W-%w").strftime('%Y-%m-%d')

            if(not first):
                sql += ","
            else:
                first = False

            room.schedule[randomday][randomtimeslot] = True
            sql += "(" + str(reservationid) + "," + str(randomtimeslot) + "," + str(randomtimeslot) + ",'" + \
                   str((timeslots[randomtimeslot][0])) +"','" + str((timeslots[randomtimeslot][1])) +"','" + str(date) +"','" + randomteacher +"','" + randomlesson +"','" + room.classname +"'," + str(currentweek) +")"
            currentiteration += 1
            reservationid += 1

    currentiteration = 1
    currentweek += 1


print(sql)