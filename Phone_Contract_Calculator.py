monthlyContractFee = float(input("Monthly contract fee: £"))

monthlyAllowanceMinutes = float(input("Total monthly allowance of minutes: "))
totalUsedMinutes = float(input("Minutes used during month: "))
overAllowanceFeePerMinute = float(input("Fee per minute over allowance (pence): "))

totalMonthlyFee = float((totalUsedMinutes-monthlyAllowanceMinutes)*overAllowanceFeePerMinute)

monthlyAllowanceData = float(input("Total monthly allowance of Data (Mb): "))
totalUsedData = float(input("Data used during month (Mb): "))
overAllowanceFeePerMb = float(input("Fee per Mb over allowance (pence): "))

totalMonthlyDataFee = float((totalUsedData-monthlyAllowanceData)*overAllowanceFeePerMb)

totalMonthlyBill = (totalMonthlyFee/100) ++ (totalMonthlyDataFee/100) ++ monthlyContractFee

if totalMonthlyFee <= 0 and totalMonthlyDataFee <= 0:
    str(print(f"No additional charges, your total bill is £{monthlyContractFee}"))

if totalMonthlyFee <= 0 and totalMonthlyDataFee >0:
    totalMonthlyBill = (totalMonthlyDataFee/100) ++ monthlyContractFee
    str(print(f"Your total bill is £{totalMonthlyBill}"))

if totalMonthlyDataFee <= 0 and totalMonthlyFee >0:
    totalMonthlyBill = (totalMonthlyFee/100) ++ monthlyContractFee
    str(print(f"Your total bill is £{totalMonthlyBill}"))

if totalMonthlyFee > 0 and totalMonthlyDataFee > 0:
    str(print(f"Your total bill is £{totalMonthlyBill}"))

