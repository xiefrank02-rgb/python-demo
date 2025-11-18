import requests
from pymongo import MongoClient
import pprint
client = MongoClient(
    "mongodb://user_phl_var_core:a5nrFCTtVUa_MBaq@fat.aliyun-phl-data1.mongodb.ppdaidb.com:7906,fat.aliyun-phl-data2.mongodb.ppdaidb.com:7906,fat.aliyun-phl-etl.mongodb.ppdaidb.com:7906/")

db = client['phl_var_core']

def get_varx_vars(db):
    collection = db['vars']
    projection = {"_id": 0, "name": 1}  # _id: 0 表示不返回 _id 字段，name 和 age 字段返回
    varx_vars = []
    results = collection.find({},projection)
    for document in results:
        varx_vars.append(document['name'])
    # pprint.pprint(varx_vars)
    client.close()
    return varx_vars

def get_irs_vars():
    url = 'http://fat-irs.juanhandapi.com/api/getDefinedVars'
    response = requests.get(url)
    resp_json = response.json()
    irs_vars = [var for var in resp_json.keys()]
    # pprint.pprint(irs_vars)
    return irs_vars


if __name__ == '__main__':
    varx_vars = get_varx_vars(db)
    irs_var =  get_irs_vars()
    intersection = list(set(varx_vars) & set(irs_var))  # 或者 set(list1).intersection(list2)
    pprint.pprint(intersection)  #  (顺序不确定)
