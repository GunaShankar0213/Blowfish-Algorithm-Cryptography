# Cryptography with Blowfish Algorithm

This repository demonstrates the usage of the **Blowfish algorithm** for encrypting and decrypting messages using Python. Blowfish is a symmetric-key block cipher that is widely used due to its speed and security.

## Overview

The **Blowfish Algorithm** was designed by **Bruce Schneier** in 1993 as a fast and secure encryption method. It operates on **64-bit** blocks of data and supports key sizes ranging from **32 bits to 448 bits**. Blowfish is a **symmetric-key cipher**, meaning the same key is used for both encryption and decryption. 

In this project, we explore the implementation of Blowfish to securely encrypt and decrypt messages using the Python programming language.

## Architecture of the Blowfish Algorithm

The Blowfish algorithm consists of the following main components:

### 1. **Key Expansion**  
The key expansion phase takes a variable-length key (between 32 and 448 bits) and generates several subkeys. These subkeys are used in the encryption and decryption processes.

### 2. **Rounds of Encryption**
Blowfish performs encryption through **16 rounds**. Each round uses a pair of subkeys (one for the left and one for the right block). These subkeys are combined with the data using a function known as the **Feistel structure**.

### 3. **Feistel Structure**
The Feistel structure splits the data block into two halves. One half is passed through a function (which involves XOR operations and S-box lookups), and the result is XOR'd with the other half. This process is repeated for a number of rounds.

### 4. **Final Permutation**
After completing the rounds, the halves are swapped and combined, and the result is a fully encrypted block.

## Blowfish Algorithm Steps

### 1. **Initialization**
- **Key Expansion**: The encryption key is expanded into a series of subkeys used for the rounds.
- **Subkey Generation**: The key is expanded into 18 subkeys, and each round uses two of these subkeys.

### 2. **Encryption**
For encryption, Blowfish uses the following:
- **Initial Data Block**: The plaintext message is divided into 64-bit blocks.
- **Feistel Network**: Each 64-bit block goes through 16 rounds of processing. The result is the encrypted message.

### 3. **Decryption**
Decryption is done by reversing the encryption process, using the same key and subkeys but in reverse order. This is possible due to the symmetric nature of the Blowfish algorithm.

## How Blowfish Encryption Works

Here’s an overview of how a message is encrypted using Blowfish:

1. **Key Input**: The user provides a secret key (between 32 and 448 bits).
2. **Key Expansion**: The key is expanded into a series of subkeys, which are used for the encryption rounds.
3. **Plaintext Input**: The message to be encrypted is divided into 64-bit blocks.
4. **Feistel Rounds**: Each block undergoes 16 rounds of the Feistel structure, where the data is processed with XOR operations and substituted through the S-boxes.
5. **Ciphertext Output**: The final result after all rounds is the encrypted ciphertext, which is outputted.

### Example Encryption Process
If we want to encrypt the message **"Hello World"** using Blowfish, the following steps would occur:

1. **Key Expansion**: The key provided is expanded into subkeys.
2. **Message Split**: The message is split into 64-bit blocks.
3. **Encryption Rounds**: Each 64-bit block undergoes 16 rounds of encryption.
4. **Resulting Ciphertext**: The encrypted ciphertext is produced after 16 rounds.

## Message Encryption Using Blowfish

The encryption process uses a series of operations involving **XOR**, **S-boxes**, and **P-array** to transform the plaintext into ciphertext. Here’s a basic demonstration of the process using Python.

### Example Code for Encryption (Blowfish Algorithm)
```python
from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
import binascii

# Initialize the Blowfish cipher
key = b"mysecretkey"  # Encryption key (between 4 and 56 bytes)
cipher = Blowfish.new(key, Blowfish.MODE_CBC)

# Sample plaintext message
plaintext = b"Hello World!"

# Pad the plaintext to make it a multiple of the block size (8 bytes for Blowfish)
padded_text = pad(plaintext, Blowfish.block_size)

# Encrypt the padded message
ciphertext = cipher.encrypt(padded_text)
print("Encrypted:", binascii.hexlify(ciphertext))

# Decrypt the ciphertext
decipher = Blowfish.new(key, Blowfish.MODE_CBC, cipher.iv)
decrypted = unpad(decipher.decrypt(ciphertext), Blowfish.block_size)
print("Decrypted:", decrypted.decode())
