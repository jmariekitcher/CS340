#Example Python Code to Insert a Document
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS, HOST, PORT, DB, COL):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        self.USER = 'aacuser'
        self.PASS = 'jacquelinkitcher'
        self.HOST = 'nv-desktop-services.apporto.com'
        self.PORT = 33975
        self.DB = 'AAC'
        self.COL = 'animals'
        #
        # Initialize Connection
        #     
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            try:
                result = self.database.animals.insert_one(data)
                if result.acknowledged:
                    return True
                else: 
                    return False
            except Exception as e:
                print(f"Error occurred: {e}")
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")


# Create method to implement the R in CRUD.
    def read_in(self, query):
        cursor = self.database.animals.find(query)
        animalq = []
        for animal in cursor:
            animalq.append(animal)
        return animalq

    def update(self, query, update_animal):
        if query is not None and update_animal is not None:
            try:
                result = self.collection.update_one(query, {"$set": update_animal})
                return result
            except Exception as e:
                print(f"Error: {e}")
                return 0
        else:
            raise Exception("Nothing to update: query or update_animal is None")
            
            
#Create method to implement the D in CRUD
    def delete(self, query):
        if query is not None:
            try:
                result = self.collection.delete_one(query)
                return result
            except Exception as e:
                print(f"Error: {e}")
                return 0
        else:
            raise Exception("Not found.")        
