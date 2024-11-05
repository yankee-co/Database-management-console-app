class View:

    def show_currencies(self, currencies):
        if currencies != None:
            print("Currencies:")
            for currency in currencies:
                print(f"\nID: {currency[0]}\nName: {currency[1]}\nRate: {currency[2]}\nQuantity: {currency[3]}\nOn wallet №{currency[4]}")

    def show_investments(self, investments):
        if investments != None:
            print("Investments:")
            for investment in investments:
                print(f"\nID: {investment[0]}\nName: {investment[1]}\nSeller: {investment[2]}\nPrice: {investment[3]}\nAnnual income: {investment[4]}\nDate: {investment[5]}\nBought from wallet no. {investment[6]}\nQuantity: {investment[7]}")

    def show_owners_investments(self, owners_investments):
        if owners_investments != None:
            print("Owners and their investments:")
            for owners_investment in owners_investments:
                print(f"\nContract ID: {owners_investment[0]}\nUser with ID {owners_investment[1]} owns investments with ID: {owners_investment[2]}")

    def show_users(self, users):
        if users != None:
            print("Users:")
            for user in users:
                print(f"\nUser ID: {user[0]}\nName: {user[1]}\nSurname: {user[2]}")

    def show_wallets(self, wallets):
        if wallets != None:
            print("Wallets:")
            for wallet in wallets:
                print(f"\nWallet ID: {wallet[0]}\nOpen: {wallet[1]}, Owner ID: {wallet[2]}")

    def get_currency_id(self):
        try:
            currency_id = int(input("\nEnter currency ID: "))
        except Exception as e:
            print("\nWrong input!")
            currency_id = None
        return currency_id
    
    def get_currency_input(self):
        try:
            name = input("\nEnter name: ")
            rate = float(input("\nEnter rate: "))
            quantity = float(input("\nEnter quantity: "))
            wallet_id = int(input("\nEnter wallet ID: "))
        except Exception as e:
            print("\nWrong input!")
            return None, None, None, None
        return name, rate, quantity, wallet_id

    def get_investment_id(self):
        try:
            investment_id = int(input("\nEnter investment ID: "))
        except Exception as e:
            print("\nWrong input!")
            investment_id = None
        return investment_id

    def get_investment_input(self):
        try:
            name = input("\nEnter name: ")
            seller = input("\nEnter seller company name: ")
            price = float(input("\nEnter investment price: "))
            annual_income = float(input("\nEnter annual income ($): "))
            date = input("\nEnter date (YEAR-MONTH-DAY HOURS:MINUTES:SECONDS+TIME_ZONE): ")
            wallet_id = int(input("\nEnter wallet ID: "))
            quantity = int(input("\nEnter quantity: "))
        except Exception as e:
            print("\nWrong input!\n")
            return None, None, None, None, None, None, None
        return name, seller, price, annual_income, date, wallet_id, quantity

    def get_contract_id(self):
        try:
            contract_id = int(input("\nEnter contract ID: "))
        except Exception as e:
            print("\nWrong input!\n")
            contract_id = None
        return contract_id

    def get_user_id(self):
        try:
            user_id = int(input("\nEnter user ID: "))
        except Exception as e:
            print("\nWrong input!\n")
            return None
        return user_id

    def get_user_input(self):
        try:
            name = input("\nEnter name: ")
            surname = input("\nEnter surname: ")
        except Exception as e:
            print("\nWrong input!\n")
            return None, None
        return name, surname

    def get_contract_input(self):
        try:
            user_id = int(input("\nEnter user ID as a part of contract: "))
            ivestment_id = int(input("\nEnter investment ID as a part of contract: "))
        except Exception as e:
            print("\nWrong input!\n")
            user_id = None
            ivestment_id = None
        return user_id, ivestment_id

    def get_wallet_id(self):
        try:
            wallet_id = int(input("\nEnter wallet ID: "))
        except Exception as e:
            print("\nWrong input!\n")
            wallet_id = None
        return wallet_id

    def get_wallet_input(self):
        try:
            status = input("\nOpen/Close wallet (open/yes/close/no etc...): ").lower() in ["open", "yes", "1", "true"]
            user_id = int(input("\nEnter new owner ID: "))
        except Exception as e:
            print("\nWrong input!\n")
            return None, None
        return status, user_id

    def get_users_currencies(self):
        try:
            name = input("\nEnter user name (partially possible or nothing): ")
            surname = input("\nEnter user surname (partially possible or nothing): ")
        except Exception as e:
            print("\nWrong input!\n")
            name = None
            surname = None
        return name, surname

    def show_users_currencies(self, data):
        if data != None:
            for fetch in data:
                print(f"\n{fetch[2]} {fetch[3]} has {fetch[1]} {fetch[0]}")

    def show_message(self, message):
        print(message)

    def get_input(self, input_message):
        return int(input(input_message))

    def get_request(self, input_message):
        return input(input_message)