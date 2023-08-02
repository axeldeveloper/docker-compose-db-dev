# Quick Start

# Linux

docker run -d -p 9000:9000 --name portainer --restart always -v /var/run/docker.sock:/var/run/docker.sock -v /home/axel/Dev/Portainer/data:/data portainer/portainer

docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v /home/axel/Dev/Portainer/data:/data portainer/portainer-ce:latest

## Mac OS

  docker run -d -p 9000:9000 --name portainer --restart always -v /var/run/docker.sock:/var/run/docker.sock -v /Users/axel/Dev/docker/portainer/data:/data portainer/portainer

# Admin

- user = admin
- pwd = demo12345