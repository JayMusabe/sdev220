
TryAgain = 'Y'

while TryAgain  == 'Y':
    LastName = str ( input ("Please enter the student's last name: "))
    if LastName != "ZZZ":
        FirstName =  input ("Please enter the student's first name: ")
        StudentGPA = float(input ("Please enter the student's GPA: "))
        if StudentGPA >= 3.5:
            print ("Dear ", FirstName, " ", LastName, ", congratulations! You Have made the Dean's List! ")
            TryAgain = input ("Would you like to check another student? (Y/N) ")
            
        elif StudentGPA >= 3.25:
            print ("Dear ", FirstName, " ", LastName, ", congratulations! You Have made the Honor Roll! ")
            TryAgain = input ("Would you like to check another student? (Y/N) ")
            
        else:
            print ("Dear ", FirstName, " ", LastName, ", keep working hard. You haven't made Dean's List or the Honor Roll.")
            TryAgain = input ("Would you like to check another student? (Y/N) ")
    
    else:
        print ("Invalid input")
        TryAgain = input ("Would you like to check another student? (Y/N) ")
