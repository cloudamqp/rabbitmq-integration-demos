import os, sys
from pika import URLParameters, BlockingConnection
from dotenv import load_dotenv

load_dotenv()

CLOUDAMQP_URL: str = os.getenv("CLOUDAMQP_URL")


params: URLParameters = URLParameters(CLOUDAMQP_URL)
connection: BlockingConnection = BlockingConnection(params)
print("[✅] Connection over channel established")

channel = connection.channel() 

def callback(ch, method, properties, body):
    print(f"[✅] Received #{ body }")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(
  prefetch_count=100
)

channel.basic_consume(
    "products",
    callback,
    auto_ack=False,
    arguments={"x-stream-offset": "first"}
)

try:
  print("[❎] Waiting for messages. To exit press CTRL+C")
  channel.start_consuming()
except Exception as e:
  print(f"Error: #{e}")
  try:
    sys.exit(0)
  except SystemExit:
    os._exit(0)