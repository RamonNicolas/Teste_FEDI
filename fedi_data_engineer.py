import sqlite3
import datetime
import pandas as pd
    
def connection_db():
    # Connection to DB
    conn = sqlite3.connect('fedimint-observer.db')
    return conn

class Test_FEDI:
    def __init__(self) -> None:
        self.conn = connection_db()
        self.cursor = self.conn.cursor()        

    def pegged_in(self):
        # Bitcoin Pegged-in
        self.cursor.execute("SELECT SUM(amount_msat), amount_msat FROM transaction_inputs")
        _pegged_in = self.cursor.fetchone()[0]
        return _pegged_in

    def pegged_out(self):
        # Bitcoin Pegged-out
        self.cursor.execute("SELECT SUM(amount_msat), amount_msat FROM transaction_outputs")
        _pegged_out = self.cursor.fetchone()[0]
        return _pegged_out

    def current_balance(self):
        return self.pegged_in() - self.pegged_out()
    
    def federation_id_input(self):
        self.cursor.execute("SELECT federation_id FROM transaction_inputs")
        _federation = self.cursor.fetchone()[0]
        return _federation
    
    def federation_id_output(self):
        self.cursor.execute("SELECT federation_id FROM transaction_outputs")
        _federation = self.cursor.fetchone()[0]
        return _federation
    
    def kind_id_input(self):
        self.cursor.execute("SELECT kind FROM transaction_inputs")
        _federation = self.cursor.fetchone()[0]
        return _federation
    
    def kind_id_output(self):
        self.cursor.execute("SELECT kind FROM transaction_outputs")
        _kind_id = self.cursor.fetchone()[0]
        return _kind_id

    def in_contracts_type(self):
        self.cursor.execute("SELECT type FROM ln_contracts")
        _type = self.cursor.fetchone()[0]
        return _type
    
    def in_contracts_paymenthash(self):
        self.cursor.execute("SELECT payment_hash FROM ln_contracts")
        _payment_hash = self.cursor.fetchone()[0]
        return _payment_hash

    def in_contracts_contract_id(self):
        self.cursor.execute("SELECT contract_id FROM ln_contracts")
        _contract_id = self.cursor.fetchone()[0]
        return _contract_id
    
    def most_recently_transaction(self):
        self.cursor.execute("SELECT max(timestamp) FROM block_times")
        _data = datetime.datetime.fromtimestamp(self.cursor.fetchone()[0])
        return _data
    
    def block_height_vote(self):
        self.cursor.execute("SELECT max(height_vote) FROM block_height_votes")
        _block_height_vote = self.cursor.fetchone()[0]
        return _block_height_vote
    
    def transaction_inputs_block_times_top100(self):
        self.cursor.execute("""
        SELECT transaction_inputs.federation_id, block_times.block_height, 
                            height_vote, transaction_inputs.amount_msat, block_times.timestamp
        FROM block_height_votes
        INNER JOIN block_times ON block_height_votes.height_vote = block_times.block_height
        INNER JOIN transaction_inputs ON transaction_inputs.federation_id = transactions.federation_id
        INNER JOIN transactions ON transaction_inputs.federation_id = transactions.federation_id
        ORDER BY transactions.federation_id DESC
        LIMIT 10;
        """)        
        _block_height_vote = self.cursor.fetchall()
        result = []
        for index,value in enumerate(_block_height_vote):
            mutable = list(_block_height_vote[index])
            mutable[-1] = datetime.datetime.fromtimestamp(_block_height_vote[index][-1])
            result.append(mutable)

        _data = pd.DataFrame(result, columns=['federation_id', 'block_height', 
                            'height_vote', 'amount_msat', 'date'])
        return _data[:10]
    
    def show_info(self):    
        print(f"Bitcoin Pegged-in: {self.pegged_in()}")
        print(f"Bitcoin Pegged-out: {self.pegged_out()}")
        print(f"Current On-chain Balance: {self.current_balance()}")
        print(f"Federation ID input On-chain: {self.federation_id_input()}")
        print(f"Federation ID output On-chain: {self.federation_id_output()}")
        print(f"Kind input On-chain: {self.kind_id_input()}")
        print(f"Kind output On-chain: {self.kind_id_output()}")
        print(f"Type: {self.in_contracts_type()}, Hash Payment: {self.in_contracts_paymenthash()} for to the contract: {self.in_contracts_contract_id()}")
        print(f"Most recently block_times data: {self.most_recently_transaction()}")
        print(f"Max Block Height Vote: {self.block_height_vote()}")
        print(f"Top 10 Block Times and have more height vote: \n \n {self.transaction_inputs_block_times_top100()}")
    
    #Finished the consult    
    def close_connection(self):
        self.conn.close()

if __name__== '__main__':
    fedi_test = Test_FEDI()
    fedi_test.show_info()
