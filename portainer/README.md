# Quick Start
  - Mananger by docker

# Linux

  - docker run -d -p 9000:9000 --name portainer --restart always -v /var/run/docker.sock:/var/run/docker.sock -v /home/axel/Dev/docker/Portainer/data:/data portainer/portainer

# Mac OS

  - docker run -d -p 9000:9000 --name portainer --restart always -v /var/run/docker.sock:/var/run/docker.sock -v /Users/axel/Dev/docker/Portainer/data:/data portainer/portainer

# Admin

  - user = admin
  - pwd = demo123456
