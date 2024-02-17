# Elasticsearch
Install of Elastic on local macOS using `podman`.

Instructions [here](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html) for v8.11.

## Install
```
podman machine start

# get image
podman network create elastic
podman pull docker.elastic.co/elasticsearch/elasticsearch:8.11.3
# verify images
wget https://artifacts.elastic.co/cosign.pub
cosign verify --key cosign.pub docker.elastic.co/elasticsearch/elasticsearch:8.11.3
```

## Run Elastic
Start Elasticsearch in container

Using the -m flag to set a memory limit for the container. This removes the need to manually set the JVM size. However, there is issue with ES on macOS with M1 as described [here](https://medium.com/@guillem.riera/elasticsearch-on-docker-podman-on-apple-silicon-mac-m1-m2-improving-official-documentation-e3b272ac7ad2)
```
# original command from ES doc site
# podman run --name es01 --net elastic -p 9200:9200 -it -m 1GB docker.elastic.co/elasticsearch/elasticsearch:8.11.3 sysctl vm.max_map_count=262144

# modified
podman run --name es01 --net elastic -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e ES_JAVA_OPTS="-Xms1g -Xmx1g" -v elastic:/usr/share/elasticsearch/data docker.elastic.co/elasticsearch/elasticsearch:8.11.3
podman run --name es01 --net elastic -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e ES_JAVA_OPTS="-Xms1g -Xmx1g" docker.elastic.co/elasticsearch/elasticsearch:8.11.3


```
