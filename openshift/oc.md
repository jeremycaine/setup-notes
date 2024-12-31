# OpenShift Command Line

## downloads


## shell
```
crc oc-env

# add to .zprofile
export PATH="/Users/jeremycaine/.crc/bin/oc:$PATH"
source ~/.zprofile

# Run this command to configure your shell:
# eval $(crc oc-env)
```

## environment
```
# return developer and kubeadmin creds
crc console --credentials

# web consoler
crc console
```