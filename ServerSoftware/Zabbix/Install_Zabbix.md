# Install and configure Zabbix

0. [Install PostgreSQL(./PostgreSql/PostgreSql.md)]

[Source: Download and install Zabbix](https://www.zabbix.com/download?zabbix=6.4&os_distribution=debian&os_version=12&components=server_frontend_agent&db=pgsql&ws=nginx)

1. Install Zabbix repository

    ```bash
    # wget https://repo.zabbix.com/zabbix/6.4/debian/pool/main/z/zabbix-release/zabbix-release_6.4-1+debian12_all.deb
    # dpkg -i zabbix-release_6.4-1+debian12_all.deb
    # apt update
    ```

2. Install Zabbix server, frontend, agent

    ```bash
    # apt install zabbix-server-pgsql zabbix-frontend-php php8.2-pgsql zabbix-nginx-conf zabbix-sql-scripts zabbix-agent
    ```

3. Create initial database

    ```bash
    # sudo -u postgres createuser --pwprompt zabbix
    # sudo -u postgres createdb -O zabbix zabbix
    ```

5. import initial schema and data

    ```bash
    # zcat /usr/share/zabbix-sql-scripts/postgresql/server.sql.gz | sudo -u zabbix psql zabbix
    ```

6. Configure the database for Zabbix server

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
    # systemctl restart zabbix-server zabbix-agent nginx php8.2-fpm
    # systemctl enable zabbix-server zabbix-agent nginx php8.2-fpm
    ```

9. Show open ports

    ```bash
    # netstat -tulpn | grep LISTEN
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

----

ToDo:

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
