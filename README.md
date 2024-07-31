# Fedimint Observer Challenge

## Description

You are provided with a SQLite file, [fedimint-observer.db](https://www.google.com/url?sa=D&q=https://fedi-public-snapshots.s3.amazonaws.com/fedimint-observer.db.gz&ust=1722548700000000&usg=AOvVaw0KxkkgALiCcEefdnRrS9rc&hl=pt-BR&source=gmail) , from a [Fedimint Observer](https://github.com/douglaz/fedimint-observer/) configured to monitor the [Bitcoin Principles](https://github.com/fedimint/awesome-fedimint?tab=readme-ov-file#mainnet) [Fedimint federation](https://github.com/fedimint/fedimint). Your task is to answer the following questions using this database.

## Basic Challenges

Use the `fedimint-observer.db` file to answer the following questions:

- How much Bitcoin was pegged-in to this federation?
- How much Bitcoin was pegged-out from this federation?
- What is the current on-chain balance of this federation?

## Extra Challenges (Optional)

**Extra Challenge 1:**

- Run the Fedimint Observer and calculate the above metrics for the Freedom One federation.

**Extra Challenge 2:**

- Explore the additional data available in the Fedimint Observer database and provide an overview of the insights that can be inferred from this publicly accessible information.

> **Note:** The extra challenges are independent of each other and are optional.

## Getting Started

### Prepare the Environment

1. Install necessary dependencies by running the following command:

    ```bash
    pip install -r requirements.txt
    ```

    This will install all required packages, including `pandas==2.2.2`.


### Download and Setup the Database

1. **Download the `fedimint-observer.db` file:**
   -  [Download fedimint-observer.db](https://www.google.com/url?sa=D&q=https://fedi-public-snapshots.s3.amazonaws.com/fedimint-observer.db.gz&ust=1722548700000000&usg=AOvVaw0KxkkgALiCcEefdnRrS9rc&hl=pt-BR&source=gmail)

2. **Place the database file in the correct directory:**
   - Move the downloaded `fedimint-observer.db` file into the `Test_DataEngineer_Fedi` folder. The folder structure should look like this:

    ```
    Test_DataEngineer_Fedi/
    ├── fedimint-observer.db
    ├── requirements.txt
    ├── fedi_data_engineer.py
    ├── test_unit.py
    ```

3. Set up the environment to access and query the SQLite database.

### Run Queries

1. Use SQL tools or Python libraries such as `sqlite3` to query the database and answer the Basic Challenges.

### For Extra Challenges

1. Set up and run the Fedimint Observer for the Freedom One federation.
2. Analyze additional data to provide insights into the database.

### Git clone

1. Open cmd/powersheel/gitBash
2. git clone https://github.com/RamonNicolas/Teste_FEDI.git
3. cd Test_DataEngineer_Fedi
4. Run Archive

### Run Archive

To run the provided test archive, execute the following Python script:

```bash

python fedi_data_engineer.py
```

### Run unit tests

```bash
python test_unit.py
```

