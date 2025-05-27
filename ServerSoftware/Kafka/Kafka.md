# Apache Kafka

[Apache Kafka](https://kafka.apache.org/)

Note: ZooKeeper is marked deprecated in release 3.5. ZooKeeper is removed in Apache Kafka 4.0.

[Почему KRaft заменил ZooKeeper](https://habr.com/ru/companies/slurm/articles/685694/)

[Apache Kafka: основы технологии](https://habr.com/ru/companies/slurm/articles/550934/)

[Управление отставанием lag в Kafka Consumers: как не просто замерить, а стабилизировать](https://habr.com/ru/companies/otus/articles/905804/)

[DLQ-first: учим Kafka-консьюмера падать красиво и поднимать поток за секунды](https://habr.com/ru/companies/otus/articles/905810/)

## Apache Kafka Quickstart

[Apache Kafka Quickstart](https://kafka.apache.org/quickstart)

0. Install Java

```bash
sudo apt install default-jre
sudo apt install default-jdk
```

1. Get Kafka

    * [Download](https://kafka.apache.org/downloads) the latest Kafka release and extract it

2. Generate a Cluster UUID

```bash
KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"
```

3. Format Log Directories

```bash
$ bin/kafka-storage.sh format --standalone -t $KAFKA_CLUSTER_ID -c config/server.properties
Formatting dynamic metadata voter directory /tmp/kraft-combined-logs with metadata.version 4.0-IV3
```

4. Start the Kafka Server

```bash
bin/kafka-server-start.sh config/server.properties
```
Stop the Kafka broker with Ctrl-C

---

[How to Install Apache Kafka on Debian 11/10](https://tecadmin.net/install-apache-kafka-debian/)

[Running Kafka Without ZooKeeper: A Step-by-Step Guide](https://risingwave.com/blog/running-kafka-without-zookeeper-a-step-by-step-guide/)

### Kafka service at home

Specify the directory where the log files will be stored (config/server.properties):

```
# A comma separated list of directories under which to store log files
log.dirs=/home/vlad/Work/System/kafka-kraft-combined-logs
```

```bash
mkdir /home/vlad/Work/System/kafka-kraft-combined-logs
cd /home/vlad/Work/System/kafka
KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"
bin/kafka-storage.sh format --standalone -t $KAFKA_CLUSTER_ID -c config/server.properties
mkdir -p ~/.config/systemd/user
```

Create Kafka service unit in ~/.config/systemd/user

[Kafka service unit](./kafka.service)

```bash
systemctl --user start kafka
systemctl --user status kafka
systemctl --user stop kafka
```

Add the alias into .bash_aliases

```
alias userctl='systemctl --user'
```

### Topics

1. Create a topic to store some events
```bash
$ cd /home/vlad/Work/System/kafka
$ bin/kafka-topics.sh --create --topic mix-events --bootstrap-server localhost:9092
Created topic mix-events.
```

2. Get topic's info
```bash
$ bin/kafka-topics.sh --describe --topic mix-events --bootstrap-server localhost:9092
Topic: mix-events	TopicId: FbHCms58QTWdhiilvYk0xA	PartitionCount: 1	ReplicationFactor: 1	Configs: segment.bytes=1073741824
	Topic: mix-events	Partition: 0	Leader: 1	Replicas: 1	Isr: 1	Elr: 	LastKnownElr:
```
 
3. Write some events into the topic
```bash
$ bin/kafka-console-producer.sh --topic mix-events --bootstrap-server localhost:9092
>1. Event one;
>2. Event two;
>3. Finish.
>^C
```

4. Read the events
```bash
bin/kafka-console-consumer.sh --topic mix-events --from-beginning --bootstrap-server localhost:9092
1. Event one;
2. Event two;
3. Finish.
^C
Processed a total of 3 messages
```

## Python

[Событийный заказ: Python и Kafka](https://habr.com/ru/companies/otus/articles/883996/)

[KafkaProducer](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaProducer.html)

[KafkaConsumer](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html)

### confluent-kafka

```bash
sudo apt install python3-confluent-kafka
```

[Confluent's Python Client for Apache Kafka. PyPI](https://docs.confluent.io/kafka-clients/python/current/overview.html)

[Installing Packages](https://packaging.python.org/en/latest/tutorials/installing-packages/)

[Загрузка файлов](https://pypi.org/project/confluent-kafka/#files)

```bash
$ python3 -m venv tutorial_env
$ source tutorial_env/bin/activate
$ pip install confluent_kafka-2.10.0-cp311-cp311-manylinux_2_28_x86_64.whl
Installing collected packages: confluent-kafka
Successfully installed confluent-kafka-2.10.0
$ pip list
Package         Version
--------------- -----------
confluent-kafka 2.10.0
```

---
[Что выбрать Python-разработчику для работы с Kafka: confluent-kafka vs kafka-python](https://bigdataschool.ru/blog/news/kafka/confluent-kafka-vs-kafka-python.html)

[Использование Kafka с Python: Consumer и Producer](https://sky.pro/wiki/python/ispolzovanie-kafka-s-python-consumer-i-producer/)

[Продюсеры и консьюмеры с Apache Kafka в Python](https://habr.com/ru/companies/otus/articles/789896/)

[Поднимаем потоковый сервис Kafka на Python](https://habr.com/ru/articles/880700/)

## Golang

[Go Client for Apache Kafka](https://docs.confluent.io/kafka-clients/go/current/overview.html)

[confluent-kafka-go. GitHub](https://github.com/confluentinc/confluent-kafka-go) - Confluent's Apache Kafka Golang client

[Подключение Go к Apache Kafka](https://selectel.ru/blog/tutorials/go-apache-kafka/)

[Простейший пример kafka + golang](https://habr.com/ru/articles/764582/)

## Message Format

[APACHE KAFKA: Message Format](https://www.getorchestra.io/guides/apache-kafka-message-format)

[JSON vs бинарные форматы: почему Kafka выбирает скорость?](https://habr.com/ru/companies/otus/articles/911012/)

&#9635;
