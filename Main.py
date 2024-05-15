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
    loan_repository = LoanRepository.ILoanRepositoryImpl()
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
        loan_repository.applyLoan(loan)
    elif choice==2:
        loanid=int(input("Enter the loanid: "))
        loan_repository.calculateInterest(loanid)
    elif choice==3:
        loanid=int(input("Enter the loanid: "))
        loan_repository.calculateEMI(loanid)
    elif choice==4:
        loanid=int(input("Enter the loanid: "))
        loan_repository.loanRepayment(loanid)
    elif choice==5:
        loan_repository.getAllLoan()
    elif choice==6:
        loanid=int(input("Enter the loanid: "))
        loan_repository.getLoanById(loanid)
    elif choice==7:
        loanid=int(input("Enter the loanid: "))
        loan_repository.loanStatus(loanid)
    elif choice==8:
        loan_repository.close()
        break
    else:
        print("Please enter the choice within range")