total_points = float(input("Enter the total points possible: "))  
 
points_achieved = float(input("Enter the points achieved: "))  
  
percentage = (points_achieved / total_points * 100)

if percentage >= 89:  
    grade = 'A'  
elif percentage >= 76:  
    grade = 'B'  
elif percentage >= 61:  
    grade = 'C'  
elif percentage >= 51:  
    grade = 'D'  
else:  
    grade = 'F'  
 
print("The letter grade is:", grade)  