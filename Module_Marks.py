Coursework = int(input('Enter your coursework mark:'))
Exam = int(input('Enter your combined in-class test and exam mark:'))

if Coursework >= 35 and Exam >= 35 and ((Coursework+Exam)/2) >= 40:
    print ('You have passed the module')
else:
    print ('Fail')