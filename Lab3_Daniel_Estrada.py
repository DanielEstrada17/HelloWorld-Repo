income = float(input("Enter your earned income: "))
marital_status = input("Enter your marital status (single/married): ").lower()

if marital_status == "single":
    if income <= 11000:
        tax_owed = income * 0.10
    elif income <= 44725:
        tax_owed = 11000 * 0.10 + (income - 11000) * 0.12
    elif income <= 95375:
        tax_owed = 11000 * 0.10 + (44725 - 11000) * 0.12 + (income - 44725) * 0.22
    else:
        print("You made too much for this calculator. Hooray!")
        exit()

elif marital_status == "married":
    if income <= 22000:
        tax_owed = income * 0.10
    elif income <= 89450:
        tax_owed = 22000 * 0.10 + (income - 22000) * 0.12
    elif income <= 190750:
        tax_owed = 22000 * 0.10 + (89450 - 22000) * 0.12 + (income - 89450) * 0.22
    else:
        print("Income exceeds calculator range for married filers.")
        exit()

else:
    print("You made too much for  this calculator. Hooray!")
    exit()

print(f"Tax owed: ${tax_owed:.2f}")

