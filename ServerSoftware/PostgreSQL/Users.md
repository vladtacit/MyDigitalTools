# Users and roles

[Роли базы данных](https://postgrespro.ru/docs/postgresql/current/user-manag)

[createuser](https://postgrespro.ru/docs/postgresql/current/app-createuser)

[CREATE ROLE](https://postgrespro.ru/docs/postgresql/current/sql-createrole)

[ALTER ROLE](https://postgrespro.ru/docs/postgresql/current/sql-alterrole)

[Управление пользователями в PostgreSQL](https://timeweb.cloud/tutorials/postgresql/upravlenie-polzovatelyami-v-postgresql)

[Как создать пользователя PostgreSQL: инструкция](https://timeweb.cloud/tutorials/postgresql/kak-sozdat-polzovatelya-postgresql)

```bash
sudo -i -u postgres psql
```

```
postgres=# \du
                                   List of roles
 Role name |                         Attributes                         | Member of 
-----------+------------------------------------------------------------+-----------
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}
 zabbix    |                                                            | {}

postgres=# 
```

Create a Superuser
```sql
CREATE USER name WITH PASSWORD 'pass' SUPERUSER;
select * from pg_user;
```

Create an ordinary user and add needed privileges to him: 
```sql
CREATE USER another_name WITH PASSWORD 'pass';
ALTER ROLE name WITH CREATEDB;
ALTER ROLE name WITH CREATEROLE;
```

## [~]
