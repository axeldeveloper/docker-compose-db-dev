# Installation(with Ubuntu 18.04)

> $ docker pull oracleinanutshell/oracle-xe-11g

# Docker Compose

```yml
version: "3"

services:
  oracle-db:
    image: oracleinanutshell/oracle-xe-11g:latest
    ports:
      - 1521:1521
      - 5500:5500
```

# Quick Start

Run with 1521 port opened:

> $ docker run -d -p 49161:1521 oracleinanutshell/oracle-xe-11g
> ---Run this, if you want the database to be connected remotely:

> $ docker run -d -p 49161:1521 -e ORACLE_ALLOW_REMOTE=true oracleinanutshell/oracle-xe-11g
> ---For performance concern, you may want to disable the disk asynch IO:

> $ docker run -d -p 49161:1521 -e ORACLE_DISABLE_ASYNCH_IO=true oracleinanutshell/oracle-xe-11g
> --Enable XDB user with default password: xdb, run this:

> $ docker run -d -p 49161:1521 -e ORACLE_ENABLE_XDB=true oracleinanutshell/oracle-xe-11g

## For APEX user:

> $ docker run -d -p 49161:1521 -p 8080:8080 oracleinanutshell/oracle-xe-11g

# Login http://localhost:8080/apex/apex_admin with following credential:

username: ADMIN
password: admin
For latest APEX(18.1) user, please pull oracleinanutshell/oracle-xe-11g:18.04-apex first:

docker run -d -p 49161:1521 -p 8080:8080 oracleinanutshell/oracle-xe-11g:18.04-apex

# Login http://localhost:8080/apex/apex_admin with following credential:

username: ADMIN
password: Oracle_11g
By default, the password verification is disable(password never expired)
Connect database with following setting:

hostname: localhost
port:  
sid: xe
username: system
password: oracle
Password for SYS & SYSTEM

oracle
Support custom DB Initialization and running shell scripts

# Dockerfile

```Dockerfile
FROM oracleinanutshell/oracle-xe-11g

ADD init.sql /docker-entrypoint-initdb.d/
ADD script.sh /docker-entrypoint-initdb.d/
Running order is alphabetically.

https://blogdocardoso.com/linux-mint-instalando-o-oracle-sql-developer-4/

## INSTALL CLIENT

https://oracle.github.io/odpi/doc/installation.html#linux
```
