docker build -t $DOCKER_ID_USER/makegcc . --no-cache
docker push $DOCKER_ID_USER/makegcc
