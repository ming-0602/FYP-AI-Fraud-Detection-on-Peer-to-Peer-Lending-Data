const LoanContract = artifacts.require("LoanContract");

module.exports = function(deployer, network, accounts) {
    // Parameters for the constructor (borrower, lender, amount, loanId)
    const borrower = accounts[1];  // Replace with the borrower address
    const lender = accounts[2];    // Replace with the lender address
    const amount = 1000;           // Example loan amount

    // Deploy the contract with the required parameters
    deployer.deploy(LoanContract, borrower, lender, amount);
};