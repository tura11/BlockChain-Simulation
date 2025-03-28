# Python Blockchain Simulation

## 📘 Project Overview

This is a simple yet comprehensive blockchain simulation implemented in Python. The project demonstrates core blockchain concepts including block creation, hashing, proof-of-work, and chain validation.

## ✨ Features

- 🧱 Custom Block Structure
- 🔒 SHA-256 Hashing
- ⛏️ Proof-of-Work Mechanism
- 🔍 Blockchain Integrity Validation
- 📝 Transaction Tracking

## 🛠️ Prerequisites

- Python 3.7+
- No external libraries required (uses standard Python libraries)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/python-blockchain-simulation.git
cd python-blockchain-simulation
```

### 2. Verify Python Installation

```bash
python3 --version
# Should return Python 3.7+ 
```

## 🎮 How to Run

### Run the Simulation

```bash
python3 blockchain_simulation.py
```

### Expected Output

The script will:
- Create a blockchain
- Add sample transactions
- Print blockchain details
- Demonstrate chain validation
- Show tampering detection

## 🧪 Example Interaction

When you run the script, you'll see output similar to:

```
Block #0
Timestamp: [Genesis Block Time]
Transactions: ['Genesis Block Transaction']
...

Block #1
Timestamp: [First Block Time]
Transactions: ['Alice sends 1 BTC to Bob']
...

Is Blockchain Valid? True

--- Tampering Demonstration ---
Is Blockchain Valid After Tampering? False
```

## 🔍 Code Structure

- `Block` class: Represents individual blockchain blocks
- `Blockchain` class: Manages the entire blockchain
- Methods:
  - `calculate_hash()`: Generate block hash
  - `mine_block()`: Proof-of-work implementation
  - `is_chain_valid()`: Validate blockchain integrity

## 🤔 How It Works

1. Genesis block is created automatically
2. New blocks are added with transactions
3. Each block contains:
   - Block index
   - Timestamp
   - Transactions
   - Previous block's hash
   - Current block's hash
4. Proof-of-work requires finding a hash with specific properties
5. Chain validation checks block integrity

## 🚧 Limitations

- In-memory blockchain (data not persisted)
- Simplified proof-of-work
- Demonstration purposes only

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
