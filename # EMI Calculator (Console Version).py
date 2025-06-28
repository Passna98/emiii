# EMI Calculator (Console Version)

print("Welcome to EMI Calculator\n")

# Take user inputs
loan_amount = float(input("Enter Loan Amount (₹): "))
annual_interest_rate = float(input("Enter Annual Interest Rate (%): "))
loan_term_years = int(input("Enter Loan Term (in years): "))

# EMI Calculation
monthly_interest_rate = annual_interest_rate / 12 / 100
months = loan_term_years * 12
emi = loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** months / ((1 + monthly_interest_rate) ** months - 1)

# Show result
print(f"\nYour Monthly EMI is: ₹{emi:,.2f}")