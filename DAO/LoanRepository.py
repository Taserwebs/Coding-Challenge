from DAO.ILoanRepository import ILoanRepository
from Util.DBconnenction import DBConnection
from Exception.Exceptions import ApplyLoanException,calculateEMIException,InvalidLoanException,RetriveloanException,calculateInterestException


class ILoanRepositoryImpl(ILoanRepository,DBConnection):

    def applyLoan(self, Loan):
        try:
            self.cursor.execute("INSERT INTO  Loans (LoanID, CustomerId, PrincipalAmount, InterestRate, LoanTerm, LoanType, LoanStatus) VALUES (?,?,?,?,?,?,?)",
                                (Loan.LoanId,Loan.CustomerId, Loan.PrincipalAmount, Loan.InterestRate, Loan.LoanTerm, Loan.LoanType, Loan.LoanStatus))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise ApplyLoanException("Could'nt apply loan check CustomerId")
        
    def calculateInterest(self, LoanID):
        try:
            self.cursor.execute("Select PrincipalAmount,InterestRate,LoanTerm from Loans where LoanID=?",
                                (LoanID))
            result=self.cursor.fetchone()
            if result:
                ##self.calculateInterest(result[0],result[1],result[2])
                principalAmount, interestRate, loanTerm = result
                interest = (principalAmount * interestRate * loanTerm) / 12
                print(f"The interest is {round(interest,2)}")
            else:
                raise calculateInterestException("Error No Loan Found")
        except Exception as e:
            self.conn.rollback()
            raise calculateInterestException("Couldn't calculate interest. Error: {}".format(str(e)))
        
    def loanStatus(self, loanId):
        try:
            self.cursor.execute("Select CreditScore from Loans l inner join  Customers c on c.CustomerId=l.CustomerId where LoanId=?;",(loanId))
            result=self.cursor.fetchone()
            if result:
                ##self.calculateInterest(result[0],result[1],result[2])
                credit_score = result[0]
                if credit_score>650:
                    print("Approved")
                    self.cursor.execute("update Loans set LoanStatus='Approved' where LoanId=?;",(loanId))
                    self.conn.commit()
                else:
                    print("Rejected")
                    self.cursor.execute("update Loans set LoanStatus='Rejected' where LoanId=?;",(loanId))
                    self.conn.commit()
            else:
                raise InvalidLoanException("Loan not found")
        except Exception as e:
            self.conn.rollback()
            raise InvalidLoanException("Couldn't find customer/loan. Error: {}".format(str(e)))
        
    def calculateEMI(self, loanId):
        try:
            self.cursor.execute("Select PrincipalAmount,InterestRate,LoanTerm from Loans where LoanId=?",
                                (loanId))            
            result=self.cursor.fetchone()
            if result:
                ##self.calculateInterest(result[0],result[1],result[2])
                PrincipalAmount, InterestRate, LoanTerm = result
                R = InterestRate / (12 * 100)
                emi=(PrincipalAmount*R*(1+R)**LoanTerm)/((1+R)**LoanTerm-1)
                print(f"The emi is {round(emi,2)}")
                return emi
            else:
                raise InvalidLoanException("Loan not found")
        except Exception as e:
            self.conn.rollback()
            raise InvalidLoanException("Couldn't find customer/loan. Error: {}".format(str(e)))
        
    def loanRepayment(self,loanId,amount):
        try:
            emi=self.calculateEMI(loanId)
            loanRepaymentcount=0
            if emi:
                if emi>amount:
                    raise InvalidLoanException(f"Payment rejected amount {amount} is letter than emi {emi}")
                ##self.calculateInterest(result[0],result[1],result[2])
                else:
                    while amount>0:
                        amount=amount/emi
                        loanRepaymentcount+=1
                print(f"The total number of emi payed by amount {amount} is {loanRepaymentcount}")
            else:
                raise calculateEMIException("Loan not found")
        except Exception as e:
            self.conn.rollback()
            raise InvalidLoanException("Couldn't find customer/loan. Error: {}".format(str(e)))
                
    def getAllLoan(self):
        try:
            self.cursor.execute("Select * from Loans")
            print(self.cursor.fetchall())
        except Exception as e:
            self.conn.rollback()
            raise InvalidLoanException("No loan available")
        
    def getLoanById(self, loanId):
        try:
            self.cursor.execute("Select * from Loans where LoanId=?",(loanId))
            result=self.cursor.fetchall()
            if result:
                print(result)
            else:
                raise RetriveloanException("Id not found")
        except Exception as e:
            self.conn.rollback()
            raise InvalidLoanException("No loan available")
    def close(self):
        self.cursor.close()
        self.conn.close()
               
        ##overloadingcode
    # def calculateInterest(self,principalAmount, interestRate, loanTerm):
    #     try:
    #         interest=(principalAmount*interestRate*loanTerm)/12
    #         print(f"The interest is {interest}")
    #     except Exception as e:
    #         raise calculateInterestException("Error")