# producer.py

import json
import uuid
from datetime import datetime
from kafka import KafkaProducer
import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def get_kafka_producer() -> KafkaProducer:
    """
    Инициализируем KafkaProducer с базовыми настройками.
    В продакшене нужно добавить обработку ошибок подключения, настройки безопасности и т.д.
    """
    try:
        producer = KafkaProducer(
            bootstrap_servers=['localhost:9092'],
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
            retries=5,               # Повторная отправка при сбоях
            linger_ms=10,            # задержка перед отправкой
            max_request_size=1048576 # Ограничение размера запроса (1MB)
        )
        logger.info("KafkaProducer успешно инициализирован!")
        return producer
    except Exception as e:
        logger.error(f"Ошибка инициализации KafkaProducer: {e}")
        raise

if __name__ == "__main__":
    producer = get_kafka_producer()
    event: Dict[str, Any] = {
        "id": str(uuid.uuid1()),
        "ts": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "SUCCESS"
    }
    try:
        meta = producer.send('mix-events', event)
        result = meta.get(timeout=10)
        logger.info(f"Сообщение отправлено: топик {result.topic}, партиция {result.partition}")
    except Exception as e:
        logger.error(f"Ошибка отправки сообщения: {e}")
    finally:
        producer.flush()
