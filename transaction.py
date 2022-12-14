class Transaction:
    def __init__(self,timestamp,amt_from,amt_to,amt):

        self.timestamp = timestamp
        self.amt_from = amt_from
        self.amt_to = amt_to
        self.amt = int(amt)
