# DB PostgresSQL
    database postgres 9

    pgadmin 4

# Version 9
    9

# Setting PGAdmin
    Em Host name/address informar o nome do container que corresponde à instância do PostgreSQL (teste-postgres-compose);
    
    Em Port definir o valor 5432 (porta default de acesso ao container e disponível a partir da rede postgres-compose-network; não informar a porta em que o PostgreSQL foi mapeado no host);
    
    No atributo Username será informado o usuário default do PostgreSQL (postgres), bem como a senha correspondente em Password (demo123)   




# Build
``` powershell     
    $ docker-compose up -d

    $ docker start/stop db_postgres
    $ docker start/stop db_postgres
```

# links uteis

link 1 [here](https://medium.com/@renato.groffe/postgresql-pgadmin-4-docker-compose-montando-rapidamente-um-ambiente-para-uso-55a2ab230b89)

Link 2 [here](https://medium.com/@renato.groffe/postgresql-pgadmin-4-docker-compose-montando-rapidamente-um-ambiente-para-uso-55a2ab230b89)

Link 3 [here](https://gist.githubusercontent.com/renatogroffe/82459fb2a517b1b5db2172c81dc86d9c/raw/8b12c3a17989fd5dde7f3244c9962822b29fc4b9/docker-compose.yml)
