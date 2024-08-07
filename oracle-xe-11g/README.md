# Contêiner do Oracle Database 23ai (23.4.0.0)


# Quick Start


```sh
# Run with 1521 port opened:

$ docker pull container-registry.oracle.com/database/free:latest

$ docker run -d --name app-oracle-db -p 1521:1521  -e ORACLE_PWD=oracle container-registry.oracle.com/database/free:latest

# using docker compose
$ sudo docker-compose -f ./docker-compose.free.yml up --build

$ docker run -d --name app-oracle-db -p 1521:1521  -e ORACLE_PWD=oracle container-registry.oracle.com/database/free:latest

docker exec -it app-oracle-db sqlplus sys/oracle@FREE as sysdba

```

# Configurações personalizadas

```sh
podman run --name <container name> \
-P | -p <host port>:1521 \
-e ORACLE_PWD=<your database passwords> \
-e ORACLE_CHARACTERSET=<your character set> \
-e ENABLE_ARCHIVELOG=true \
-e ENABLE_FORCE_LOGGING=true \
-v [<host mount point>:]/opt/oracle/oradata \
container-registry.oracle.com/database/free:latest
```


```powershell
$ docker run -d -p 49161:1521 oracleinanutshell/oracle-xe-11g
# Run this, if you want the database to be connected remotely:

$ docker run -d -p 49161:1521 -e ORACLE_ALLOW_REMOTE=true oracleinanutshell/oracle-xe-11g
# For performance concern, you may want to disable the disk asynch IO:

$ docker run -d -p 49161:1521 -e ORACLE_DISABLE_ASYNCH_IO=true oracleinanutshell/oracle-xe-11g
# Enable XDB user with default password: xdb, run this:

# Run this, if you want the database to be connected remotely:
$ docker run -d -p 49161:1521 oracleinanutshell/oracle-xe-11g


# For performance concern, you may want to disable the disk asynch IO:
$ docker run -d -p 49161:1521 -e ORACLE_ALLOW_REMOTE=true oracleinanutshell/oracle-xe-11g

# Enable XDB user with default password: xdb, run this:
$ docker run -d -p 49161:1521 -e ORACLE_DISABLE_ASYNCH_IO=true oracleinanutshell/oracle-xe-11g


$ docker run -d -p 49161:1521 -e ORACLE_ENABLE_XDB=true oracleinanutshell/oracle-xe-11g

## For APEX user:

$ docker run -d -p 49161:1521 -p 8080:8080 oracleinanutshell/oracle-xe-11g



```
# Login apex_admin

  http://localhost:8080/apex/apex_admin with following
credential:

  - username: ADMIN
  - password: admin - temporario trocar

```sh
$ docker run -d -p 49161:1521 -p 8080:8080 oracleinanutshell/oracle-xe-11g:18.04-apex

# Login http://localhost:8080/apex/apex_admin with following credential:

username: ADMIN
password: Oracle_11g

By default, the password verification is disable(password never expired)
Connect database with following setting:

hostname: localhost
port:   49161:1521
sid: xe
username: system
password: oracle
Password for SYS & SYSTEM

#oracle
#Support custom DB Initialization and running shell #scripts

# username/password: SYS/oracle
# SID: orcl

```
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