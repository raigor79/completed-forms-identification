import pytest
import asyncio

from db import Store


class TestStore():
    def setup(self):
        self.test_string = {'name': 'UserForm', 'phone': 'phone', 'e_mail': 'mail'}
        self.store = Store(host='172.23.0.1')
    
    def test_get_list_from_store(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.store.get_documents_from_db())
        assert self.store.list_records[0]['name'] == self.test_string['name']
        assert self.store.list_records[0]['phone'] == self.test_string['phone']
        assert self.store.list_records[0]['e_mail'] == self.test_string['e_mail']
