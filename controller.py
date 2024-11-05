from model import Model
from view import View

class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        while True:
            choice = self.show_menu()

            if choice == 1:
                self.show_currencies()    
            elif choice == 2:
                self.show_investments()
            elif choice == 3:
                self.show_owners_investments()
            elif choice == 4:
                self.show_users()
            elif choice == 5:
                self.show_wallets()
            
            elif choice == 6:
                self.update_currency()
            elif choice == 7:
                self.update_investment()
            elif choice == 8:
                self.update_contract()
            elif choice == 8:
                self.update_contract()
            elif choice == 9:
                self.update_user()
            
            elif choice == 11:
                self.add_currency()
            elif choice == 12:
                self.add_investment()
            elif choice == 13:
                self.add_contract()
            elif choice == 14:
                self.add_user()
            elif choice == 15:
                self.add_wallet()
            
            elif choice == 16:
                self.search_in_currency()
            elif choice == 17:
                self.search_in_investments()
            elif choice == 18:
                self.search_in_contracts()
            elif choice == 19:
                self.search_in_users()
            elif choice == 20:
                self.search_in_wallets()
            elif choice == 21:
                self.search_users_currencies()

            elif choice == 22:
                self.delete_currency()
            elif choice == 23:
                self.delete_investment()
            elif choice == 24:
                self.delete_contract()
            elif choice == 25:
                self.delete_users()
            elif choice == 26:
                self.delete_wallet()

            elif choice == 27:
                self.generate_currency()
            elif choice == 28:
                self.generate_contracts()
            elif choice == 29:
                self.generate_users()
            elif choice == 30:
                self.generate_wallets()
            
            elif choice == 31:
                break

    def show_menu(self):
        
        while True:

            self.view.show_message("\nMenu:")
            self.view.show_message("\n--- GET ---\n")
            self.view.show_message("1.Show currencies")
            self.view.show_message("2.Show investments")
            self.view.show_message("3.Show contracts")
            self.view.show_message("4.Show users")
            self.view.show_message("5.Show wallets")
            self.view.show_message("\n--- UPDATE ---\n")
            self.view.show_message("6.Update currency data")
            self.view.show_message("7.Update investments")
            self.view.show_message("8.Update contracts")
            self.view.show_message("9.Update users")
            self.view.show_message("10.Update wallets")
            self.view.show_message("\n--- ADD ---\n")
            self.view.show_message("11.Add currency")
            self.view.show_message("12.Add investment")
            self.view.show_message("13.Add contract")
            self.view.show_message("14.Add user")
            self.view.show_message("15.Add wallet")
            self.view.show_message("\n--- SEARCH IN ---\n")
            self.view.show_message("16.Search in currencies")
            self.view.show_message("17.Search in investments")
            self.view.show_message("18.Search in contracts")
            self.view.show_message("19.Search in users")
            self.view.show_message("20.Search in wallets")
            self.view.show_message("21.Search currencies by user")
            self.view.show_message("\n--- DELETE ---\n")
            self.view.show_message("22.Delete currency")
            self.view.show_message("23.Delete investment")
            self.view.show_message("24.Delete contract")
            self.view.show_message("25.Delete users")
            self.view.show_message("26.Delete wallet")
            self.view.show_message("\n--- GENERATE ---\n")
            self.view.show_message("27.Generate currencies")
            self.view.show_message("28.Generate contracts")
            self.view.show_message("29.Generate users")
            self.view.show_message("30.Generate wallets")
            
            self.view.show_message("\n31.Quit")

            try:
                choice = self.view.get_input("\nEnter your choice: ")
            except Exception as e:
                print("\nWrong input!\n")
                continue

            return choice
    
    # GET (SHOW)

    def show_currencies(self):
        try:
            start_id = self.view.get_input("\nEnter starting ID to show from: ")
            end_id = self.view.get_input("\nEnter ending currency ID to show: ")
            
        except Exception as e:
            print(f"Error occured: {e}")
            start_id = None
            end_id = None

        if start_id != None:
            currencies = self.model.get_currencies(start_id, end_id)
            self.view.show_currencies(currencies)

    def show_investments(self):
        try:
            start_id = self.view.get_input("\nEnter starting ID to show from: ")
            end_id = self.view.get_input("\nEnter ending currency ID to show: ")
            
        except Exception as e:
            print(f"Error occured: {e}")
            start_id = None
            end_id = None
        
        if start_id != None:
            investments = self.model.get_investments(start_id, end_id)
            self.view.show_investments(investments)

    def show_owners_investments(self):
        try:
            start_id = self.view.get_input("\nEnter starting ID to show from: ")
            end_id = self.view.get_input("\nEnter ending currency ID to show: ")
            
        except Exception as e:
            print(f"Error occured: {e}")
            start_id = None
            end_id = None

        if start_id != None:
            owners_investments = self.model.get_owners_investments(start_id, end_id)
            self.view.show_owners_investments(owners_investments)

    def show_users(self):
        try:
            start_id = self.view.get_input("\nEnter starting ID to show from: ")
            end_id = self.view.get_input("\nEnter ending currency ID to show: ")
            
        except Exception as e:
            print(f"Error occured: {e}")
            start_id = None
            end_id = None

        if start_id != None:
            users = self.model.get_users(start_id, end_id)
            self.view.show_users(users)

    def show_wallets(self):
        try:
            start_id = self.view.get_input("\nEnter starting ID to show from: ")
            end_id = self.view.get_input("\nEnter ending currency ID to show: ")
            
        except Exception as e:
            print(f"Error occured: {e}")
            start_id = None
            end_id = None

        if start_id != None:
            wallets = self.model.get_wallets(start_id, end_id)
            self.view.show_wallets(wallets)

    # UPDATE

    def update_currency(self):
        currency_id = self.view.get_currency_id()
        if currency_id != None:
            name, rate, quantity, wallet_id = self.view.get_currency_input()
            if wallet_id != None:
                self.model.update_currency(name, rate, quantity, wallet_id, currency_id)
        
    def update_investment(self):
        investment_id = self.view.get_investment_id()
        if investment_id != None:
            name, seller, price, annual_income, date, wallet_id, quantity = self.view.get_investment_input()
            if wallet_id != None:
                self.model.update_investment(
                    name,
                    seller,
                    price,
                    annual_income,
                    date,
                    wallet_id,
                    quantity,
                    investment_id
                )

    def update_contract(self):
        contract_id = self.view.get_contract_id()
        if contract_id != None:
            user_id, investment_id = self.view.get_contract_input()
            if user_id != None:
                self.model.update_contract(contract_id, user_id, investment_id)

    def update_user(self):
        user_id = self.view.get_user_id()
        if user_id != None:
            name, surname = self.view.get_user_input()
            if name != None:
                self.model.update_user(name, surname, user_id)

    def update_wallet(self):
        wallet_id = self.view.get_wallet_id()
        if wallet_id != None:
            status, user_id = self.view.get_wallet_input()
            if user_id != None:
                self.model.update_wallet(status, user_id, wallet_id)

    # ADD (CREATE)

    def add_currency(self):
        name, rate, quantity, wallet_id = self.view.get_currency_input()
        if name != None:
            self.model.add_currency(name, rate, quantity, wallet_id)

    def add_investment(self):
        name, seller, price, annual_income, date, wallet_id, quantity = self.view.get_investment_input()
        if wallet_id != None:
            self.model.add_investment(name, seller, price, annual_income, date, wallet_id, quantity)

    def add_contract(self):
        user_id, investment_id = self.view.get_contract_input()
        if user_id != None:
            self.model.add_contract(user_id, investment_id)

    def add_user(self):
        name, surname = self.view.get_user_input()
        if name != None:
            self.model.add_user(name, surname)

    def add_wallet(self):
        status, user_id = self.view.get_wallet_input()
        if user_id != None:
            self.model.add_wallet(status, user_id)

    # SEARCH

    def search_in_currency(self):
        choice = self.view.get_input("\nSearch by:\n1.ID\n2.Name\n3.Rate\n4.Quantity\n5.Wallet ID\nFor numeric data input must be like '5,9' (between 5 and 9)\n\nEnter your choice: ")
        request = self.view.get_request("\nEnter your search request: ")
        results = self.model.search_in_currency(request, choice)
        self.view.show_currencies(results)
    
    def search_in_investments(self):
        choice = self.view.get_input("\nSearch by:\n1.ID\n2.Name\n3.Seller\n4.Wallet ID\n5.Price'\n6.Annual income\n7.Quantity\nFor numeric data input must be like '5,9' (between 5 and 9)\n\nEnter your choice: ")
        request = self.view.get_request("\nEnter your search request: ")
        results = self.model.search_in_investments(request, choice)
        self.view.show_investments(results)

    def search_in_contracts(self):
        choice = self.view.get_input("\nSearch by:\n1.Contract ID\n2.User ID\n3.Investment ID\n\nEnter your choice: ")
        request = self.view.get_request("\nEnter your search request: ")
        results = self.model.search_in_contracts(request, choice)
        self.view.show_owners_investments(results)

    def search_in_users(self):
        choice = self.view.get_input("\nSearch by:\n1.User ID\n2.Name\n3.Surname\n\nEnter your choice: ")
        request = self.view.get_request("\nEnter your search request: ")
        results = self.model.search_in_users(request, choice)
        self.view.show_users(results)

    def search_in_wallets(self):
        choice = self.view.get_input("\nSearch by:\n1.Wallet ID\n2.Status\n3.Owner ID\n\nEnter your choice: ")
        request = self.view.get_request("\nEnter your search request: ")
        order = self.view.get_request("\nEnter field to order by (wallet_id, status, user_id): ")
        results = self.model.search_in_wallets(request, choice, order)
        self.view.show_wallets(results)

    def search_users_currencies(self):
        name, surname = self.view.get_users_currencies()
        if name != None:
            result = self.model.search_users_currencies(name, surname)
            self.view.show_users_currencies(result)

    # DELETE

    def delete_currency(self):
        try:
            start_id = self.view.get_input("\nEnter starting currency ID to remove: ")
            end_id = self.view.get_input("\nEnter ending currency ID to remove: ")
        
        except Exception as e:
            print(f"Error occured: {e}")
            start_id = None
            end_id = None

        if start_id != None:
            self.model.delete_currency(start_id, end_id)

    def delete_investment(self):
        try:
            start_id = self.view.get_input("\nEnter starting currency ID to remove: ")
            end_id = self.view.get_input("\nEnter ending currency ID to remove: ")
        
        except Exception as e:
            print(f"Error occured: {e}")
            start_id = None
            end_id = None

        if start_id != None:
            self.model.delete_investment(start_id, end_id)

    def delete_contract(self):
        try:
            start_id = self.view.get_input("\nEnter starting currency ID to remove: ")
            end_id = self.view.get_input("\nEnter ending currency ID to remove: ")
        
        except Exception as e:
            print(f"Error occured: {e}")
            start_id = None
            end_id = None

        if start_id != None:
            self.model.delete_contract(start_id, end_id)

    def delete_users(self):
        try:
            start_id = self.view.get_input("\nEnter starting currency ID to remove: ")
            end_id = self.view.get_input("\nEnter ending currency ID to remove: ")
        
        except Exception as e:
            print(f"Error occured: {e}")
            start_id = None
            end_id = None

        if start_id != None:
            self.model.delete_users_in_range(start_id, end_id)

    def delete_wallet(self):
        try:
            start_id = self.view.get_input("\nEnter starting currency ID to remove: ")
            end_id = self.view.get_input("\nEnter ending currency ID to remove: ")
        
        except Exception as e:
            print(f"Error occured: {e}")
            start_id = None
            end_id = None

        if start_id != None:
            self.model.delete_wallet(start_id, end_id)

    # Generate users

    def generate_users(self):
        quantity = self.view.get_input("\nEnter quantity of users to generate: ")
        self.model.generate_users(quantity)

    def generate_currency(self):
        quantity = self.view.get_input("\nEnter quantity of currencies to generate: ")
        self.model.generate_currency(quantity)

    def generate_wallets(self):
        quantity = self.view.get_input("\nEnter quantity of wallets to generate: ")
        self.model.generate_wallets(quantity)

    def generate_contracts(self):
        quantity = self.view.get_input("\nEnter quantity of contracts to generate: ")
        self.model.generate_contracts(quantity)