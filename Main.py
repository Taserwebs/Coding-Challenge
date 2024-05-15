from Entity import Loans
from DAO import LoanRepository
def mainmenu():
    print("1. Apply loan")
    print("2. Calculate Interest")
    print("3. calculate Emi")
    print("4. loanRepayment")
    print("5. getAllLoan")
    print("6. getLoanByID")
    print("7. getLoanStatus")
    print("8. Exit")
while True:
    mainmenu()
    choice=int(input("Enter your choice: "))
    if choice==1:
        loanID = input("Enter Loan ID: ")
        customerID = input("Enter Customer ID: ")
        principalAmount = float(input("Enter Principal Amount: "))
        interestRate = float(input("Enter Interest Rate: "))
        loanTerm = int(input("Enter Loan Term (in months): "))
        loanType = input("Enter Loan Type: CarLoan/HomeLoan: ")
        loanStatus = "Pending"
        
        loan = Loans(loanID, customerID, principalAmount, interestRate, loanTerm, loanType, loanStatus)
        LoanRepository.applyLoan(loan)
    elif choice==2:
        loneid=int(input("Enter the loanid: "))
        LoanRepository.calculateInterest(loneid)
    elif choice==3:
        loneid=int(input("Enter the loanid: "))
        LoanRepository.calculateEMI(loneid)
    elif choice==4:
        loneid=int(input("Enter the loanid: "))
        LoanRepository.loanRepayment(loneid)
    elif choice==5:
        LoanRepository.getAllLoan()
    elif choice==6:
        loneid=int(input("Enter the loanid: "))
        LoanRepository.getLoanById(loneid)
    elif choice==7:
        loneid=int(input("Enter the loneid: "))
        LoanRepository.loanStatus(loneid)
    elif choice==8:
        LoanRepository.close()
        break
    else:
        print("Please enter the choice within range")