import pika
import json

def soma(data):
    return {"resultado": data["a"] + data["b"]}

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue="service_soma")

def on_request(ch, method, props, body):
    data = json.loads(body)
    print("[SOMA] Recebi:", data)

    resposta = soma(data)

    ch.basic_publish(
        exchange='',
        routing_key=props.reply_to,
        properties=pika.BasicProperties(
            correlation_id=props.correlation_id
        ),
        body=json.dumps(resposta)
    )
    ch.basic_ack(method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="service_soma", on_message_callback=on_request)

print(" [SOMA] Aguardando requisições…")
channel.start_consuming()
