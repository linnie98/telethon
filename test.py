################################ TEST ENV ################################
# import os
# from dotenv import load_dotenv

# # Load the environment variables from the .env file
# load_dotenv()
#
# # Access the environment variables
# data_plaform_api_key = os.getenv('DATA_PLATFORM_API_KEY')
# api_id = os.getenv('TG_API_ID')
# api_hash = os.getenv('TG_API_HASH')
#
# # Print or use the variables as needed
# print(f"data_plaform_api_key: {type(data_plaform_api_key)}")
# print(f"api_id: {type(api_id)}")
# print(f"api_hash: {api_hash}")



################################ TEST TOPIC ################################
# import topics

# topic_name = topics.topic_dict.get(94100, "")
# print(topic_name)



################################ TEST INSERT ################################
# import datetime as dt
# import json
# import requests
#
# def insert_data():
#     url = 'https://data.dev.agione.ai/api/v1/data/operate'
#     headers = {
#         'api-key': 'mc-n_KDyqNaDLJs6NOeoO-Y42rjtN_sJbV1kn7OqdBvIu0fMNxqrp1_P4f05Ns1a1EJ',
#         'Content-Type': 'application/json'
#     }
#
#     created_at = dt.datetime.now()
#     data = {
#         "db_id": "449a6897-b3c9-4b01-a22a-fee1df723235",
#         "sql_query": f"INSERT INTO brc20scaner (text, topic_id, topic_name, created_at) VALUES ('test', 123, 'TEST', '{created_at}');"
#     }
#
#     # 将数据转换为 JSON 格式
#     json_data = json.dumps(data)
#
#     # 发送 POST 请求
#     response = requests.post(url, headers=headers, data=json_data)
#
#     # 打印响应结果
#     print(response.status_code)
#     print(response.text)
#
# insert_data()



################################ TEST SEARCH ################################
import requests
import json

def retrieve_data():
    url = 'https://data.dev.agione.ai/api/v1/data/operate'
    headers = {
        'api-key': 'mc-n_KDyqNaDLJs6NOeoO-Y42rjtN_sJbV1kn7OqdBvIu0fMNxqrp1_P4f05Ns1a1EJ',
        'Content-Type': 'application/json'
    }
    topic_id = 425110
    data = {
        "db_id": "449a6897-b3c9-4b01-a22a-fee1df723235",
        "sql_query": f"SELECT * FROM brc20scaner WHERE topic_id={topic_id}"
    }

    # 将数据转换为 JSON 格式
    json_data = json.dumps(data)

    # 发送 POST 请求
    response = requests.post(url, headers=headers, data=json_data)

    # 打印响应结果
    print(response.status_code)
    # print(response.text)

    rows = []

    try:
        rows = response.json()['data']['executed_result']['query_result']['rows']
    except Exception as e:
        print(">>>e", e)
    return rows


data = retrieve_data()
print(">>>data: ", data)