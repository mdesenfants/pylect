import os, uuid, sys

from flask import Flask
from azure.storage import CloudStorageAccount
from azure.storage.table import TableService, Entity
from azure.storage.queue import QueueService, QueueMessage

app = Flask(__name__)

account_name = "pylectstorage"
account_key = os.environ["STORAGE_KEY"]

account = CloudStorageAccount(account_name=account_name, account_key=account_key)

def count_hits():
    return 0

@app.route('/', methods=['GET'])
def atomic():
    count = count_hits()
    return str(count) # effectively a json number

@app.route('/increment', methods=['POST'])
def increment():
    return '0', 202

# used if we're running the app directly 
if __name__ == "__main__":
    app.run(host='0.0.0.0')
