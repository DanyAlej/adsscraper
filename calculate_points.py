from pymongo import MongoClient
from bson import json_util, ObjectId
import json
from datetime import date

def month_string_to_number(string):
    m = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr':4,
        'may':5,
        'jun':6,
        'jul':7,
        'aug':8,
        'sep':9,
        'oct':10,
        'nov':11,
        'dec':12
        }
    s = string.strip()[:3].lower()

    try:
        out = m[s]
        return out
    except:
        raise ValueError('Not a month')

client = MongoClient()
db = client['ads']
collections = db.list_collections()

for current_collection in collections:
    print(current_collection)
    docs = db[current_collection['name']].find()
    collection = db[current_collection['name']]
    print(collection)
    print(docs)
    for doc in docs:
        json_ad = json.loads(json_util.dumps(doc))
        date_retrieved = json_ad['date_retrieved'].split('/')
        date_retrieved= date(int(date_retrieved[2]), int(date_retrieved[1]), int(date_retrieved[0]))

        date_started_running = json_ad['started_running'].split(' ')
        print(json_ad['started_running'])
        try:
            date_started_running = date(int(date_started_running[5].replace(',','')), int(month_string_to_number(date_started_running[3].replace(',',''))), int(date_started_running[4].replace(',', '')))
            delta_time = date_retrieved - date_started_running
            score = delta_time.days + 10
            if score > 90: 
                score = 90
            print(score)
            adId = json_ad['_id']['$oid']
            ad2 = collection.find_one({'_id': ObjectId(adId)})
            if ad2 is not None:
                ad2['score'] = score
                collection.save(ad2)
        except:
            pass
        
