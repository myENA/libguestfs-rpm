# RPM Spec for Libguestfs, Supermin and others

Backport of the latest libguestfs development release from Fedora for CentOS 7.x including supporting packages.

# Building

The RPMs may be built with [Docker](#with-docker), [Vagrant](#with-vagrant), or [manual](#manual).

Whatever way you choose you will need to do a few basic things first.

```bash
git clone https://github.com/myENA/libguestfs-rpm  ## check out this code
cd libguestfs-rpm                                  ## uhh... you should know
mkdir -p artifacts                                 ## prep the artifacts location
```

## With Docker

```bash
docker build -t ena/libguestfs-rpm .                                ## build the image
docker run -v $PWD/artifacts:/tmp/artifacts -it ena/libguestfs-rpm  ## run the image and build the RPMs
```

## With Vagrant

```bash
vagrant up                         ## provision and build the RPMs
```

## Manual

```bash
cat build.sh     ## read the script
```

## Result

A whole lot of RPMs for libguestfs, ocaml-libvirt language bindings, supermin, virt-v2v and friends and many libguestfs language bindings.

```bash

```
