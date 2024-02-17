crc pkg
pull secret
run pkg installer
cd .crc
only has .launchd-crcd.log

crc config set preset podman
crc setup
applications > rh openshift > get started
podman preset > run setup

.crc
dir is populated
crc version
crc -h
crc podman-env
Machine does not exist. Use 'crc start' to create it

go to where the pull secret is
cd ~/.
crc start
eval $(crc podman-env)
(base) ➜  ~ podman -v
podman version 4.3.1


crc config set preset openshift
* preset Virtual machine preset (valid values are: podman, openshift and okd)
crc 
podman -v > not found
crc start



# OpenShift Local (formerly Code Ready Containers)
Instructions for Apple MacPro Silicon M1 `aarch64` chip architecture. The [CRC Site](https://crc.dev) reroutes to [OpenShift Local site](https://developers.redhat.com/products/openshift-local/overview) 

xxx## Before you start
xxxInstall Podman on MacBook Pro M1.

crc podman-env shows env vars
eval $(crc podman-env)
podman machine start

error:
Starting machine "podman-machine-default"
Error: unable to start host networking: "could not find \"gvproxy\" in one of [/usr/local/opt/podman/libexec /opt/homebrew/bin /opt/homebrew/opt/podman/libexec /usr/local/bin /usr/local/libexec/podman /usr/local/lib/podman /usr/libexec/podman /usr/lib/podman].  To resolve this error, set the helper_binaries_dir key in the `[engine]` section of containers.conf to the directory containing your helper binaries."

gvproxy
https://podman-desktop.io/docs/troubleshooting#unable-to-set-custom-binary-path-for-podman-on-macos

add to `~/.config/containers/containers.conf
```
...
[engine]
helper_binaries_dir=["/Users/jeremycaine/.gvproxy"]\
...
```

sudo /Users/jeremycaine/.crc/cache/crc_vfkit_4.12.5_arm64/podman-mac-helper install
podman machine stop
podman machine start


### Install
The basic installation intstruction are [here](https://podman.io/getting-started/installation)
```
brew install podman
which podman
```
Returns the install location as `/opt/homebrew/bin/podman`

In your Shell profile add this to the path
```
export PATH="/opt/homebrew/bin/podman:$PATH"
```

On 28 March 2023, the podman version installed with brew was `4.4.4`.
CRC versions were:
```
CRC version: 2.15.0+72256c3c
OpenShift version: 4.12.5
Podman version: 4.3.1
```

### Test Podman
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


## Install OpenShift Local
- Log in to Red Hat account
- Download installer and pull secret from [Dowload page](https://console.redhat.com/openshift/create/local)
- Run installer
- move pull secret to the directory where you will set up OpenShift local
- run `crc setup` (or via Applications | Red Hat OpenShift Local > double-click, launches an installer)

## Start
Once installed
- go to Terminal and `.crc` directory will be in your MacOS user folder e.g. `/Users/<username>`
- `crc start` which takes about four minutes to start up the cluster instance
- password will be printed in the output

example tail of start output
```
...
INFO Operators are stable (3/3)...
INFO Adding crc-admin and crc-developer contexts to kubeconfig...
Started the OpenShift cluster.

The server is accessible via web console at:
  https://console-openshift-console.apps-crc.testing

Log in as administrator:
  Username: kubeadmin
  Password: GfffH-TCw7R-4CQqa-rZ8cR

Log in as user:
  Username: developer
  Password: developer

Use the 'oc' command line interface:
  $ eval $(crc oc-env)
  $ oc login -u developer https://api.crc.testing:6443
```

## Podman Check
CRC (OpenShift Local) has now installed. As part of that installation it has also installed `podman`. It uses this internally for Source to Image builds. There is also an option to use this podman install for container build and management. However it is only available when CRC is running.

After `crc setup` then the following symbolic link is created:
```
/Users/jeremycaine/.crc/bin/oc/podman -> /Users/jeremycaine/.crc/cache/crc_vfkit_4.12.5_arm64/podman
```

As soon as you execute `eval $(crc oc-env)` then the PATH is setup with `/Users/jeremycaine/.crc/bin/oc`.

Therefore to consisten

You therefore need to fix your path so that you can continue to use `podman`


## Access 
Access the web console
```
crc console
```

Log in as the developer user with the password printed in the output of the crc start command. You can also view the password for the developer and kubeadmin users by running the following command: 
```
crc console --credentials
```

## OpenShift CLI
Log into command line as developer
```
eval $(crc oc-env)
oc login -u developer https://api.crc.testing:6443
```
Output will be:
```
Logged into "https://api.crc.testing:6443" as "developer" using existing credentials.

You don't have any projects. You can try to create a new project, by running

    oc new-project <projectname>
```

## Build a Hello World Project
In order to understand how OpenShift Local is configured out of the box, we'll use a hello world project examples to show a few aspects of this.

as dev
```
oc create secret docker-registry my-docker-secret --docker-server=docker.io --docker-username=cg2p --docker-password=Le1cester --docker-email=jezcaine@gmail.com
oc secrets link default my-docker-secret --for=pull
```


```
oc login -u developer https://api.crc.testing:6443
oc new-project hello
oc new-app https://github.com/cg2p/hello-node --strategy=docker
oc expose service/hello-node
```
gives warning
```
--> Found container image 5fee518 (4 days old) from Docker Hub for "node:latest"

    * An image stream tag will be created as "node:latest" that will track the source image
    * A Docker build using source code from https://github.com/cg2p/hello-node will be created
      * The resulting image will be pushed to image stream tag "hello-node:latest"
      * Every time "node:latest" changes a new build will be triggered

--> Creating resources ...
    imagestream.image.openshift.io "node" created
    imagestream.image.openshift.io "hello-node" created
    buildconfig.build.openshift.io "hello-node" created
Warning: would violate PodSecurity "restricted:v1.24": allowPrivilegeEscalation != false (container "hello-node" must set securityContext.allowPrivilegeEscalation=false), unrestricted capabilities (container "hello-node" must set securityContext.capabilities.drop=["ALL"]), runAsNonRoot != true (pod or container "hello-node" must set securityContext.runAsNonRoot=true), seccompProfile (pod or container "hello-node" must set securityContext.seccompProfile.type to "RuntimeDefault" or "Localhost")
    deployment.apps "hello-node" created
    service "hello-node" created
--> Success
    Build scheduled, use 'oc logs -f buildconfig/hello-node' to track its progress.
    Application is not exposed. You can expose services to the outside world by executing one or more of the commands below:
     'oc expose service/hello-node'
    Run 'oc status' to view your app.
```


### Deploy a simple app from Google registry
```
kubectl create deployment hello-node --image=k8s.gcr.io/e2e-test-images/agnhost:2.33 -- /agnhost serve-hostname
```
get this output
```
Warning: would violate PodSecurity "restricted:v1.24": allowPrivilegeEscalation != false (container "agnhost" must set securityContext.allowPrivilegeEscalation=false), unrestricted capabilities (container "agnhost" must set securityContext.capabilities.drop=["ALL"]), runAsNonRoot != true (pod or container "agnhost" must set securityContext.runAsNonRoot=true), seccompProfile (pod or container "agnhost" must set securityContext.seccompProfile.type to "RuntimeDefault" or "Localhost")
deployment.apps/hello-node created
```
The app is being deployed despite the warning, check with `oc get all`
```
oc expose deployment.apps/hello-node --port=8080
oc status
```


Then, try an OpenShift template based build and deploy
```
oc new-project test1
oc new-app rails-postgresql-example

    

oc new-app https://github.com/jeremycaine/hello-world
oc expose service/hello-world

# get URL of deployment from

oc status
```

## Configure Registry Access in OpenShift Local
Go to the console as kubeadmin and configure the OpenShift Local cluster to accept images from external registries.

Go to Overview | Details | View Settings | Configuration | edit `Image' YAML
It starts like this out of the box
```

spec:
  additionalTrustedCA:
    name: registry-certs
status:
  externalRegistryHostnames:
    - default-route-openshift-image-registry.apps-crc.testing
  internalRegistryHostname: 'image-registry.openshift-image-registry.svc:5000'
```
then we update it
```
spec:
  additionalTrustedCA:
    name: registry-certs
  allowedRegistriesForImport:
    - domainName: quay.io
      insecure: false
  registrySources:
    allowedRegistries:
      - quay.io
      - 'image-registry.openshift-image-registry.svc:5000'
status:
  externalRegistryHostnames:
    - default-route-openshift-image-registry.apps-crc.testing
  internalRegistryHostname: 'image-registry.openshift-image-registry.svc:5000'
```
###


oc get secret/pull-secret -n openshift-config --template='{{index .data ".dockerconfigjson" | base64decode}}' ><pull_secret_location> 


oc policy add-role-to-user registry-viewer developer

oc new-project hello
oc import-image ubi8/nodejs-16 --from=registry.redhat.io/ubi8/nodejs-16 --confirm
oc import-image ubi8/nodejs-16-minimal --from=registry.redhat.io/ubi8/nodejs-16-minimal --confirm


# CLEAN
openshift local
registry sources for quay.io etc
oc login developer
new project hello
oc new-app . (x looks  for docker.io)
oc new-app . --image-stream=nodejs (looks in imagestream in local)
tag = nodejs:16-ubi9, name = ubi9/nodejs-16 (same as FROM)
oc expose service/hello-world
oc status

## Uninstall
- `crc delete --clear-cache` removes the instance but not the CRC install
- move Red Hat OpenShift Local to bin
- empty and delete `~/.crc` folder
- remove CRC daemon [link](https://access.redhat.com/documentation/pt-br/red_hat_codeready_containers/1.7/html/release_notes_and_known_issues/issues_on_macos)
```
launchctl unload ~/Library/LaunchAgents/com.redhat.crc.daemon.plist
rm ~/Library/LaunchAgents/com.redhat.crc.daemon.plist
```
