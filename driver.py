from transaction import Transaction
from block import Block
import time
import json
import hashlib

if __name__=="__main__":

    transaction_list = []
    prev_block_hash = "NA"
    block_height = 0

    while True:
        while True:

            amt_from = input("Please enter who this is from: ")
            amt_to = input("Please enter who this is to: ")
            amt = input("Please enter the amount to send: ")
            timestamp = int(time.time())

            transaction = Transaction(timestamp, amt_from, amt_to, amt)

            transaction_json_as_str = json.dumps(transaction.__dict__)
            transaction_list.append(transaction_json_as_str)
            transaction_json = json.dumps(transaction.__dict__).encode('UTF-8')

            # https://datagy.io/python-sha256/
            hashed_transaction_json = hashlib.sha256(transaction_json).hexdigest()

            # https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/
            with open(hashed_transaction_json + ".json", "w") as out:
                out.write(transaction_json_as_str)
                print(f"Transaction JSON file {hashed_transaction_json}.json created.")

                choice = input("Continue adding transactions? Y/N: ").lower()
                if choice == "n":
                    break

        header = {
        "block_height": block_height,
        "block_timestamp": int(time.time()),
        "prev_block_hash": prev_block_hash
        }

        header_json = json.dumps(header, indent = 4)
        current_block_hash = hashlib.sha256(header_json.encode('UTF-8')).hexdigest()
        header['current_block_hash'] = current_block_hash

        body = transaction_list

        block = Block(header, body)
        block_json = json.dumps(block.__dict__)

        with open("block" + str(header["block_height"]) + ".json", "w") as out:
            out.write(block_json)
        print("Block " + str(header["block_height"]) +  " JSON file created.")

        print("Current block hash: " + str(current_block_hash))
        print("Previous block hash: " + str(prev_block_hash))
        print("Current block height: " + str(block_height))

        block_height += 1
        prev_block_hash = current_block_hash

        choice = input("Continue adding blocks? Y/N: ").lower()
        if choice == "n":
            break
