import json
import os

DB_FILE = 'database.json'

def load_database():
    if not os.path.exists(DB_FILE):
        with open(DB_FILE,'w') as db:
            json.dump({"customers":[], "admins":[], "staff":[]},db)
    
    with open(DB_FILE,'r') as db:
        return json.load(db)

def save_database(data):
    with open(DB_FILE,'w') as db:
        json.dump(data,db, indent=4)


def find_customer(account_number):
    db = load_database()
    for customer in db['customers']:
        if customer['account_number'] == account_number:
            return customer
        
    return None


def update_customer(account_number,new_data):
    db = load_database()
    for i, customer in enumerate(db['customers']):
        if customer['account_number'] == account_number:
            db['customers'][i] = new_data
            save_database(db)
            return True
    
    return False

    

