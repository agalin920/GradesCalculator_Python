
def print_grades(grades):
    for x in grades:
        print x

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average
    
def grades_variance(scores):
    average=grades_average(scores);
    variance = 0;
    for x in scores:
        variance+=(average-x)**2;
    return variance/len(scores);
    
def grades_std_deviation(variance):
    return variance ** 0.5;

def isInteger(userInput):
    tmp=0;
    try:
        tmp = int(userInput)
        return True;      
    except ValueError:
        return False;



    
#MAIN

grades=[];
i=0;
x=0;

while True:
    numGrades=raw_input("How many grades are you you going to be calculating?");
    if(isInteger(numGrades)):
        numGrades=int(numGrades)
        break
    else:
        print("Invalid Input!...Please try again")
    

while(i < int(numGrades)):
    while True:
        x = raw_input("Enter Grade:")
        if(isInteger(x)):
            x=int(x)
            break       
        else:
            print("Invalid input!...Please try again")
            
            
        
    grades.append(x);
    i+=1;




variance = grades_variance(grades);

print("Grades Entered:");
print(print_grades(grades));

print("Grade Average:");
print(grades_average(grades));

print("Grade variance:")
print(grades_variance(grades));

print("Grade standard deviation:")
print(grades_std_deviation(variance));
