// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract LoanContract {

    address public borrower;
    address public lender;
    uint256 public amount;

    event LoanCreated(address borrower, address lender, uint256 amount);

    // Constructor to initialize loan details
    constructor(address _borrower, address _lender, uint256 _amount) {
        borrower = _borrower;
        lender = _lender;
        amount = _amount;
        // Emit the LoanCreated event
        emit LoanCreated(_borrower, _lender, _amount);
    }

    function getBorrower() public view returns (address) {
        return borrower;
    }

    function getLender() public view returns (address) {
        return lender;
    }

    function getAmount() public view returns (uint256) {
        return amount;
    }

    // Function to get loan details
    function getLoanDetails() public view returns (address, address, uint256) {
        return (borrower, lender, amount);
    }
}
