# Install and configure Zabbix

0. [Install PostgreSQL(./PostgreSql/PostgreSql.md)]

[Source: Download and install Zabbix 6.4](https://www.zabbix.com/download?zabbix=6.4&os_distribution=debian&os_version=12&components=server_frontend_agent&db=pgsql&ws=nginx)

1. Install Zabbix repository

```bash
wget https://repo.zabbix.com/zabbix/6.4/debian/pool/main/z/zabbix-release/zabbix-release_6.4-1+debian12_all.deb
dpkg -i zabbix-release_6.4-1+debian12_all.deb
apt update
```
2. Install Zabbix server, frontend, agent

```bash
 apt install zabbix-server-pgsql zabbix-frontend-php php8.2-pgsql zabbix-nginx-conf zabbix-sql-scripts zabbix-agent
```
3. Create initial database

```bash
sudo -u postgres createuser --pwprompt zabbix
sudo -u postgres createdb -O zabbix zabbix
```

4. import initial schema and data

```bash
 zcat /usr/share/zabbix-sql-scripts/postgresql/server.sql.gz | sudo -u zabbix psql zabbix
```

5. Configure the database for Zabbix server

Edit file /etc/zabbix/zabbix_server.conf

```
DBPassword=password
```

7. Configure PHP for Zabbix frontend

Edit file /etc/zabbix/nginx.conf uncomment and set 'listen' and 'server_name' directives.

```
listen 8080;
server_name example.com;
```

8. Start Zabbix server and agent processes

```bash
systemctl enable zabbix-server zabbix-agent php8.2-fpm
systemctl restart nginx
systemctl start zabbix-server zabbix-agent php8.2-fpm
```

9. Show open ports

```bash
netstat -tulpn | grep LISTEN
```

10. Configure Zabbix

[Login and configuring user](https://www.zabbix.com/documentation/6.4/en/manual/quickstart/login)

```
http://localhost:8080
```

![ Zabbix welcome screen](ZabbixWelcomeScreen.png)

11. Login as Zabbix superuser

Enter the **user name** Admin with **password** zabbix to log in as a **Zabbix superuser**.

12. Add new users

## Upgrade procedure

[Upgrade procedure](https://www.zabbix.com/documentation/7.0/en/manual/installation/upgrade)

[Обновление Zabbix 6.0 до 7.0](https://serveradmin.ru/obnovlenie-zabbix-6-0-do-7-0/)

[Source: Download and install Zabbix](https://www.zabbix.com/download?zabbix=7.0&os_distribution=debian&os_version=12&components=server_frontend_agent&db=pgsql&ws=nginx)

1. Remove old (6.4) repository 

```bash
systemctl stop zabbix-server zabbix-agent php8.2-fpm
rm -Rf /etc/apt/sources.list.d/zabbix.list
```

2. Install 7.0 repository

```bash
wget https://repo.zabbix.com/zabbix/7.0/debian/pool/main/z/zabbix-release/zabbix-release_latest_7.0+debian12_all.deb
dpkg -i zabbix-release_latest_7.0+debian12_all.deb
apt update
```

3. Upgrade 6.4 -> 7.0

```bash
apt install --only-upgrade zabbix-server-pgsql zabbix-frontend-php php8.2-pgsql zabbix-nginx-conf zabbix-sql-scripts zabbix-agent
systemctl restart nginx
systemctl start zabbix-server zabbix-agent php8.2-fpm
tail -f /var/log/zabbix/zabbix_server.log

 10491:20250604:214550.018 completed 99% of database upgrade
 10491:20250604:214550.032 completed 100% of database upgrade
 10491:20250604:214550.052 database upgrade fully completed
```

Надо сохранить настройки соединения с БД в файле /etc/zabbix/zabbix_server.conf. Иначе получим такую ошибку:

```
The Zabbix database version does not match current requirements. Your database version: 6040000. Required version: 7000000. Please contact your system administrator.
```

4. Проверяем подключение к UI Zabbix и удаляем установочный файл

```bash
rm zabbix-release_latest_7.0+debian12_all.deb
```

### WebDriver

В конфиге добавился раздел "Browser monitoring".

## Database creation

[Database creation](https://www.zabbix.com/documentation/current/en/manual/appendix/install/db_scripts)

[Создание базы данных](https://www.zabbix.com/documentation/7.0/ru/manual/appendix/install/db_scripts)

## ToDo:

- Study WebDriver
   * [WebDriver](https://www.selenium.dev/documentation/webdriver/)
   * [WebDriver](https://developer.mozilla.org/en-US/docs/Web/WebDriver)
   * [Selenium](https://ru.wikipedia.org/wiki/Selenium)
   * [Что такое Selenium WebDriver?](https://habr.com/ru/articles/152971/)

- Add TimescaleDB
   [TimescaleDB setup](https://www.zabbix.com/documentation/6.4/en/manual/appendix/install/timescaledb)

- Configure Geomap
   [Geomap](https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/dashboards/widgets/geomap)

   [Памятник Якову Дьяченко](https://2gis.ru/khabarovsk/geo/4926507877138434/135.051177%2C48.473923?m=135.053663%2C48.473332%2F18) 48.473923° 135.051177°

 - Install Grafana

 - Setup HTTPS

 - Setup NTP

 - Study Nginx

## HTML Tidy

[HTML Tidy](https://ru.wikipedia.org/wiki/HTML_Tidy)

[libtidy-5.6.0-5.el8.x86_64.rpm](https://rhel.pkgs.org/8/epel-x86_64/libtidy-5.6.0-5.el8.x86_64.rpm.html)

&#9635;
