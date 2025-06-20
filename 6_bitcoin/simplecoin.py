# helper function mentioned in the homework assignment
def verifySignature(pubKey, message, signature):
    """
    Assumed to be a pre-existing function that verifies a signature.
    For my simulation, we'll just check if the signature matches the
    expected format: 'sig_for_' + pubKey.
    """
    return signature == f"sig_for_{pubKey}"

# Part 1: Data Structures

class Coin:
    """
    Represents a single coin, more accurately an Unspent Transaction Output.
    A coin is defined by the transaction that created it and its position within
    that transaction's outputs.
    """
    # A coin includes: transaction_id, output_index, value, recipient_pubkey
    def __init__(self, transaction_id, output_index, value, recipient_pubkey):
        self.transaction_id = transaction_id
        self.output_index = output_index
        self.value = value
        self.recipient_pubkey = recipient_pubkey

    def get_id(self):
        """Returns the unique identifier for this coin."""
        return (self.transaction_id, self.output_index)


class Transaction:
    def __init__(self, transaction_type):
        self.id = None
        self.transaction_type = transaction_type  # "CreateCoin" or "PayCoin"

    # create a method to assign id to the transaction
    def assign_id(self, transaction_id):
        self.id = transaction_id


# CreateCoin: inherit from Transaction
class CreateCoinTransaction(Transaction):
    """
    Represents a CreateCoin transaction that creates new coins 
    and Only entity G can create these (like mining/minting).
    """
    def __init__(self, outputs):
        super().__init__("CreateCoin")
        self.outputs = outputs  # List of new Coins created
        self.inputs = []   # No inputs
        self.signatures = []  # No signatures (G creates them)

    def assign_id(self, transaction_id):
        """Assigns an ID to this transaction and updates its output coins."""
        # First assign the transaction ID
        super().assign_id(transaction_id)
        
        # Then update each output coin with this transaction ID and its index
        # enumerate to get index and coin
        for i, coin in enumerate(self.outputs):
            coin.transaction_id = self.id # Assign the transaction ID
            coin.output_index = i       # Assign the output index
        # The final output will be a list of coins with correct IDs


# Another subclass for transactions: payment transactions
class PayCoinTransaction(Transaction):
    """
    Represents a PayCoin transaction, which consumes existing coins and creates new ones (outputs).
    The ID is assigned by the Ledger upon processing.
    """
    def __init__(self, inputs, outputs, signatures):
        super().__init__("PayCoin")
        self.inputs = inputs  # List of coin IDs (tuples) being spent.
        self.outputs = outputs # List of new Coin objects being created.
        self.signatures = signatures # List of signatures

    # Similar to CreateCoinTransaction, we need to assign IDs to outputs
    def assign_id(self, transaction_id):
        """Assigns an ID to this transaction and updates its output coins."""
        super().assign_id(transaction_id)
        for i, coin in enumerate(self.outputs):
            coin.transaction_id = self.id
            coin.output_index = i


# Part 2: Blockchain (Ledger) Structure

class Block:
    """
    A Single block in the blockchain, containing a Single transaction.
    """
    def __init__(self, transaction, previous_hash):
        self.transaction = transaction
        self.previous_hash = previous_hash
        # The block's hash is simply the ID of the transaction it contains, for simplicity.
        self.hash = transaction.id

