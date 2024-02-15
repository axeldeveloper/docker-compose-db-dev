# Project
    rabbitmq

# Build
``` powershell
    $ docker-compose up -d

    $ docker start/stop db_postgres
    $ docker start/stop db_postgres
```
# test
    open your browser and head over to http://localhost:15672. You should see the RabbitMQ UI. Use guest as username and password.
    Once we've created the main.go file, let's test sendMessage with the following terminal command: go run sendMessage.go. 
    You should see something like this:


# links uteis
    - https://x-team.com/blog/set-up-rabbitmq-with-docker-compose/


# install go

```powershell

    wget https://dl.google.com/go/go1.14.2.linux-amd64.tar.gz
    sudo tar -xvf go1.14.2.linux-amd64.tar.gz
    sudo mv go /usr/local

    Next up open up your .bashrc file. You can find it by navigating to the home path, opening up the current directory in Windows Explorer and opening up .bashrc with a text editor of your choice.

    cd ~
    explorer.exe .

    Add the following three lines to the botom of your .bashrc file and save it.

    export GOROOT=/usr/local/go
    export GOPATH=$HOME/go
    export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
```