# Zabbix

[Definitions](https://www.zabbix.com/documentation/current/en/manual/definitions)

[Определения](https://www.zabbix.com/documentation/7.0/ru/manual/definitions)

## Install and configure Zabbix 6.0 for Debian 12

[Get Zabbix](https://www.zabbix.com/download?zabbix=6.0&os_distribution=debian&os_version=12&components=server_frontend_agent&db=pgsql&ws=nginx)

1. Install Zabbix repository

```bash
# wget https://repo.zabbix.com/zabbix/6.0/debian/pool/main/z/zabbix-release/zabbix-release_latest_6.0+debian12_all.deb
# dpkg -i zabbix-release_latest_6.0+debian12_all.deb
# apt update
...
Hit:9 https://repo.zabbix.com/zabbix/6.0/debian bookworm InRelease
```

2. Install Zabbix server, frontend, agent

```bash
# apt install zabbix-server-pgsql zabbix-frontend-php php8.2-pgsql zabbix-nginx-conf zabbix-sql-scripts zabbix-agent
```

3. Create and configure database

```bash
# sudo -u postgres createuser --pwprompt zabbix
# sudo -u postgres createdb -O zabbix zabbix
```

Edit file /etc/zabbix/zabbix_server.conf

```
DBPassword=password
```

4. Configure PHP for Zabbix frontend

dit file /etc/zabbix/nginx.conf uncomment and set 'listen' and 'server_name' directives.

```
# listen 8080;
# server_name example.com;
```

5. Start Zabbix server and agent processes

```bash
# systemctl restart zabbix-server zabbix-agent nginx php8.2-fpm
# systemctl enable zabbix-server zabbix-agent nginx php8.2-fpm
```

Default user name Admin with password zabbix.

## fping

[fping](https://ru.wikipedia.org/wiki/Fping)

[Zabbix: Simple checks](https://www.zabbix.com/documentation/current/en/manual/config/items/itemtypes/simple_checks)

## Zabbix + Kafka

[Zabbix + Kafka](https://www.zabbix.com/ru/integrations/kafka)

[kafka-monitoring](https://github.com/helli0n/kafka-monitoring)
>Kafka monitoring using zabbix and burrow

[ZABBIX as a Kafka Consumer](https://www.michelvanderzijden.nl/zabbix-as-a-kafka-consumer/)

[Kafka Connector](https://git.zabbix.com/projects/ZT/repos/kafka-connector/browse)
>Kafka connector for Zabbix server

## Streaming to external systems

[Streaming to external systems](https://www.zabbix.com/documentation/current/en/manual/config/export/streaming)

[Receiver](https://git.zabbix.com/projects/ZT/repos/receiver/browse)
>Experimental connector for data streaming (PoC)

## Mix

[Подключаем производственный календарь в Zabbix](https://habr.com/ru/articles/488504/)
>Во множестве организаций существуют внутренние производственные календари, на расписании которых работают технологические и бизнес-процессы. Системы мониторинга работающие автономно, довольно часто настроены на мониторинг бизнес-процессов в рамках обычной деятельности предприятия и имеют жёсткое фиксированное расписание по контролю информационных потоков и данных, сопровождающих бизнес процессы. В моменты изменения ежедневного рабочего расписания, администраторам требуются ручные действия по изменению логики мониторинга. Как заставить Zabbix использовать производственный календарь? Рассмотрим несколько вариантов поподробнее.

## [~]
