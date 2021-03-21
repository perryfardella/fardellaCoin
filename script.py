from blockchain import Blockchain

# Python dictionary objects with key/value pairs to store the transaction data
transaction1 = {
    'amount': '30',
    'sender': 'Alice',
    'receiver': 'Bob'}
transaction2 = {
    'amount': '200',
    'sender': 'Bob',
    'receiver': 'Alice'}
transaction3 = {
    'amount': '300',
    'sender': 'Alice',
    'receiver': 'Timothy'}
transaction4 = {
    'amount': '300',
    'sender': 'Rodrigo',
    'receiver': 'Thomas'}
transaction5 = {
    'amount': '200',
    'sender': 'Timothy',
    'receiver': 'Thomas'}
transaction6 = {
    'amount': '400',
    'sender': 'Tiffany',
    'receiver': 'Xavier'}
my_transaction = {
    'amount': '400',
    'sender': 'Xavier',
    'receiver': 'Perry'
}

mempool = [transaction1, transaction2, transaction3,
           transaction4, transaction5, transaction6, my_transaction]

new_transactions = [transaction1, transaction2, my_transaction]


my_blockchain = Blockchain()
my_blockchain.add_block(new_transactions)
my_blockchain.print_blocks

my_blockchain.chain[1].transactions = 'fake_transactions'

print(my_blockchain.validate_chain())
