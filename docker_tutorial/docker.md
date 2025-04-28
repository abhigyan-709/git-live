# Programming - Python

## Dockerfile - application - build 
## Application - Image - repository | registry - Docker Hub, ECR (elastic container registry)


# tester 
image pull - docker application image will be pulled by tester

# deployment of the image application


# microservice - 
c for container!
1. db - c1
2. ui - c2
3. api - c3
4. redis - c4
5. backend - c5


# Docker Commands : 

1. docker run = docker create + docker start 

docker run <image_name>
docker run -it (interactive mode) --name <contauiner-name> <image-name>

docker pull - image (agar image locally nahi hai to)
docker create - conatiner will be created 
docker start - container will be started


docker ps - only running conatainer
docker ps -a all conatiner (running + stopped)
docker ps -a -l (
)
docker ps -a (for all conatiner)
docker ps -l for latest created container
docker ps -q this will show the id of the container


docker exec

docker run -d (de-attached) -p (port) from_port:to_port <image-name>

