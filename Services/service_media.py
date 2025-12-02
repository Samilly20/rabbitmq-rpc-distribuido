import pika
import json

def media(data):
    valores = data["valores"]
    return {"resultado": sum(valores) / len(valores)}

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue="service_media")

def on_request(ch, method, props, body):
    data = json.loads(body)
    print("[MEDIA] Recebi:", data)

    resposta = media(data)

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
channel.basic_consume(queue="service_media", on_message_callback=on_request)

print(" [MEDIA] Aguardando requisições…")
channel.start_consuming()
