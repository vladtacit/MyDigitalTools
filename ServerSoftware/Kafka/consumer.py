# consumer.py

import json
import logging
from kafka import KafkaConsumer
from typing import Any, Dict

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def get_kafka_consumer(topic: str, group_id: str = "order_consumers") -> KafkaConsumer:
    """
    Инициализация KafkaConsumer с ручным подтверждением.
    """
    try:
        consumer = KafkaConsumer(
            topic,
            bootstrap_servers=['localhost:9092'],
            group_id=group_id,
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            auto_offset_reset='earliest',
            enable_auto_commit=False  # Ручное подтверждение для большей надежности
        )
        logger.info("KafkaConsumer успешно инициализирован!")
        return consumer
    except Exception as e:
        logger.error(f"Ошибка инициализации KafkaConsumer: {e}")
        raise

def process_order_event(event: Dict[str, Any]) -> None:
    """
    Логика обработки события заказа.
    """
    try:
        order_id = event.get("order_id")
        status_event = event.get("status")
        logger.info(f"Обрабатываю заказ {order_id} со статусом {status_event}")

        if status_event == "CREATED":
            logger.info(f"Заказ {order_id} подтвержден – начинаем обработку платежа.")
            # Можно добавить вызов функции подтверждения заказа или уведомления другого сервиса
        elif status_event == "CANCELLED":
            logger.info(f"Заказ {order_id} отменён – запускаем компенсационные транзакции.")
            # Здесь реализуйте логику отмены и компенсационных транзакций
        else:
            logger.warning(f"Заказ {order_id} имеет неизвестный статус: {status_event}")
    except Exception as e:
        logger.error(f"Ошибка при обработке заказа {event.get('order_id')}: {e}")

if __name__ == "__main__":
    consumer = get_kafka_consumer("orders_topic")
    try:
        for message in consumer:
            logger.info(f"Получено сообщение: {message.value}")
            process_order_event(message.value)
            consumer.commit()  # Ручное подтверждение после успешной обработки
    except KeyboardInterrupt:
        logger.info("Остановка KafkaConsumer...")
    finally:
        consumer.close()
