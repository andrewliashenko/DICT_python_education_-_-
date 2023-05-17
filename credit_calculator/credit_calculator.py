import math

loan_principal = float(input("Введіть суму кредиту: "))
calculation_type = input("Оберіть, що потрібно розрахувати (monthly_payment або number_of_months): ")

if calculation_type == "monthly_payment":
    months = int(input("Введіть кількість місяців: "))
    monthly_payment = math.ceil(loan_principal / months)
    print(f"Щомісячний платіж: {monthly_payment}")
elif calculation_type == "number_of_months":
    monthly_payment = float(input("Введіть щомісячний платіж: "))
    number_of_months = math.ceil(loan_principal / monthly_payment)
    print(f"Кількість місяців: {number_of_months}")
else:
    print("Невірний тип обчислення. Будь ласка, виберіть 'monthly_payment' або 'number_of_months'.")



