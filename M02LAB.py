#Jules Musabe
#File name: M02Lab.py
#The app will accept student names and GPA and test to see if they made the Dean's List or 
# the Honors Roll


#set a variable to allow users to try again

TryAgain = 'Y'

#The app will run as long as the TryAgain variable is 'Y'
while TryAgain  == 'Y':
    
#Get the student's last name

    LastName = str ( input ("Please enter the student's last name: "))

#Exit if the last name is ZZZ

    if LastName != "ZZZ":
        
#Get the student's first name and GPA

        FirstName =  input ("Please enter the student's first name: ")
        StudentGPA = float(input ("Please enter the student's GPA: "))
        
#Process the GPA, print the results, and ask the user if they want to check another student

        if StudentGPA >= 3.5:
            print ("Dear ", FirstName, " ", LastName, ", congratulations! You Have made the Dean's List! ")
            TryAgain = input ("Would you like to check another student? (Y/N) ")
            
        elif StudentGPA >= 3.25:
            print ("Dear ", FirstName, " ", LastName, ", congratulations! You Have made the Honor Roll! ")
            TryAgain = input ("Would you like to check another student? (Y/N) ")
            
        else:
            print ("Dear ", FirstName, " ", LastName, ", keep working hard. You haven't made Dean's List or the Honor Roll.")
            TryAgain = input ("Would you like to check another student? (Y/N) ")
 
 #inform the user that they quit the process and ask them if they want to start over.
    
    else:
        print ("You aborted the process.")
        TryAgain = input ("Would you like to start over? (Y/N) ")
