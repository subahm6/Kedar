from pymongo import MongoClient

mongodb_client = MongoClient(host="localhost:27017", connect=True)
database = mongodb_client["admin"]
collection = database.get_collection("user_credentials")



def startup_db_client(collection,document):
    
    result = collection.insert_one(document)
    print(f"Document inserted with ID: {result.inserted_id}")

def get_data(collection,user,passw):
    docs = collection.find()
    for i in docs:
        if i['user'] == user and i['pass'] == passw:
            return True
        else:
            return False
    
print(get_data(collection,'singhfuleshwar552@gmail.com', 'subhamsinghhkiller'))
