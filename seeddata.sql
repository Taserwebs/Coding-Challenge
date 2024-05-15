-- Insert values into the Customers table
INSERT INTO Customers
    (CustomerId, Name, EmailAddress, PhoneNumber, Address, CreditScore)
VALUES
    (1, 'John Doe', 'john.doe@email.com', '1234567890', '123 Main St, City, State', 750),
    (2, 'Jane Smith', 'jane.smith@email.com', '9876543210', '456 Elm St, City, State', 680),
    (3, 'Michael Johnson', 'michael.johnson@email.com', '5551234567', '789 Oak Rd, City, State', 820),
    (4, 'Emily Davis', 'emily.davis@email.com', '1112223333', '321 Pine Ave, City, State', 700),
    (5, 'David Wilson', 'david.wilson@email.com', '4445556666', '159 Maple Ln, City, State', 650),
    (6, 'Sophia Thompson', 'sophia.thompson@email.com', '7778889999', '753 Cedar Dr, City, State', 790),
    (7, 'Daniel Anderson', 'daniel.anderson@email.com', '2223334444', '963 Birch St, City, State', 720),
    (8, 'Olivia Martinez', 'olivia.martinez@email.com', '5556667777', '147 Walnut Rd, City, State', 780),
    (9, 'William Brown', 'william.brown@email.com', '8889990000', '258 Spruce Ave, City, State', 710),
    (10, 'Emma Garcia', 'emma.garcia@email.com', '1112223344', '369 Ash Ln, City, State', 670);

-- Insert values into the Loans table
INSERT INTO Loans
    (LoanId, CustomerId, PrincipalAmount, InterestRate, LoanTerm, LoanType, LoanStatus)
VALUES
    (1, 1, 250000.00, 4.25, 360, 'HomeLoan', 'Approved'),
    (2, 2, 20000.00, 6.75, 48, 'CarLoan', 'Pending'),
    (3, 3, 150000.00, 3.90, 180, 'HomeLoan', 'Approved'),
    (4, 4, 25000.00, 5.50, 60, 'CarLoan', 'Approved'),
    (5, 5, 75000.00, 4.65, 120, 'HomeLoan', 'Pending'),
    (6, 6, 35000.00, 7.25, 72, 'CarLoan', 'Approved'),
    (7, 7, 200000.00, 4.10, 240, 'HomeLoan', 'Approved'),
    (8, 8, 18000.00, 6.20, 36, 'CarLoan', 'Pending'),
    (9, 9, 100000.00, 3.75, 120, 'HomeLoan', 'Approved'),
    (10, 10, 30000.00, 6.50, 60, 'CarLoan', 'Pending');
