from kafka import KafkaConsumer

class DataProcessing:
    def __init__(self, topic):
        self.consumer = KafkaConsumer(topic)

    def process_data(self):
        for message in self.consumer:
            print('Received message:', message.value)

# Example usage
if __name__ == '__main__':
    dp = DataProcessing('your_topic_name')
    dp.process_data()
