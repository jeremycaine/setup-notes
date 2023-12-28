# Podman on MacBook Pro M1
The basic installation intstruction are [here](https://podman.io/getting-started/installation)

## Test Podman
```
podman machine init
podman machine start

git clone http://github.com/baude/alpine_nginx && cd alpine_nginx
podman build -t alpine_nginx .
podman images

podman run -dt -p 9999:80 alpine_nginx
curl http://localhost:9999
```

Cleanup
```
# get container id that is running from
podman ps

# remove it
podman rm <container id>
```



