CREATE DATABASE LoanManagementSystem
use LoanManagementSystem

-- Create the Customers table
CREATE TABLE Customers
(
    CustomerId INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    EmailAddress VARCHAR(100) NOT NULL,
    PhoneNumber VARCHAR(20) NOT NULL,
    Address VARCHAR(200) NOT NULL,
    CreditScore INT NOT NULL
);

-- Create the Loans table
CREATE TABLE Loans
(
    LoanId INT PRIMARY KEY,
    CustomerId INT NOT NULL,
    PrincipalAmount DECIMAL(10, 2) NOT NULL,
    InterestRate DECIMAL(5, 2) NOT NULL,
    LoanTerm INT NOT NULL,
    LoanType VARCHAR(20) NOT NULL,
    LoanStatus VARCHAR(20) NOT NULL,
    FOREIGN KEY (CustomerId) REFERENCES Customers(CustomerId)
);