salary = int(input("Enter the employee's annual salary: "))

if salary <= 20000:
    bonus = salary * 5 / 100

elif salary > 20000 and salary <= 40000:
    bonus = salary * 10 / 100

else:
    bonus = salary * 15 / 100

print("Employee's annual salary:", salary)
print("Bonus:", bonus)
print("Total salary:", salary + bonus)