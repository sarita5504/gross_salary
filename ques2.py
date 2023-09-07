# Function to calculate gross salary
def calculate_gross_salary(basic, grade):
    hra = 0.20 * basic
    da = 0.50 * basic
    
    if grade == 'A':
        allowance = 1700
    elif grade == 'B':
        allowance = 1500
    else:
        allowance = 1300
    
    pf = 0.11 * basic
    
    gross_salary = basic + hra + da + allowance - pf
    return gross_salary

# Test cases
basic_A = int(input("Enter basic pay : "))
grade_A = str(input("Enter grades : "))
gross_salary_A = calculate_gross_salary(basic_A, grade_A)
print(f"Gross Salary for grade A: {gross_salary_A}")

basic_B = 4567
grade_B = 'B'
gross_salary_B = calculate_gross_salary(basic_B, grade_B)
print(f"Gross Salary for grade B: {gross_salary_B}")
	

