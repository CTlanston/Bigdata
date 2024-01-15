import json
import pymongo
import os

# MongoDB Connection
client = pymongo.MongoClient('mongodb://docdbmaster:GBS$msba$2024@msba2024-production-instance-cluster.cluster-cqxikovybdnm.us-east-2.docdb.amazonaws.com:27017/?replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false')
netid='agu567'
mydatabase = netid + "_database"
mycollection = netid + "_collection"

##Specify the database to be used
db = client[mydatabase]

##Specify the collection to be used
col = db[mycollection]

# File path
file_path = r'/home/ubuntu/json_award.json'

# Check if the file exists
if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for record in data:
        awardYear = record.get('awardYear')
        # print(f"Extracted awardYear: {awardYear}, Type: {type(awardYear)}")  # Debug print statement   # it shows that awardYear is str not interger
        if awardYear:
            record['_id'] = int(awardYear)
        col.update_one({'_id': record['_id']}, {'$set': record}, upsert=True)

    print("Running query 1 ")
    result1 = col.find({'awardYear': '2019'}, {'_id': 1, 'category.en': 1, 'laureates.knownName.en': 1})

    for res in result1:
        year = res['_id']
        category = res['category']['en']
        laureates = [l['knownName']['en'] for l in res['laureates']]
        for laureate in laureates:
            print("In the Year %s Nobel award for %s was given to %s"%(year,category,laureate))

    print("Running query 2 ")
    result2 = col.find({'category.en': 'Physics'}, {'id': 1, 'laureates.knownName.en': 1})
    for res in result2:
        year = res['_id']
        laureates = [l['knownName']['en'] for l in res['laureates']]
        for laureate in laureates:
            print("In the Year %s Nobel award for %s was given to %s"%(year,'Physics',laureate))
client.close()




