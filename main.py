import requests
import json
import os
from dotenv import load_dotenv
from telethon import TelegramClient, events
import datetime as dt
import topics

# Access the environment variables
load_dotenv()
data_platform_api_key = os.getenv('DATA_PLATFORM_API_KEY')
api_id = os.getenv('TG_API_ID')
api_hash = os.getenv('TG_API_HASH')
db_id = os.getenv('DB_ID')


def insert_data(
        text: str,
        topic_id: str,
        topic_name: str,

):
    url = 'https://data.dev.agione.ai/api/v1/data/operate'
    headers = {
        'api-key': data_platform_api_key,
        'Content-Type': 'application/json'
    }

    created_at = dt.datetime.now()
    data = {
        "db_id": db_id,
        "sql_query": f"INSERT INTO brc20scaner (text, topic_id, topic_name, created_at) VALUES ('{text}', {topic_id}, '{topic_name}', '{created_at}');"
    }

    # 将数据转换为 JSON 格式
    json_data = json.dumps(data)

    # 发送 POST 请求
    response = requests.post(url, headers=headers, data=json_data)

    # 打印响应结果
    print(response.status_code)
    print(response.text)


client = TelegramClient('session_1', api_id, api_hash)
client.start()


@client.on(events.NewMessage(chats='@brc20scaner/'))
async def my_event_handler(event):
    text = event.raw_text
    print(">>>raw Message: ", )

    topic_id = -1
    # Check if the message belongs to a topic (forum)
    if hasattr(event.message, 'reply_to') and event.message.reply_to_msg_id:
        topic_id = event.message.reply_to_msg_id
        print(f">>>Topic ID: {topic_id}")
    else:
        print(">>>No topic ID in this message.")

    topic_name = topics.topic_dict.get(topic_id, "")
    insert_data(text, topic_id, topic_name)

    print("----------------------------------------------------------------------")


if __name__ == '__main__':
    client.start()
    client.run_until_disconnected()







