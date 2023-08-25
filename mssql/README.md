# DB MSSQL
- mssql-server-linux-tinytds:2017-GA `imagem`
- mcr.microsoft.com/mssql/server:2017-latest `imagem`


# Version 9
    sqlq server 2017

# Setting


# docker compose
``` powershell
    $ docker-compose up -d

    $ docker start/stop mssql_tinytds

    docker compose -f "mssql/docker-compose-v2.yml" up -d --build

```

# docker
``` powershell
    $ docker pull mcr.microsoft.com/mssql/server:2019-latest
    # pull imagem

    $ docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=demo123" ` -p 1433:1433 --name sql1 --hostname sql1 `  -d mcr.microsoft.com/mssql/server:2019-latest
    # rum images

    $ docker exec -t sql1 cat /var/opt/mssql/log/errorlog | grep connection
    # exec contianer

    $ docker exec -it sql1 /opt/mssql-tools/bin/sqlcmd `-S localhost -U SA -P "<YourStrong@Passw0rd>" ` -Q "ALTER LOGIN SA WITH PASSWORD='<YourNewStrong@Passw0rd>'"
    # exec contianer

    $ docker exec -it sql1 "bash"
       Once inside the container, connect locally with sqlcmd, using its full path.

        Bash

        Copy
        /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P "<YourNewStrong@Passw0rd>"

```

# Parameter	Description

-e "ACCEPT_EULA=Y"	Set the ACCEPT_EULA variable to any value to confirm your acceptance of the End-User Licensing Agreement. Required setting for the SQL Server image.


-e "SA_PASSWORD=<YourStrong@Passw0rd>"	Specify your own strong password that is at least eight characters and meets the SQL Server password requirements. Required setting for the SQL Server image.


-p 1433:1433	Map a TCP port on the host environment (first value) with a TCP port in the container (second value). In this example, SQL Server is listening on TCP 1433 in the container and this port is exposed to the port, 1433, on the host.


--name sql1	Specify a custom name for the container rather than a randomly generated one. If you run more than one container, you can't reuse this same name.


--hostname sql1	Used to explicitly set the container hostname. If you don't specify the hostname, it defaults to the container ID, which is a randomly generated system GUID.


# links uteis
