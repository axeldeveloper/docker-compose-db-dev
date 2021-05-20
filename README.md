# UTILIZANDO DO DOCKER TOOLBOX

    desabilitar  Hyper-V

    https://support.bluestacks.com/hc/pt-br/articles/115004254383-Como-eu-desabilito-o-Hyper-V-no-Windows-

    abrir o powershell



# LISTA AS VMS

    docker version
    docker info
    > $ docker -v
    > $ docker-machine ls



# CRIA UMA MAQUINA VIRTUAL DOCKER

    >$ docker-machine create --driver virtualbox myvm1

    >$ docker-machine create --driver virtualbox default

    >$ docker-machine create default --virtualbox-no-vtx-check 

    >$ docker-machine create -d virtualbox --engine-env HTTP_PROXY=http://axbenites@fazenda:xxxxx@xx@proxy.spa.mo.br:8058 -engine-env HTTPS_PROXY=https://axbenites@fazenda:xxx@xx@proxy.spa.mo.br:8058 --engine-env NO_PROXY=example2.com default

    Docker is up and running!
    https://github.com/docker/machine/issues/4271

    docker run -p 3001:3001 -d $NAME

# REGERANDO CERTIFICADO

    >$ docker-machine regenerate-certs default


# Start and stop machines


    $ docker-machine stop default

    $ docker-machine start default

    Starting VM... 

    $ docker-machine run default /assuming default is your Linux VM/

    $ docker-machine ssh default


    $ docker-machine rm baz

    $ docker image rm 75835a67d134 2a4cca5ac898


# IP - PROXY

    $ docker-machine ip
    $ docker-machine ssh
    $ docker-machine env default
    $ docker network ls


Removing Docker Networks
Remove one or more networks

docker network ls


DOCKER COM ELASTIC SEARCH
--------------------------------------------------
docker run -p 9200:9200 -e ELASTIC_PASSWORD=766312 docker.elastic.co/elasticsearch/elasticsearch-platinum:6.2.4

USER: elastic 
PWS: 766312




DOCKER COM MONGO
--------------------------------------------------
docker pull mongo
docker run --name testemongo -p 17017:27017 -d mongo


DOCKER REDIS
--------------------------------------------------
docker pull redis
docker run --name testeredis -p 6379:6379 -d redis
https://medium.com/@renato.groffe/docker-nosql-executando-o-mongodb-e-o-redis-a-partir-de-containers-3c143e920f09



Connect your shell to the new machine.

 $ eval "$(docker-machine env default)"

 docker pull docker.elastic.co/elasticsearch/elasticsearch:6.3.2


DOCKER  RUM
--------------------------- 
 

docker-compose -f docker-compose.yml build

docker-compose -f docker-compose.yml up -d




docker run -d -p 9200:9200 -e "discovery.type=single-node" -v esdata:/usr/share/elasticsearch/data docker.elastic.co/elasticsearch/elasticsearch:6.4.2

docker run -p 9200:9200 -e ELASTIC_PASSWORD=766312 docker.elastic.co/elasticsearch/elasticsearch-platinum:6.2.4



docker run --name mariadbtest -e MYSQL_ROOT_PASSWORD=mypass -d mariadb/server:10.3 --log-bin --binlog-format=MIXED



STOP CONTEINER
------------------
elastic_pascal



removendo tudo
------------------
Para remover adicionalmente todos os contêineres parados e todas as imagens não utilizadas 
(não apenas imagens pendentes), 
adicione o -a sinalizador ao comando:

docker system prune -a

docker container rm $(docker container ls -aq)




# Windows

# utilizando do docker toolbox
----------------------------------------

# Desabilitar  Hyper-V
---------------------------------------
https://support.bluestacks.com/hc/pt-br/articles/115004254383-Como-eu-desabilito-o-Hyper-V-no-Windows-




# comandos docker 
--------------------------------------------
docker version
docker info
    > $ docker -v
    
    > $ docker-machine ls `docker tool`



