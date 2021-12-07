
firstName = input("Enter first name:")
lastName = input("Enter last name:")
degreeName = input("Enter degree name:")
courseworkMark = float(input("Enter coursework mark:"))
firstExamMark = float(input("Enter first exam mark:"))
secondExamMark = float(input("Enter second exam mark:"))
moduleMark = str((courseworkMark*0.6)+(firstExamMark*0.15)+(secondExamMark*0.25))


print(f"{firstName} {lastName} your total mark for {degreeName} was {moduleMark}%")

