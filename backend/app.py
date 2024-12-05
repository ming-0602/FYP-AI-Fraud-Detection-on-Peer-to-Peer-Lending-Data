from flask import Flask, request, jsonify
from web3 import Web3

app = Flask(__name__)

# Connect to Ganache
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

# Check if connected
if not w3.is_connected():
    raise Exception("Failed to connect to Ganache")

# Contract ABI and Address (Replace with your contract's ABI and address)
contract_abi = [
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_borrower",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "_lender",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "_amount",
                "type": "uint256"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "borrower",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "address",
                "name": "lender",
                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "amount",
                "type": "uint256"
            }
        ],
        "name": "LoanCreated",
        "type": "event"
    },
    {
        "inputs": [],
        "name": "amount",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function",
        "constant": True
    },
    {
        "inputs": [],
        "name": "borrower",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function",
        "constant": True
    },
    {
        "inputs": [],
        "name": "lender",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function",
        "constant": True
    },
    {
        "inputs": [],
        "name": "getBorrower",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function",
        "constant": True
    },
    {
        "inputs": [],
        "name": "getLender",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function",
        "constant": True
    },
    {
        "inputs": [],
        "name": "getAmount",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function",
        "constant": True
    },
    {
        "inputs": [],
        "name": "getLoanDetails",
        "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function",
        "constant": True
    }
]

contract_bytecode = '0x608060405234801561001057600080fd5b5060405161059c38038061059c83398181016040528101906100329190610127565b826000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555081600160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550806002819055507f239918703fc8dd9af4a7df82136ff89b353e3bed6fb86c9952ca3e8698a7d6338383836040516100ed93929190610194565b60405180910390a1505050610235565b60008151905061010c81610207565b92915050565b6000815190506101218161021e565b92915050565b60008060006060848603121561013c57600080fd5b600061014a868287016100fd565b935050602061015b868287016100fd565b925050604061016c86828701610112565b9150509250925092565b61017f816101cb565b82525050565b61018e816101fd565b82525050565b60006060820190506101a96000830186610176565b6101b66020830185610176565b6101c36040830184610185565b949350505050565b60006101d6826101dd565b9050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b6000819050919050565b610210816101cb565b811461021b57600080fd5b50565b610227816101fd565b811461023257600080fd5b50565b610358806102446000396000f3fe608060405234801561001057600080fd5b506004361061007d5760003560e01c8063a3b9e39d1161005b578063a3b9e39d146100dc578063aa8c217c146100fc578063bcead63e1461011a578063d321fe29146101385761007d565b80631cb0c3e7146100825780637df1f1b9146100a05780639861f3e5146100be575b600080fd5b61008a610156565b6040516100979190610279565b60405180910390f35b6100a861017f565b6040516100b59190610279565b60405180910390f35b6100c66101a3565b6040516100d39190610279565b60405180910390f35b6100e46101cd565b6040516100f393929190610294565b60405180910390f35b610104610225565b60405161011191906102cb565b60405180910390f35b61012261022b565b60405161012f9190610279565b60405180910390f35b610140610251565b60405161014d91906102cb565b60405180910390f35b60008060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905090565b60008054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b6000600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905090565b60008060008060009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16600254925092509250909192565b60025481565b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b6000600254905090565b610264816102e6565b82525050565b61027381610318565b82525050565b600060208201905061028e600083018461025b565b92915050565b60006060820190506102a9600083018661025b565b6102b6602083018561025b565b6102c3604083018461026a565b949350505050565b60006020820190506102e0600083018461026a565b92915050565b60006102f1826102f8565b9050919050565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b600081905091905056fea26469706673582212206287c952bc2b15e464af0aa32b71ab66e4e20c5cf935b23db488bc44806003e864736f6c63430008000033'  # Replace with your contract's deployed address
contract_address = '0xDd6AcE8EBEBd8f6879e36Bc04C00a13A76d7b2Ab'

# Set up the contract instance
# contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Use the first account from Ganache (Make sure you have Ganache running)
account = w3.eth.accounts[0]


@app.route('/create-loan', methods=['POST'])
def create_loan():
    data = request.json
    borrower = data['borrower']
    lender = data['lender']
    amount = data['amount']

    # Compile and deploy the LoanContract with the given loan details
    LoanContract = w3.eth.contract(abi=contract_abi, bytecode=contract_bytecode)

    # Deploy the contract
    tx_hash = LoanContract.constructor(borrower, lender, amount).transact({'from': account})

    # Wait for the transaction to be mined
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    # Get the deployed contract address
    loan_contract_address = receipt['contractAddress']

    print(f"Deploying contract with: Borrower={borrower}, Lender={lender}, Amount={amount}")

    return jsonify({
        'status': 'Loan created',
        'loanContractAddress': loan_contract_address,
        'transactionHash': receipt['transactionHash'].hex()
    })


# Endpoint to retrieve loan details
@app.route('/get-loan-details/<loan_contract_address>', methods=['GET'])
def get_loan_details(loan_contract_address):
    contract = w3.eth.contract(address=loan_contract_address, abi=contract_abi)

    # Call the getLoanDetails function from the contract
    loan_details = contract.functions.getLoanDetails().call()

    return jsonify({
        'borrower': loan_details[0],
        'lender': loan_details[1],
        'amount': loan_details[2]
    })


@app.route('/get_all_contract', methods=['GET'])
def get_all_contract():
    contract_addresses = []

    # Get the latest block number
    latest_block = w3.eth.block_number

    # Iterate through all blocks and fetch contract addresses
    for block_num in range(latest_block + 1):
        block = w3.eth.get_block(block_num, full_transactions=True)

        # Check all transactions in the block
        for tx in block['transactions']:
            if tx['to'] is None:  # This is a contract creation transaction
                # Get the receipt of the transaction to find the contract address
                receipt = w3.eth.get_transaction_receipt(tx['hash'])

                # Check if 'contractAddress' exists in the receipt
                if 'contractAddress' in receipt:
                    contract_addresses.append(receipt['contractAddress'])

    # return jsonify({'contractAddresses': contract_addresses})
    return contract_addresses


@app.route('/get-all-loans', methods=['GET'])
def get_all_loans():
    contract_addresses = get_all_contract()  # Function that returns all contract addresses
    loan_details = []

    for address in contract_addresses:
        contract = w3.eth.contract(address=address, abi=contract_abi)  # Interact with the contract using the ABI

        try:
            # Call the existing getter functions (you should already have these in your contract)
            borrower = contract.functions.getBorrower().call()

            lender = contract.functions.getLender().call()

            amount = contract.functions.getAmount().call()


            # print(f"Fetched details - Borrower: {borrower}, Lender: {lender}, Amount: {amount}")

            # Store the details for each contract
            loan_details.append({
                'contract_address': address,
                'borrower': str(borrower),
                'lender': str(lender),
                'amount': int(amount)
            })

            # print(loan_details)
        except Exception as e:
            # Handle errors in case a contract doesn't have the expected data or is not accessible
            loan_details.append({
                'contract_address': address,
                'error': str(e)
            })

    return jsonify(loan_details)


if __name__ == '__main__':
    app.run(debug=True)
