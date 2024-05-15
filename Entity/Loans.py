class Loans:
    def __init__(
            self,
            LoanId,
            CustomerId,
            PrincipalAmount,
            InterestRate,
            LoanTerm,
            LoanType,
            LoanStatus,
            
    ):
        self.LoanId = LoanId
        self.customerId = CustomerId
        self.PrincipalAmount = PrincipalAmount
        self.InterestRate = InterestRate 
        self.LoanTerm = LoanTerm
        self.LoanType = LoanType
        self.LoanStatus = LoanStatus

class HomeLoan(Loans):
    def __init__(self, loan_id, customer, principal_amount, interest_rate, loan_term, property_address, property_value):
        super().__init__(loan_id, customer, principal_amount, interest_rate, loan_term, "HomeLoan", "Pending")
        self.property_address = property_address
        self.property_value = property_value

    def __str__(self):
        return super().__str__() + f", Property Address: {self.property_address}, Property Value: {self.property_value}"


class CarLoan(Loans):
    def __init__(self, loan_id, customer, principal_amount, interest_rate, loan_term, car_model, car_value):
        super().__init__(loan_id, customer, principal_amount, interest_rate, loan_term, "CarLoan", "Pending")
        self.car_model = car_model
        self.car_value = car_value

    def __str__(self):
        return super().__str__() + f", Car Model: {self.car_model}, Car Value: {self.car_value}"