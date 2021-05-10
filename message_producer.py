import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='us')
channel.queue_declare(queue='cc')
channel.queue_declare(queue='other')

with open('example_csv.csv', 'r', encoding="utf8") as file:
    for customer in file.readlines():
        eval = customer.split(',')
        if eval[8] == "United States":
            channel.basic_publish(exchange='', routing_key='us', body=customer)
        elif eval[7] != "":
            channel.basic_publish(exchange='', routing_key='cc', body=customer)
        else:
            channel.basic_publish(exchange='', routing_key='other', body=customer)

print(" [x] Data successfully parsed.")
connection.close()
