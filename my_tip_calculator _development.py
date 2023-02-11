'''
This is my tip calculator to divide tip and
 the whole bill between group of people.
 '''
print("Welcome to my Tip calculator!")

''' 
I am using var to store the output and 
input function to take and also using float function
'''
bill = float(input("What was the total bill without tip? $"))
tip = int(input("How much you would like to tip? 5, 10, 15 :"))
group_of_people = int(input("How many people would like to split the bill?"))
total_bill = bill + tip
bill_per_person = total_bill / group_of_people
#Using round function to round the bill in two decimal
final_amount = round(bill_per_person, 2)
print(f"Every person has to pay: ${final_amount}")