cria uma maquina virtual docker
--------------------------------------------

>$ docker-machine create --driver virtualbox default

>$ docker-machine create default --virtualbox-no-vtx-check 

>$ docker-machine create -d virtualbox --engine-env HTTP_PROXY=http://axbenites@fazenda:Axel@193@proxy.sgi.ms.gov.br:8080 -engine-env HTTPS_PROXY=https://axbenites@fazenda:Axel@193@proxy.sgi.ms.gov.br:8080 --engine-env NO_PROXY=example2.com default

Docker is up and running!
https://github.com/docker/machine/issues/4271


Regerando certificado
---------------------------------------------
>$ docker-machine regenerate-certs default


Start and stop machines
-------------------------------------------

$ docker-machine stop default
$ docker-machine start default
Starting VM... 

About to remove baz
-------------------------------------------
>docker-machine rm baz


IP - PROXY
-------------------------------------------
$ docker-machine ip
$ docker-machine ssh
docker-machine env default


Connect your shell to the new machine.

 $ eval "$(docker-machine env default)"

 docker pull docker.elastic.co/elasticsearch/elasticsearch:6.3.2


docker-compose -f docker-compose.yml build

docker-compose -f docker-compose.yml up -d

docker run -e ELASTIC_PASSWORD=766312 docker.elastic.co/elasticsearch/elasticsearch-platinum:6.2.4

Environment="HTTP_PROXY=http://axbenites@fazenda:Axel@193@proxy.sgi.ms.gov.br:8080"

sudo HTTP_PROXY=HTTP_PROXY=http://axbenites@fazenda:Axel@193@proxy.sgi.ms.gov.br:8080/ docker pull docker pull docker.elastic.co/elasticsearch/elasticsearch:6.3.2      

docker-machine create -d virtualbox \
    --engine-env HTTP_PROXY=http://example.com:8080 \
    --engine-env HTTPS_PROXY=https://example.com:8080 \
    --engine-env NO_PROXY=example2.com \
    default                                 

mnt/sda1/var/lib/docker









DENTRO DO DOCKER
- INFORMAÇÕES DE REDE
cat /etc/resolv.conf 

sudo vi  /etc/systemd/system/docker.service.d/http-proxy.conf

sudo mkdir -p /etc/systemd/system/docker.service.d 

escreve
---------------------
echo -e "[Service]\nEnvironment=\"HTTP_PROXY=http://axbenites@fazenda:Axel@193@proxy.sgi.ms.gov.br:8080/\"" > /etc/systemd/system/docker.service.d/https-proxy.conf

reinicia
------------------------------------
sudo /etc/init.d/docker restart


[Service]
Environment="HTTP_PROXY=http://axbenites@fazenda:Axel@193@proxy.sgi.ms.gov.br:8080"
Environment="HTTP_PROXY=http://axbenites@fazenda:Axel@193@proxy.sgi.ms.gov.br:8080"

Environment="NO_PROXY=localhost,127.0.0.1,docker-registry.example.com,.corp, docker-registry.local"











Missing proxy configuration?

mkdir -p /etc/systemd/system/docker.service.d
nano /etc/systemd/system/docker.service.d/http-proxy.conf

[Service]
Environment="HTTP_PROXY=http://USER:PASSWD@SERVER:PORT/"
Environment="HTTPS_PROXY=http://USER:PASSWD@SERVER:PORT/"

systemctl daemon-reload
systemctl restart docker



