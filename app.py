#######################################################################################################################
#                                                                                                                     #
#                                           S N A K E  C H A I N                                                      #
#                                                                                                                     #
#######################################################################################################################


# Define our block structure
# @properties: hash, timestamp, index, data, previous_hash

import hashlib as hasher
import datetime as date


class Block:
    def __init__(self, index, timestamp, data, prev_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update((str(self.index) +
                    str(self.timestamp) +
                    str(self.data) +
                    str(self.prev_hash)).encode())

        return sha.hexdigest()


# Create the first block - genesis block
# block of index 0 with an arbitrary data value and prev_hash
def mk_genesis_block():
    return Block(0, date.datetime.now(), 'Genesis Block', '0')


# Generate succeeding blocks
# @params(prev_block)
def next_block(prev_block):
    self_index = prev_block.index + 1
    self_timestamp = date.datetime.now()
    self_data = f'  --> Block: {self_index}'
    self_hash = prev_block.hash

    return Block(self_index, self_timestamp, self_data, self_hash)


# Start up the blockchain
snakechain = [mk_genesis_block()]
last_block = snakechain[0]
status_active = True

while status_active is True:
    new_block = next_block(last_block)
    snakechain.append(new_block)
    last_block = new_block

    print(f'\n  ☻ New block in the blockchain: {new_block.index} ')
    print(f'    # Hash: {new_block.hash} \n')
