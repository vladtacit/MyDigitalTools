# Users and roles

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

```sql
CREATE USER name WITH PASSWORD 'pass' SUPERUSER;
```

## [~]
