import math

def calculate_monthly_payment(principal, interest_rate, months):
    interest_rate_per_month = interest_rate / 12 / 100
    monthly_payment = (principal * interest_rate_per_month) / (1 - math.pow(1 + interest_rate_per_month, -months))
    return monthly_payment

def calculate_number_of_months(principal, interest_rate, monthly_payment):
    interest_rate_per_month = interest_rate / 12 / 100
    number_of_months = -math.log(1 - (principal * interest_rate_per_month) / monthly_payment) / math.log(1 + interest_rate_per_month)
    return math.ceil(number_of_months)

def calculate_loan_principal(monthly_payment, interest_rate, months):
    interest_rate_per_month = interest_rate / 12 / 100
    loan_principal = monthly_payment * (1 - math.pow(1 + interest_rate_per_month, -months)) / interest_rate_per_month
    return loan_principal

def round_value(value):
    rounded_value = round(value, 2)
    return rounded_value

print("Вітаю у кредитному калькуляторі!")
principal = float(input("Введіть суму кредиту: "))
interest_rate = float(input("Введіть річну процентну ставку (%): "))

calculation_type = input("Що бажаєте розрахувати (monthly_payment, number_of_months, loan_principal): ")

if calculation_type == "monthly_payment":
    months = int(input("Введіть кількість місяців: "))
    monthly_payment = calculate_monthly_payment(principal, interest_rate, months)
    print(f"Щомісячний платіж: {round_value(monthly_payment)}")
elif calculation_type == "number_of_months":
    monthly_payment = float(input("Введіть щомісячний платіж: "))
    number_of_months = calculate_number_of_months(principal, interest_rate, monthly_payment)
    print(f"Кількість місяців: {number_of_months}")
elif calculation_type == "loan_principal":
    monthly_payment = float(input("Введіть щомісячний платіж: "))
    months = int(input("Введіть кількість місяців: "))
    loan_principal = calculate_loan_principal(monthly_payment, interest_rate, months)
    print(f"Основна сума кредиту: {round_value(loan_principal)}")
else:
    print("Невірний тип обчислення. Будь ласка, виберіть monthly_payment, number_of_months або loan_principal.")
