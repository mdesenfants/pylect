import os, uuid, sys

from flask import Flask
from azure.cosmosdb.table import TableService, Entity
from azure.storage.queue import QueueService, QueueMessage

app = Flask(__name__)

account_name = "pylectstorage"
account_key = os.environ["STORAGE_KEY"]

global table_name
table_name='atomic'
global partition_key
partition_key='hits'

global table_service
table_service = TableService(account_name=account_name, account_key=account_key)
table_service.create_table(table_name, fail_on_exist=False, timeout=None)

def count_hits():
    results = table_service.query_entities(table_name, filter="PartitionKey eq '" + partition_key +"'")
    tally = len(list(map(lambda x: 1, results)))
    return tally

def insert_hit():
    record = {'PartitionKey': partition_key, 'RowKey': str(uuid.uuid4()), 'count': 1}
    table_service.insert_or_replace_entity(table_name, record)

@app.route('/', methods=['GET'])
def atomic():
    count = count_hits()
    return str(count)

@app.route('/increment', methods=['POST'])
def increment():
    insert_hit()
    return '1', 202

# used if we're running the app directly 
if __name__ == "__main__":
    app.run(host='0.0.0.0')
