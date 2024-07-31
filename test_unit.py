import pytest
import sqlite3
import datetime
import pandas as pd
from fedi_data_engineer import Test_FEDI  # Substitua 'your_module' pelo nome do módulo onde a classe Test_FEDI está definida

@pytest.fixture(scope='module')
def setup_db():
    # Set up a test database in memory
    conn = sqlite3.connect(':memory:')  # Using an in-memory database for testing
    cursor = conn.cursor()

    # Create schema and populate with test data
    cursor.execute('''CREATE TABLE transactions (
                        federation_id INTEGER,
                        amount_msat INTEGER,
                        kind TEXT
                      )''')
    cursor.execute('''CREATE TABLE transaction_inputs (
                        federation_id INTEGER,
                        amount_msat INTEGER,
                        kind TEXT
                      )''')
    cursor.execute('''CREATE TABLE transaction_outputs (
                        federation_id INTEGER,
                        amount_msat INTEGER,
                        kind TEXT
                      )''')
    cursor.execute('''CREATE TABLE ln_contracts (
                        type TEXT,
                        payment_hash TEXT,
                        contract_id TEXT
                      )''')
    cursor.execute('''CREATE TABLE block_times (
                        block_height INTEGER,
                        timestamp INTEGER
                      )''')
    cursor.execute('''CREATE TABLE block_height_votes (
                        height_vote INTEGER
                      )''')

    # Insert test data
    cursor.execute("INSERT INTO transaction_inputs VALUES (1, 100000, 'input')")
    cursor.execute("INSERT INTO transactions VALUES (1, 100000, 'input')")
    cursor.execute("INSERT INTO transaction_outputs VALUES (1, 50000, 'output')")
    cursor.execute("INSERT INTO ln_contracts VALUES ('type1', 'hash1', 'contract1')")
    cursor.execute("INSERT INTO block_times VALUES (1, 1712332271)")
    cursor.execute("INSERT INTO block_height_votes VALUES (1)")

    conn.commit()

    # Provide the connection and cursor to the tests
    yield conn, cursor

    conn.close()

def test_pegged_in(setup_db):
    conn, cursor = setup_db
    fedi = Test_FEDI()
    fedi.conn = conn
    fedi.cursor = cursor
    assert fedi.pegged_in() == 100000

def test_pegged_out(setup_db):
    conn, cursor = setup_db
    fedi = Test_FEDI()
    fedi.conn = conn
    fedi.cursor = cursor
    assert fedi.pegged_out() == 50000

def test_current_balance(setup_db):
    conn, cursor = setup_db
    fedi = Test_FEDI()
    fedi.conn = conn
    fedi.cursor = cursor
    assert fedi.current_balance() == 50000

def test_federation_id_input(setup_db):
    conn, cursor = setup_db
    fedi = Test_FEDI()
    fedi.conn = conn
    fedi.cursor = cursor
    assert fedi.federation_id_input() == 1

def test_federation_id_output(setup_db):
    conn, cursor = setup_db
    fedi = Test_FEDI()
    fedi.conn = conn
    fedi.cursor = cursor
    assert fedi.federation_id_output() == 1

def test_kind_id_input(setup_db):
    conn, cursor = setup_db
    fedi = Test_FEDI()
    fedi.conn = conn
    fedi.cursor = cursor
    assert fedi.kind_id_input() == 'input'

def test_kind_id_output(setup_db):
    conn, cursor = setup_db
    fedi = Test_FEDI()
    fedi.conn = conn
    fedi.cursor = cursor
    assert fedi.kind_id_output() == 'output'

def test_in_contracts_type(setup_db):
    conn, cursor = setup_db
    fedi = Test_FEDI()
    fedi.conn = conn
    fedi.cursor = cursor
    assert fedi.in_contracts_type() == 'type1'

def test_in_contracts_paymenthash(setup_db):
    conn, cursor = setup_db
    fedi = Test_FEDI()
    fedi.conn = conn
    fedi.cursor = cursor
    assert fedi.in_contracts_paymenthash() == 'hash1'

def test_in_contracts_contract_id(setup_db):
    conn, cursor = setup_db
    fedi = Test_FEDI()
    fedi.conn = conn
    fedi.cursor = cursor
    assert fedi.in_contracts_contract_id() == 'contract1'

def test_most_recently_transaction(setup_db):
    conn, cursor = setup_db
    fedi = Test_FEDI()
    fedi.conn = conn
    fedi.cursor = cursor
    assert fedi.most_recently_transaction() == datetime.datetime.fromtimestamp(1712332271)

def test_block_height_vote(setup_db):
    conn, cursor = setup_db
    fedi = Test_FEDI()
    fedi.conn = conn
    fedi.cursor = cursor
    assert fedi.block_height_vote() == 1

def test_transaction_inputs_block_times_top100(setup_db):
    conn, cursor = setup_db
    fedi = Test_FEDI()
    fedi.conn = conn
    fedi.cursor = cursor
    df = fedi.transaction_inputs_block_times_top100()
    print(df)
    assert len(df) == 1
    assert df.iloc[0]['federation_id'] == 1
    assert df.iloc[0]['block_height'] == 1
    assert df.iloc[0]['height_vote'] == 1
    assert df.iloc[0]['amount_msat'] == 100000
