from motor.motor_asyncio import AsyncIOMotorClient


class Store():
    def __init__(self, name_store: str ='mongodb', name_db: str ='dbforms', host: str ='0.0.0.0', port: str ='27018'):
        client = AsyncIOMotorClient(f'{name_store}://{host}:{port}')
        self.db = client[f'{name_db}']
    
    async def get_documents_from_db(self, name_collection: str ='typeforms'):
        self.list_records = []
        self.collection = self.db[name_collection]
        async for doc in self.collection.find():
            self.list_records.append(doc)

    async def find_document_in_db(self, name_collection: str ='typeform', parametr_find: str = None):
        self.collection = self.db[name_collection]
        document = await self.collection.find_one(parametr_find)
        self.document = document


if __name__ == "__main__":
    pass
