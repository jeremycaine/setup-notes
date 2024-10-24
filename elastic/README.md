# Elasticsearch
Install of Elastic on local macOS using `podman`.

## brew
brew tap elastic/tap
brew install elastic/tap/elasticsearch-full

home Elasticsearch home directory or $ES_HOME /usr/local/var/homebrew/linked/elasticsearch-full

bin Binary scripts including elasticsearch to start a node and elasticsearch-plugin to install plugins /usr/local/var/homebrew/linked/elasticsearch-full/bin

conf Configuration files including elasticsearch.yml /usr/local/etc/elasticsearch

ES_PATH_CONF

data

The location of the data files of each index / shard allocated on the node.

/usr/local/var/lib/elasticsearch

path.data

logs

Log files location.

/usr/local/var/log/elasticsearch

path.logs

plugins

Plugin files location. Each plugin will be contained in a subdirectory.

/usr/local/var/homebrew/linked/elasticsearch/plugins


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
podman container rm es01

podman run --name es01 --net elastic -p 9200:9200 -e "discovery.type=single-node" -e ES_JAVA_OPTS="-Xms1g -Xmx1g" -v elastic:/usr/share/elasticsearch/data docker.elastic.co/elasticsearch/elasticsearch:8.11.3
```

export ES_USER="elastic"
export ES_PASSWORD=$(podman exec -ti es01 /usr/share/elasticsearch/bin/elasticsearch-reset-password -s -b -u $ES_USER | tr -d '[:space:]')
export ES_CRED="${ES_USER}:${ES_PASSWORD}"

export ES_PASSWORD=$(podman exec -ti es01 /usr/share/elasticsearch/bin/elasticsearch-reset-password -s -b -u $ES_USER | tr -d '[:space:]')
