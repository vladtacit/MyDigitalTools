# consumer.py

import json
import logging
from kafka import KafkaConsumer
from typing import Any, Dict
import configparser
# dynaconf ???

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

config = configparser.ConfigParser()
config.read('settings.ini')

def get_kafka_consumer(topic: str, group_id: str) -> KafkaConsumer:
    """
    Инициализация KafkaConsumer с ручным подтверждением.
    """
    try:
        consumer = KafkaConsumer(
            topic,
            bootstrap_servers=['localhost:9092'],
            group_id=group_id,
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            #auto_offset_reset='earliest',
            #enable_auto_commit=False  # Ручное подтверждение для большей надежности
        )
        logger.info("KafkaConsumer успешно инициализирован!")
        return consumer
    except Exception as e:
        logger.error(f"Ошибка инициализации KafkaConsumer: {e}")
        raise

def process_event(event: Dict[str, Any]) -> None:
    """
    Логика обработки события.
    """
    try:
        event_id = event.get("id")
        event_status = event.get("status")
        logger.info(f"Event {event_id} status: {event_status}")

        if event_status == "CREATED":
            logger.info(f"начинаем обработку.")
        elif event_status == "CANCELLED":
            logger.info(f"Отмена.")
        else:
            logger.warning(f"Событие {event_id} имеет неизвестный статус: {event_status}")
    except Exception as e:
        logger.error(f"Ошибка при обработке события {event.get('event_id')}: {e}")

if __name__ == "__main__":
    consumer = get_kafka_consumer(config['Kafka']['Topic'], config['Kafka']['Consumer_group_id'])
    try:
        for message in consumer:
            logger.info(f"Получено сообщение: {message.value}")
            process_event(message.value)
            # consumer.commit()  # Ручное подтверждение после успешной обработки
    except KeyboardInterrupt:
        logger.info("Остановка KafkaConsumer...")
    finally:
        consumer.close()
