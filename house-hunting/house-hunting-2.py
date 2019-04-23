annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(
    input("Enter the percent of your salary to save, as a decimal: "))
monthly_saved = (annual_salary / 12.0) * portion_saved

total_cost = int(input("Enter the cost of your dream home: "))
portion_down_payment = total_cost * 0.25

semi_annual_raise = float(input("Enter the semi-annual salary raise: "))


current_savings = 0.0
annual_return = 0.04
number_of_months = 0

while current_savings < portion_down_payment:
    number_of_months += 1
    monthly_return = current_savings * (annual_return / 12)
    current_savings += monthly_return + monthly_saved

    if number_of_months % 6 == 0:
        monthly_increase = monthly_saved * semi_annual_raise
        monthly_saved += monthly_increase

print("Number of months:", number_of_months)
