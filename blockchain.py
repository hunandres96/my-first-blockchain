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


# part 2 - mining our blockchain