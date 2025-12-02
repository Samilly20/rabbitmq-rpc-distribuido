import pika
import json

BANCO = {
    1: "João",
    2: "Maria",
    3: "Ana",
    4: "Carlos"
}

def buscar(data):
    id_user = data["id"]
    nome = BANCO.get(id_user, "Não encontrado")
    return {"resultado": nome}

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue="service_busca")

def on_request(ch, method, props, body):
    data = json.loads(body)
    print("[BUSCA] Recebi:", data)

    resposta = buscar(data)

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
channel.basic_consume(queue="service_busca", on_message_callback=on_request)

print(" [BUSCA] Aguardando requisições…")
channel.start_consuming()
