import hashlib
import time
import json

class Block:
    def __init__(self, index, previous_hash, transactions, timestamp=None):
        """
        Initialize a new block in the blockchain.
        
        :param index: Block number/index
        :param previous_hash: Hash of the previous block
        :param transactions: List of transactions in the block
        :param timestamp: Optional timestamp (defaults to current time)
        """
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = timestamp or time.time()
        self.nonce = 0
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        """
        Calculate the hash of the block using SHA-256.
        Includes all block data to ensure unique hash generation.
        
        :return: Calculated block hash
        """
        block_string = json.dumps({
            "index": self.index,
            "previous_hash": self.previous_hash,
            "transactions": self.transactions,
            "timestamp": self.timestamp,
            "nonce": self.nonce
        }, sort_keys=True)
        
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def mine_block(self, difficulty=4):
        """
        Simple proof-of-work mechanism.
        Finds a hash that starts with a specified number of zeros.
        
        :param difficulty: Number of leading zeros required
        :return: Final block hash
        """
        target = "0" * difficulty
        
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        
        return self.hash

class Blockchain:
    def __init__(self):
        """
        Initialize the blockchain with a genesis block.
        """
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4
    
    def create_genesis_block(self):
        """
        Create the first block in the blockchain.
        
        :return: Genesis block
        """
        return Block(0, "0", ["Genesis Block Transaction"], time.time())
    
    def get_latest_block(self):
        """
        Get the most recently added block.
        
        :return: Latest block in the chain
        """
        return self.chain[-1]
    
    def add_block(self, transactions):
        """
        Add a new block to the blockchain.
        
        :param transactions: List of transactions to include
        :return: Newly created and mined block
        """
        index = len(self.chain)
        previous_hash = self.get_latest_block().hash
        
        new_block = Block(index, previous_hash, transactions)
        new_block.mine_block(self.difficulty)
        
        self.chain.append(new_block)
        return new_block
    
    def is_chain_valid(self):
        """
        Validate the entire blockchain's integrity.
        Checks:
        1. Each block's previous hash matches actual previous block's hash
        2. Each block's hash is correctly calculated
        
        :return: Boolean indicating chain validity
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            
            # Check if current block's previous hash matches actual previous block's hash
            if current_block.previous_hash != previous_block.hash:
                return False
            
            # Verify block's own hash
            if current_block.hash != current_block.calculate_hash():
                return False
        
        return True
    
    def print_blockchain(self):
        """
        Print detailed information about each block in the chain.
        """
        for block in self.chain:
            print(f"\nBlock #{block.index}")
            print(f"Timestamp: {time.ctime(block.timestamp)}")
            print(f"Transactions: {block.transactions}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Current Hash: {block.hash}")
            print(f"Nonce: {block.nonce}")
            print("-" * 50)

def demonstrate_blockchain():
    """
    Demonstrate blockchain functionality including:
    1. Block creation
    2. Transaction addition
    3. Chain validation
    4. Tampering detection
    """
    # Create blockchain
    my_blockchain = Blockchain()
    
    # Add some sample blocks
    my_blockchain.add_block(["Alice sends 1 BTC to Bob"])
    my_blockchain.add_block(["Bob sends 0.5 BTC to Charlie"])
    my_blockchain.add_block(["Charlie sends 0.2 BTC to David"])
    
    # Print initial blockchain
    print("Initial Blockchain:")
    my_blockchain.print_blockchain()
    
    # Validate chain
    print(f"\nIs Blockchain Valid? {my_blockchain.is_chain_valid()}")
    
    # Demonstrate tampering
    print("\n--- Tampering Demonstration ---")
    # Try to modify a past block's transaction
    my_blockchain.chain[1].transactions[0] = "Hacked: Alice sends 1000 BTC to Hacker"
    
    # Recompute hash after tampering
    my_blockchain.chain[1].hash = my_blockchain.chain[1].calculate_hash()
    
    print(f"\nIs Blockchain Valid After Tampering? {my_blockchain.is_chain_valid()}")

# Run the demonstration
if __name__ == "__main__":
    demonstrate_blockchain()