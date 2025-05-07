# Apache Kafka

[Apache Kafka](https://kafka.apache.org/)

Note: ZooKeeper is marked deprecated in release 3.5. ZooKeeper is removed in Apache Kafka 4.0.

[Почему KRaft заменил ZooKeeper](https://habr.com/ru/companies/slurm/articles/685694/)

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

## Kafka service at home

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

## Python

[Событийный заказ: Python и Kafka](https://habr.com/ru/companies/otus/articles/883996/)

[KafkaProducer](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaProducer.html)

&#9635;
