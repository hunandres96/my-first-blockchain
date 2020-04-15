# Create a Blockchain

# importing the libraries
import datetime
import hashlib
import json
from flask import Flask, jsonify

# part 1 - building the blockchain
class Blockchain:
    
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')
        
    def create_block(self, proof, previous_hash):
        block = {
                    'index': len(self.chain) + 1,
                    'timestamp': str(datetime.datetime.now()),
                    'proof': proof,
                    'previous_hash': previous_hash
                }
        
        self.chain.append(block)
        return block


# part 2 - mining our blockchain