.
https://docs.docker.com/toolbox/faqs/troubleshoot/#/http-proxies-and-connectivity-errors
    Use ssh to log in to the virtual machine. This example logs in to the default machine.

     $ docker-machine ssh default
     docker@default:~$ sudo vi /var/lib/boot2docker/profile

    Add a NO_PROXY setting to the end of the file similar to the example below.

     # replace with your office's proxy environment
     export "HTTP_PROXY=http://PROXY:PORT"
     export "HTTPS_PROXY=http://PROXY:PORT"
     # you can add more no_proxy with your environment.
     export "NO_PROXY=192.168.99.*,*.local,169.254/16,*.example.com,192.168.59.*"

    Restart Docker.

    After you modify the profile on your VM, restart Docker and log out of the machine.

     docker@default:~$ sudo /etc/init.d/docker restart
     docker@default:~$ exit



     https://github.com/docker/awesome-compose






















git config --global http.proxy http://axbenites:Axel@193@proxy.sgi.ms.gov.br:8081





Environment="HTTP_PROXY=http://axbenites:Axel@193@proxy.sgi.ms.gov.br:8081"

sudo HTTP_PROXY=HTTP_PROXY=http://axbenites@fazenda:Axel@193@proxy.sgi.ms.gov.br:8080/ docker pull docker pull docker.elastic.co/elasticsearch/elasticsearch:6.3.2      

docker-machine create -d virtualbox \
    --engine-env HTTP_PROXY=http://example.com:8080 \
    --engine-env HTTPS_PROXY=https://example.com:8080 \
    --engine-env NO_PROXY=example2.com \
    default                                 

mnt/sda1/var/lib/docker









DENTRO DO DOCKER
- INFORMAÇÕES DE REDE
cat /etc/resolv.conf 

sudo vi  /etc/systemd/system/docker.service.d/http-proxy.conf

sudo mkdir -p /etc/systemd/system/docker.service.d 

escreve
---------------------
echo -e "[Service]\nEnvironment=\"HTTP_PROXY=http://axbenites@fazenda:Axel@193@proxy.sgi.ms.gov.br:8080/\"" > /etc/systemd/system/docker.service.d/https-proxy.conf

reinicia
------------------------------------
sudo /etc/init.d/docker restart


[Service]
Environment="HTTP_PROXY=http://axbenites@fazenda:Axel@193@proxy.sgi.ms.gov.br:8080"
Environment="HTTP_PROXY=http://axbenites@fazenda:Axel@193@proxy.sgi.ms.gov.br:8080"

Environment="NO_PROXY=localhost,127.0.0.1,docker-registry.example.com,.corp, docker-registry.local"











Missing proxy configuration?

mkdir -p /etc/systemd/system/docker.service.d
nano /etc/systemd/system/docker.service.d/http-proxy.conf

[Service]
Environment="HTTP_PROXY=http://USER:PASSWD@SERVER:PORT/"
Environment="HTTPS_PROXY=http://USER:PASSWD@SERVER:PORT/"

systemctl daemon-reload
systemctl restart docker



.
https://docs.docker.com/toolbox/faqs/troubleshoot/#/http-proxies-and-connectivity-errors
    Use ssh to log in to the virtual machine. This example logs in to the default machine.

     $ docker-machine ssh default
     docker@default:~$ sudo vi /var/lib/boot2docker/profile

    Add a NO_PROXY setting to the end of the file similar to the example below.

     # replace with your office's proxy environment
     export "HTTP_PROXY=http://PROXY:PORT"
     export "HTTPS_PROXY=http://PROXY:PORT"
     # you can add more no_proxy with your environment.
     export "NO_PROXY=192.168.99.*,*.local,169.254/16,*.example.com,192.168.59.*"

    Restart Docker.

    After you modify the profile on your VM, restart Docker and log out of the machine.

     docker@default:~$ sudo /etc/init.d/docker restart
     docker@default:~$ exit



HTTPS_PROXY = https://axbenites:Axel@193@proxy.sgi.ms.gov.br:8081


 docker --build --no-cache --build-arg http_proxy=http://proxy.sgi.ms.gov.br:8080 --build-arg https_proxy=https://proxy.sgi.ms.gov.br:8080 .



Vendedor
AUTO PECAS DIAS
011 45137557

Enviar mensagem











