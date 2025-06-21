# PostgreSQL

[PostgreSQL](https://www.postgresql.org/)

[PostgreSQL Documentation](https://www.postgresql.org/docs/current/index.html)

## Install (Debian)

[PostgreSql](https://wiki.debian.org/PostgreSql)

Search Debian packages to find the list of possibilities:
```bash
# apt search postgresql
```

Install:
```bash
# apt install postgresql
The following additional packages will be installed:
    libcommon-sense-perl
    libjson-perl
    libjson-xs-perl
    libllvm14
    libpq5
    libsensors-config
    libsensors5
    libtypes-serialiser-perl
    libxslt1.1
    libz3-4
    logrotate
    postgresql-15
    postgresql-client-15
    postgresql-client-common
    postgresql-common
    ssl-cert
    sysstat
```

Check PostgreSQL status:
```bash
# systemctl status postgresql
```

User access:
```bash
$ sudo -u postgres psql
```

## Install (RHEL)

[Getting started with PostgreSQL on Linux](https://www.redhat.com/en/blog/postgresql-setup-use-cases)

[Linux downloads (Red Hat family)](https://www.postgresql.org/download/linux/redhat/)

[Установка PostgreSQL на Red Hat Enterprise Linux](https://victorz.ru/202109091472)

## TimescaleDB

### Detect TimescaleDB extension

```sql
SELECT extversion INTO current_timescaledb_version_full FROM pg_extension WHERE extname = 'timescaledb';
```

```sql
SELECT count(extversion) FROM pg_extension WHERE extname = 'timescaledb';
```

## psql

[psql (PostgreSQL client) tool install on RHEL - Database Administrators Stack Exchange](https://dba.stackexchange.com/questions/298872/psql-postgresql-client-tool-install-on-rhel)
>On RedHat, and compatible systems, in order to install just the client only, the command is:
```bash
sudo yum install postgresql
```
>For a full-blown server install (should you require it in the future), the command is:
```bash
sudo yum install postgresql-server
```
>You can back out either of the commands above by issuing the command:
```bash
sudo yum remove <package name>
```
>uninstall your PostgreSQL client tools:
```bash
sudo yum remove postgresql 
```

## [~]
