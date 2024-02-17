# KServer Model Mesh

## OpenShift
```
crc start
```
login as oc kubeadmin

## Kustomize
```
brew install kustomize
```

## KServe install
https://github.com/kserve/modelmesh-serving/blob/main/docs/install/install-script.md 


create `etcd-config.json`
```
{
  "endpoints": "https://api.crc.testing:6443",
  "userid": "kubeadmin",
  "password": "tizcq-PJqAL-IdWVP-NGC8J",
  "root_prefix": "unique-chroot-prefix"
}
```

```
kubectl create secret generic model-serving-etcd --from-file=etcd_connection=etcd-config.json

RELEASE="main"
git clone -b $RELEASE --depth 1 --single-branch https://github.com/kserve/modelmesh-serving.git
cd modelmesh-serving

kubectl create namespace modelmesh-serving
./scripts/install.sh --namespace-scope-mode --namespace modelmesh-serving --quickstart 
```