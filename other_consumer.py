import pika, sys, os

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='other')

    file = open("other_customer.csv", "a")

    def callback(ch, method, properties, body):
        file.write(str(body))
        file.write("\n")

    channel.basic_consume(queue='other', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            f.close()
            sys.exit(0)
        except SystemExit:
            f.close()
            os._exit(0)
