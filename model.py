import psycopg2, random
from math import ceil, sqrt
from psycopg2 import Error

import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()  # Record the end time
        elapsed_time = (end_time - start_time) * 1000 # Calculate elapsed time in milliseconds
        
        # Output the result and elapsed time
        print(f"Function '{func.__name__}' executed in {elapsed_time:.4f} milliseconds")
        
        return result  # Return the result of the function
    return wrapper

class Model:

    def __init__(self):
        self.conn = psycopg2.connect(
            dbname = '',
            user = '',
            password = '#',
            host = '',
            port = 
        )

    #  GET

    @timeit
    def get_currencies(self, start_id, end_id):
        c = self.conn.cursor()
        c.execute(f'SELECT * FROM currency WHERE currency_id BETWEEN {start_id} AND {end_id} ORDER BY currency_id ASC')
        return c.fetchall()

    @timeit
    def get_investments(self, start_id, end_id):
        c = self.conn.cursor()
        c.execute(f'SELECT * FROM investments WHERE investment_id BETWEEN {start_id} AND {end_id} ORDER BY investment_id ASC')
        return c.fetchall()

    @timeit
    def get_owners_investments(self, start_id, end_id):
        c = self.conn.cursor()
        c.execute(f'SELECT * FROM owners_investments WHERE contract_id BETWEEN {start_id} AND {end_id} ORDER BY contract_id ASC')
        return c.fetchall()

    @timeit
    def get_users(self, start_id, end_id):
        c = self.conn.cursor()
        c.execute(f'SELECT * FROM users WHERE user_id BETWEEN {start_id} AND {end_id} ORDER BY user_id ASC')
        return c.fetchall()

    @timeit
    def get_wallets(self, start_id, end_id):
        c = self.conn.cursor()
        c.execute(f'SELECT * FROM wallets WHERE wallet_id BETWEEN {start_id} AND {end_id} ORDER BY wallet_id ASC')
        return c.fetchall()

    # UPDATE

    @timeit
    def update_currency(self, name, rate, quantity, wallet_id, currency_id):
        c = self.conn.cursor()
        try:
            c.execute('UPDATE currency SET name=\'%s\', rate=%f, quantity=%f, wallet_id=%d WHERE currency_id=%d' % (name, rate, quantity, wallet_id, currency_id))
            self.conn.commit()
            rows_updated = c.rowcount
            print(f"\n{rows_updated} currencies updated.\n")
        except Error as e:
            self.conn.rollback()
            print(f"An error occurred: {e}")
        finally:
            c.close()

    @timeit
    def update_investment(self, name, seller, price, annual_income, date, wallet_id, quantity, investment_id):
        c = self.conn.cursor()
        try:
            c.execute(f'UPDATE investments SET name=\'{name}\', seller=\'{seller}\', price={price}, annual_income={annual_income}, date=\'{date}\', wallet_id={wallet_id}, quantity={quantity} WHERE investment_id={investment_id}')
            self.conn.commit()
            rows_updated = c.rowcount
            print(f"\n{rows_updated} investments updated.\n")
        except Error as e:
            self.conn.rollback()
            print(f"An error occurred: {e}")
        finally:
            c.close()

    @timeit
    def update_contract(self, contract_id, user_id, investment_id):
        c = self.conn.cursor()
        try:
            c.execute(f'UPDATE owners_investments SET user_id={user_id}, investment_id={investment_id} WHERE contract_id={contract_id}')
            self.conn.commit()
            rows_updated = c.rowcount
            print(f"\n{rows_updated} relations updated.\n")
        except Error as e:
            self.conn.rollback()
            print(f"An error occurred: {e}")
        finally:
            c.close()

    @timeit
    def update_user(self, name, surname, user_id):
        c = self.conn.cursor()
        try:
            c.execute(f'UPDATE users SET name=\'{name}\', surname=\'{surname}\' WHERE user_id={user_id}')
            self.conn.commit()
            rows_updated = c.rowcount
            print(f"\n{rows_updated} users updated.\n")
        except Error as e:
            self.conn.rollback()
            print(f"An error occurred: {e}")
        finally:
            c.close()

    @timeit
    def update_wallet(self, status, user_id, wallet_id):
        c = self.conn.cursor()
        try:
            c.execute(f'UPDATE wallets SET status={status}, user_id={user_id} WHERE wallet_id={wallet_id}')
            self.conn.commit()
            rows_updated = c.rowcount
            print(f"\n{rows_updated} wallets updated.\n")
        except Error as e:
            self.conn.rollback()
            print(f"An error occurred: {e}")
        finally:
            c.close()

    # ADD

    @timeit
    def add_currency(self, name, rate, quantity, wallet_id):
        c = self.conn.cursor()
        try:
            c.execute("SELECT MAX(currency_id) FROM currency")
            latest_id = c.fetchone()[0]
            c.execute(f'INSERT INTO currency (currency_id, name, rate, quantity, wallet_id) VALUES ({latest_id + 1}, \'{name}\', {rate}, {quantity}, {wallet_id})')
            self.conn.commit()
            rows_updated = c.rowcount
            print(f"\n{rows_updated} currency added.\n")
        except Error as e:
            print(f"An error occurred: {e}")
            self.conn.rollback()
        finally:
            c.close()         

    @timeit
    def add_investment(self, name, seller, price, annual_income, date, wallet_id, quantity):
        c = self.conn.cursor()
        try:
            c.execute("SELECT MAX(investment_id) FROM investments")
            latest_id = c.fetchone()[0]
            c.execute(f'INSERT INTO investments (investment_id, name, seller, price, annual_income, date, wallet_id, quantity) VALUES ({latest_id + 1}, \'{name}\', \'{seller}\', {price}, {annual_income}, \'{date}\', {wallet_id}, {quantity})')
            self.conn.commit()
            rows_updated = c.rowcount
            print(f"\n{rows_updated} investments added.\n")
        except Error as e:
            print(f"An error occurred: {e}")
            self.conn.rollback()
        finally:
            c.close()

    @timeit
    def add_contract(self, user_id, investment_id):
        c = self.conn.cursor()
        try:
            c.execute("SELECT MAX(contract_id) FROM owners_investments")
            latest_id = c.fetchone()[0]
            c.execute(f'INSERT INTO owners_investments (contract_id, user_id, investment_id) VALUES ({latest_id + 1}, {user_id}, {investment_id})')
            self.conn.commit()
            rows_updated = c.rowcount
            print(f"\n{rows_updated} contracts added.\n")
        except Error as e:
            print(f"An error occurred: {e}")
            self.conn.rollback()
        finally:
            c.close()

    @timeit
    def add_user(self, name, surname):
        c = self.conn.cursor()
        try:
            c.execute("SELECT MAX(user_id) FROM users")
            latest_id = c.fetchone()[0]
            c.execute(f'INSERT INTO users (user_id, name, surname) VALUES ({latest_id + 1}, \'{name}\', \'{surname}\')')
            self.conn.commit()
            rows_updated = c.rowcount
            print(f"\n{rows_updated} users added.\n")
        except Error as e:
            self.conn.rollback()
            print(f"An error occurred: {e}")
        finally:
            c.close()

    @timeit
    def add_wallet(self, status, user_id):
        c = self.conn.cursor()
        try:
            c.execute("SELECT MAX(wallet_id) FROM wallets")
            latest_id = c.fetchone()[0]
            c.execute(f'INSERT INTO wallets (wallet_id, status, user_id) VALUES ({latest_id + 1}, {status}, {user_id})')
            self.conn.commit()
            rows_updated = c.rowcount
            self.conn.rollback()
            print(f"\n{rows_updated} wallets added.\n")
        except Error as e:
            print(f"An error occurred: {e}")
            
        c.close()

    # SEARCH

    @timeit
    def search_in_currency(self, request, choice):
        c = self.conn.cursor()
        try:
            if choice == 1: # id
                c.execute(f'SELECT * FROM currency WHERE currency_id = {request}')
            elif choice == 2: # name
                c.execute(f'SELECT * FROM currency WHERE name LIKE \'%{request}%\' ORDER BY currency_id ASC')
            elif choice == 3: # rate
                values = [item.strip() for item in request.split(',')]
                c.execute(f'SELECT * FROM currency WHERE rate BETWEEN {values[0]} AND {values[1]} ORDER BY currency_id ASC')
            elif choice == 4: # quantity
                values = [item.strip() for item in request.split(',')]
                c.execute(f'SELECT * FROM currency WHERE quantity BETWEEN {values[0]} AND {values[1]} ORDER BY currency_id ASC')
            if choice == 5: # wallet id
                c.execute(f'SELECT * FROM currency WHERE wallet_id = {request} ORDER BY currency_id ASC')
            results = c.fetchall()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.conn.rollback()
            results = None  

        c.close()
        return results

    @timeit
    def search_in_investments(self, request, choice):
        c = self.conn.cursor()
        try:
            if choice == 1: # ID
                c.execute(f'SELECT * FROM investments WHERE investment_id = {request}')
            elif choice == 2: # Name
                c.execute(f'SELECT * FROM investments WHERE name LIKE \'%{request}%\' ORDER BY investment_id ASC')
            elif choice == 3: # Seller
                c.execute(f'SELECT * FROM investments WHERE seller LIKE \'%{request}%\' ORDER BY investment_id ASC')
            elif choice == 4: # Wallet ID
                c.execute(f'SELECT * FROM investments WHERE wallet_id = {request} ORDER BY investment_id ASC')
            elif choice >= 5 and choice <= 7: 
                values = [item.strip() for item in request.split(',')]
                if choice == 5: # price
                    c.execute(f'SELECT * FROM investments WHERE price BETWEEN {values[0]} AND {values[1]} ORDER BY investment_id ASC')
                elif choice == 6: # annual income
                    c.execute(f'SELECT * FROM investments WHERE annual_income BETWEEN {values[0]} AND {values[1]} ORDER BY investment_id ASC')
                elif choice == 7: # quantity
                    c.execute(f'SELECT * FROM investments WHERE quantity BETWEEN {values[0]} AND {values[1]} ORDER BY investment_id ASC')
            results = c.fetchall()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.conn.rollback()
            results = None  

        c.close()
        return results

    @timeit
    def search_in_contracts(self, request, choice):
        c = self.conn.cursor()
        try:
            if choice == 1: # ID
                c.execute(f'SELECT * FROM owners_investments WHERE contract_id = {request}')
            elif choice == 2: # user id
                c.execute(f'SELECT * FROM owners_investments WHERE user_id = {request} ORDER BY contract_id ASC')
            elif choice == 3: # investment id
                c.execute(f'SELECT * FROM owners_investments WHERE investment_id = {request} ORDER BY contract_id ASC')
            results = c.fetchall()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.conn.rollback()
            results = None  
        
        c.close()
        return results

    @timeit
    def search_in_users(self, request, choice):
        c = self.conn.cursor()
        try:
            if choice == 1: # ID
                c.execute(f'SELECT * FROM users WHERE user_id = {request}')
            elif choice == 2: # Name
                c.execute(f'SELECT * FROM users WHERE name LIKE \'%{request}%\' ORDER BY user_id ASC')
            elif choice == 3: # Surname
                c.execute(f'SELECT * FROM users WHERE surname LIKE \'%{request}%\' ORDER BY user_id ASC')
            results = c.fetchall()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.conn.rollback()
            results = None  
        
        c.close()
        return results

    @timeit
    def search_in_wallets(self, request, choice, order):
        c = self.conn.cursor()
        try:
            if choice == 1: # ID
                c.execute(f'SELECT * FROM wallets WHERE wallet_id = {request}')
            elif choice == 2: # status
                if request.lower() in ['opened', 'open', '1', 'yes', 'active', 'on', 'true']:
                    request = 'true'
                elif request.lower() in ['closed', 'close', '0', 'no', 'off', 'false']:
                    request = 'false'
                c.execute(f'SELECT * FROM wallets WHERE status = {request} ORDER BY {order} ASC')
            elif choice == 3: # user_id
                c.execute(f'SELECT * FROM wallets WHERE user_id = {request} ORDER BY {order} ASC')
            results = c.fetchall()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.conn.rollback()
            results = None
        c.close()
        return results
    
    # SEARCH IN users and users at the same time

    @timeit
    def search_users_currencies(self, name, surname):
        c = self.conn.cursor()
        try:
            c.execute(f"""SELECT currency.name, currency.quantity, users.name, users.surname
            FROM currency
            JOIN wallets ON currency.wallet_id = wallets.wallet_id
            JOIN users ON users.user_id = wallets.user_id
            WHERE users.name LIKE \'%{name}%\' AND users.surname LIKE \'%{surname}%\';""")
            results = c.fetchall()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.conn.rollback()
            results = None
        c.close()
        return results

    # DELETE

    @timeit
    def delete_currency(self, start_id, end_id):
        try:
            c = self.conn.cursor()
            c.execute(f'DELETE FROM currency WHERE currency_id BETWEEN {start_id} AND {end_id}')
            self.conn.commit()
            print("\nDeleted successfully! ")
        except Exception as e:
            print(f"An error occurred: {e}")
            self.conn.rollback()

    @timeit
    def delete_investment(self, start_id, end_id):
        try:
            c = self.conn.cursor()
            c.execute(f'DELETE FROM investments WHERE investment_id BETWEEN {start_id} AND {end_id}')
            self.conn.commit()
            print("\nDeleted successfully! ")
        except Exception as e:
            print(f"An error occurred: {e}")
            self.conn.rollback()

    @timeit
    def delete_contract(self, start_id, end_id):
        try:
            c = self.conn.cursor()
            c.execute(f'DELETE FROM owners_investments WHERE contract_id BETWEEN {start_id} AND {end_id}')
            self.conn.commit()
            print("\nDeleted successfully! ")
        except Exception as e:
            print(f"An error occurred: {e}")
            self.conn.rollback()

    @timeit
    def delete_users_in_range(self, start_id, end_id):
        c = self.conn.cursor()
        try:
            c.execute("DELETE FROM users WHERE user_id BETWEEN %s AND %s", (start_id, end_id))
            self.conn.commit()
            print("\nDeleted successfully! ")
        except Exception as e:
            print(f"An error occurred: {e}")
            self.conn.rollback()

    @timeit
    def delete_wallet(self, start_id, end_id):
        try:
            c = self.conn.cursor()
            c.execute(f'DELETE FROM wallets WHERE wallet_id BETWEEN {start_id} AND {end_id}')
            self.conn.commit()
            print("\nDeleted successfully! ")
        except Exception as e:
            print(f"An error occurred: {e}")
            self.conn.rollback()

    # GENERATE DATA

    @timeit
    def generate_users(self, quantity):
        # Get the current max user_id
        c = self.conn.cursor()
        c.execute("SELECT COALESCE(MAX(user_id), 0) FROM users")  # Use 0 if there are no users
        max_user_id = c.fetchone()[0]
        next_user_id = max_user_id + 1

        # Prepare name list
        name_list = ""
        
        with open('names.txt', 'r') as names:
            for counter in range(ceil(sqrt(quantity))):
                name = names.readline()
                if not name: break
                name_list += "'" + name.strip() + "', "

        name_list = name_list[:-2] # Deleting " ," in the end

        # Prepare surname list
        surname_list = ""
        with open('surnames.txt', 'r') as surnames:
            for counter in range(ceil(sqrt(quantity))):
                surname = surnames.readline()
                if not surname: break
                surname_list += "'" + surname.strip().capitalize() + "', "

        surname_list = surname_list[:-2]

        # Insert users with incremented user_id and unique name-surname pairs
        try:
            c.execute(f"""WITH max_id AS (
                      SELECT COALESCE(MAX(user_id), 0) AS current_max_id FROM users),
                      generated_users AS (
                      SELECT 
                      (ROW_NUMBER() OVER () + (SELECT current_max_id FROM max_id)) AS user_id,
                      first_name AS name, 
                      last_name AS surname
                      FROM unnest(array[{name_list}]) AS first_name
                      CROSS JOIN unnest(array[{surname_list}]) AS last_name
                      LIMIT {quantity})
                      INSERT INTO users (user_id, name, surname)
                      SELECT user_id, name, surname
                      FROM generated_users;
                      """)
            self.conn.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.conn.rollback()

    @timeit
    def generate_currency(self, quantity):
        c = self.conn.cursor()
        try:
            c.execute("SELECT MAX(wallet_id) FROM wallets")
            max_wallet_id = c.fetchone()[0]
            c.execute(f"""WITH max_id AS (
                    SELECT COALESCE(MAX(currency_id), 0) AS current_max_id FROM currency
                ),
                generated_currency AS (
                    SELECT 
                        (ROW_NUMBER() OVER () + (SELECT current_max_id FROM max_id)) AS currency_id,
                        chr(trunc(65 + random() * 26)::int) ||
                        chr(trunc(65 + random() * 26)::int) ||
                        chr(trunc(65 + random() * 26)::int) AS name,
                        ROUND((random() * 100)::numeric, 2) AS rate,
                        ROUND((random() * 1000)::numeric, 2) AS quantity,
                        trunc(random() * {max_wallet_id} + 1)::int AS wallet_id
                    FROM generate_series(1, {quantity})
                )
                INSERT INTO currency (currency_id, name, rate, quantity, wallet_id)
                SELECT currency_id, name, rate, quantity, wallet_id
                FROM generated_currency
                LIMIT {quantity}
                """)
            self.conn.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.conn.rollback()
            
    @timeit
    def generate_wallets(self, quantity):
        c = self.conn.cursor()
        try:
            # Get the maximum wallet_id from the wallets table
            c.execute("SELECT COALESCE(MAX(wallet_id), 0) FROM wallets")
            max_wallet_id = c.fetchone()[0]
            
            # Generate wallets using a common table expression
            c.execute(f"""
                WITH max_id AS (
                    SELECT COALESCE(MAX(user_id), 0) AS current_max_id FROM users
                ),
                generated_wallets AS (
                    SELECT 
                        (ROW_NUMBER() OVER () + {max_wallet_id}) AS wallet_id,
                        (RANDOM() < 0.5) AS status,  -- Randomly generates true or false
                        ((random()*(SELECT current_max_id FROM max_id))) AS user_id
                    FROM generate_series(1, {quantity})
                )
                INSERT INTO wallets (wallet_id, status, user_id)
                SELECT wallet_id, status, user_id
                FROM generated_wallets
                LIMIT {quantity}
            """)
            self.conn.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.conn.rollback()
        finally:
            c.close()

    @timeit
    def generate_contracts(self, quantity):
        c = self.conn.cursor()
        try:
            # Get the maximum contract_id from the contracts table
            c.execute("SELECT COALESCE(MAX(contract_id), 0) FROM owners_investments")
            max_contract_id = c.fetchone()[0]

            # Get the maximum user_id from the users table
            c.execute("SELECT COALESCE(MAX(user_id), 0) FROM users")
            max_user_id = c.fetchone()[0]

            # Get the maximum investment_id from the investments table
            c.execute("SELECT COALESCE(MAX(investment_id), 0) FROM investments")
            max_investment_id = c.fetchone()[0]

            # Generate contracts using a common table expression
            c.execute(f"""
                WITH generated_contracts AS (
                    SELECT 
                        (ROW_NUMBER() OVER () + {max_contract_id}) AS contract_id,
                        FLOOR(RANDOM() * {max_user_id} + 1)::int AS user_id,
                        FLOOR(RANDOM() * {max_investment_id} + 1)::int AS investment_id
                    FROM generate_series(1, {quantity})
                )
                INSERT INTO owners_investments (contract_id, user_id, investment_id)
                SELECT contract_id, user_id, investment_id
                FROM generated_contracts
                LIMIT {quantity}
            """)
            self.conn.commit()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.conn.rollback()
        finally:
            c.close()  # Ensure the cursor is closed after the operation