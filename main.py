#int
year = 2020
birthDay = 1985
month = 3
print(year, type(year), birthDay, type(birthDay), month, type(month))

#float
pi = 3.1415
radius = 18.0
deep = 100.452
print(pi, type(pi), radius, type(radius), deep, type(deep))

#string
name = 'Alexander'
country = 'Russia'
monthStr = 'march'
print(name, type(name), country, type(country), monthStr,type(monthStr))

#list
alphabetEng = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
arabicNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
allLists = [alphabetEng, arabicNumber]
print(alphabetEng, type(alphabetEng))
print(arabicNumber, type(arabicNumber))
print(allLists, type(allLists))

#dict
user = {
    'name': 'userName',
    'lastname': 'lastUserName'
}

century = {
    'year': 100,
    'day': 36500,
}

car = {
    'model': 'mazda',
    'turbo': 'true',
    'year': year,
    'wheelRadius': radius,
    'driver': user
}
print(user, type(user))
print(century, type(century))
print(car, type(car))

#tuple
yearTime = (4, 'winter', 'spring', 'summer', 'autumn')
monthWeek = (1, 2, 3, 4)
part = ('one', 'eleven', 'thousand', 33)
print(yearTime, type(yearTime))
print(monthWeek, type(monthWeek))
print(part, type(part))

#set
orderNumber = {9, 4, 2, 6, 1, 7, 3}
orderSet = {'c', 33, 41, 2, 0}
strangeSets = {yearTime, monthWeek}
print(orderNumber, type(orderNumber))
print(orderSet, type(orderSet))
print(strangeSets, type(strangeSets))

#bool
lieStatus = True
booleanType = True
stats = False
print(lieStatus, type(lieStatus), booleanType, type(booleanType), stats, type(stats))

#actions
todayYear = year - birthDay
zero = 35 - todayYear
print(todayYear)
print(zero)

trueTest = lieStatus + stats
listTest = alphabetEng + arabicNumber
print(trueTest)
print(listTest)

statePi = pi ** radius
zeroYear = zero ** year
print(statePi)
print(zeroYear)

divYear = year / birthDay
zeroDiv = divYear / deep
print(divYear)
print(zeroDiv)