class Ledger:
    """
    Represents the entire blockchain and the state of all coins.
    This class contains the logic used by entity 'G' to validate transactions.
    """
    def __init__(self):
        # The blockchain is a list of blocks, each containing a transaction.
        self.chain = []
        # A dictionary to store all unspent coins for quick lookups.
        self.unspent_coins = {}
        # The Ledger is responsible for assigning transaction IDs.
        self.next_transaction_id = 0
        self._create_initial_coins()

    # Let's make some initial coins for Alice and Bob (Not been used in real world)
    def _create_initial_coins(self):
        """
        Creates the very first CreateCoin transaction to introduce initial coins.
        """
        initial_coins = [
            Coin(None, 0, 10.0, "Alice_pubkey"),
            Coin(None, 1, 15.0, "Alice_pubkey"),
            Coin(None, 2, 25.0, "Bob_pubkey"),
        ]

        # Create a proper CreateCoin transaction
        initial_transaction = CreateCoinTransaction(outputs=initial_coins)
        self.process_transaction(initial_transaction)
        print("Ledger initialized with initial CreateCoin transaction.")

    def create_new_coins(self, value_list, recipient_list):
        """
        G can create new coins by issuing a CreateCoin transaction.
        """
        if len(value_list) != len(recipient_list):
            raise ValueError("Value list and recipient list must have the same length")
        
        new_coins = [
            Coin(None, i, value, recipient) 
            for i, (value, recipient) in enumerate(zip(value_list, recipient_list))
        ]
        
        create_tx = CreateCoinTransaction(outputs=new_coins)
        # process the transaction is in part 3, to check whether it is valid or not.
        return self.process_transaction(create_tx)



    # Part 3: Transaction Validation Function
    # return True if valid, False if invalid
    def process_transaction(self, transaction):
        """
        The main function for G to check if a transaction is valid.
        If it is, it assigns an ID and adds it to the blockchain.
        """
        # Assign the next available ID before processing to track the ID used.
        transaction.assign_id(self.next_transaction_id)
        # Print infomation about the transaction, 1.ID 2.type
        print(f"Processing {transaction.transaction_type} transaction {transaction.id}...")

        try:
            if transaction.transaction_type == "CreateCoin":
                # CreateCoin transactions are always valid (G has authority to create coins)
                print(f"CreateCoin transaction {transaction.id} is VALID (G has authority).")
                # AddToBlockchain will be provided later, a function to add the transaction to the chain.
                # Bascially just
                self.AddToBlockchain(transaction)
                # This is the default counter
                self.next_transaction_id += 1
                return True
            
            elif transaction.transaction_type == "PayCoin":
                # Rule 1: The consumed coins are valid AND have proper signatures from their owners
                input_coins = []
                
                # First, check if all input coins exist and are valid
                for coin_id in transaction.inputs:
                    # Find the coin in our records (could be spent or unspent)
                    coin_found = False
                    target_coin = None
                    
                    # Check in unspent coins
                    if coin_id in self.unspent_coins:
                        target_coin = self.unspent_coins[coin_id]
                        coin_found = True
                    else:
                        # Check in blockchain history to see if coin ever existed
                        for block in self.chain:
                            for i, output_coin in enumerate(block.transaction.outputs):
                                if output_coin.get_id() == coin_id:
                                    target_coin = output_coin
                                    coin_found = True
                                    break
                            if coin_found:
                                break
                    
                    if not coin_found:
                        raise ValueError(f"Validation Failed (Rule 1): Input coin {coin_id} does not exist.")
                    
                    input_coins.append(target_coin)
                
                # Check signatures for ownership verification (part of Rule 1)
                if len(input_coins) != len(transaction.signatures):
                    raise ValueError("Validation Failed (Rule 1): Number of inputs must match number of signatures.")

                for i, coin in enumerate(input_coins):
                    signature = transaction.signatures[i]
                    owner_pubkey = coin.recipient_pubkey                    
                    # Verify that the signature was created by the coin's rightful owner
                    if not verifySignature(owner_pubkey, signature):
                        raise ValueError(f"Validation Failed (Rule 1): Invalid signature for coin {coin.get_id()}. Only the owner ({owner_pubkey}) can spend this coin.")
                    
                # Rule 2: No double spending within the transaction.
                # This is automatically checked by the above loop, 
                # since we have a dictionary of unspent coins self.unspent_coins. But I will keep it for clarity.
                for coin_id in transaction.inputs:
                    if coin_id not in self.unspent_coins:
                        raise ValueError(f"Validation Failed (Rule 2): Input coin {coin_id} has already been spent (double spending attempt).")

                # Rule 3: Total value of outputs equals total value of inputs.
                total_input_value = sum(coin.value for coin in input_coins)
                total_output_value = sum(coin.value for coin in transaction.outputs)
                if total_input_value != total_output_value:
                    raise ValueError(f"Validation Failed: Input value ({total_input_value}) does not match output value ({total_output_value}).")


                # Rule 4: Valid signatures from the owners of the consumed coins.
                if len(input_coins) != len(transaction.signatures):
                     raise ValueError("Validation Failed: Number of inputs must match number of signatures.")

                for i, coin in enumerate(input_coins):
                    signature = transaction.signatures[i]
                    owner_pubkey = coin.recipient_pubkey
                    # The 'message' being signed would typically be the transaction data.
                    if not verifySignature(owner_pubkey, signature):
                        raise ValueError(f"Validation Failed: Invalid signature for coin {coin.get_id()} from owner {owner_pubkey}.")

                # If all checks pass, the transaction is valid.
                print(f"PayCoin transaction {transaction.id} is VALID.")
                self.AddToBlockchain(transaction)
                self.next_transaction_id += 1
                return True

        except ValueError as e:
            # If validation fails, we do not increment the next_transaction_id.
            # The failed transaction's ID is discarded.
            print(f"Transaction {transaction.id} is INVALID. Reason: {e}")
            return False

    def AddToBlockchain(self, transaction):
        """
        Add a validated transaction to the chain and update the self.unspent_coins = {}.
        """
        # Create a new block
        last_block_hash = self.chain[-1].hash if self.chain else "0" # if self.chain check if it is empty
        new_block = Block(transaction, last_block_hash)
        self.chain.append(new_block)

        # Update the unspent_coins dictionary: remove spent (for PayCoin), add new.
        for coin_id in transaction.inputs:
            del self.unspent_coins[coin_id]
        for coin in transaction.outputs:
            self.unspent_coins[coin.get_id()] = coin

        print(f"Transaction {transaction.id} added to new block {new_block.hash}.")
        print("Ledger state updated.")

    def get_balance(self, pubkey):
        """Get total balance for a given public key"""
        balance = 0
        for coin in self.unspent_coins.values():
            if coin.recipient_pubkey == pubkey:
                balance += coin.value
        return balance

    def get_transaction_history(self):
        """Get a list of all transactions in the blockchain"""
        # this is simple in my list data structure, real world is more complex.
        return [(block.transaction.id, block.transaction.transaction_type) for block in self.chain]

    def print_full_state(self):
        print("FULL LEDGER STATE")
        print("Blockchain:")
        for i, block in enumerate(self.chain):
            print(f"Block {i}: {block}")
        
        print(f"Unspent Coins ({len(self.unspent_coins)}):")
        for coin_id, coin in self.unspent_coins.items():
            print(f"{coin}")
        
        print("Balances:")
        all_owners = set(coin.recipient_pubkey for coin in self.unspent_coins.values())
        for owner in all_owners:
            print(f"{owner}: {self.get_balance(owner)}")

        print(f"Transaction History: {self.get_transaction_history()}")