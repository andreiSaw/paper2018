docker build -t $DOCKER_ID_USER/montecarlo . --no-cache
docker push $DOCKER_ID_USER/montecarlo:latest
