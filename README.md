# RPM Spec for Libguestfs, Supermin and others

Backporp of the latest libguestfs stable release from Fedora for CentOS 7.x including supporting packages.

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
-rw-r--r--   1 ahurt  staff    159300 Jun 29 17:47 erlang-libguestfs-1.36.5-1.el7.centos.x86_64.rpm
-rw-r--r--   1 ahurt  staff     55704 Jun 29 17:47 golang-guestfs-1.36.5-1.el7.centos.noarch.rpm
-rw-r--r--   1 ahurt  staff  22755558 Jun 29 17:47 libguestfs-1.36.5-1.el7.centos.src.rpm
-rw-r--r--   1 ahurt  staff   2014068 Jun 29 17:47 libguestfs-1.36.5-1.el7.centos.x86_64.rpm
-rw-r--r--   1 ahurt  staff      8056 Jun 29 17:47 libguestfs-bash-completion-1.36.5-1.el7.centos.noarch.rpm
-rw-r--r--   1 ahurt  staff     41712 Jun 29 17:47 libguestfs-benchmarking-1.36.5-1.el7.centos.x86_64.rpm
-rw-r--r--   1 ahurt  staff   8485124 Jun 29 17:47 libguestfs-debuginfo-1.36.5-1.el7.centos.x86_64.rpm
-rw-r--r--   1 ahurt  staff   1359304 Jun 29 17:47 libguestfs-devel-1.36.5-1.el7.centos.x86_64.rpm
-rw-r--r--   1 ahurt  staff      2516 Jun 29 17:47 libguestfs-forensics-1.36.5-1.el7.centos.x86_64.rpm
-rw-r--r--   1 ahurt  staff      2440 Jun 29 17:47 libguestfs-gfs2-1.36.5-1.el7.centos.x86_64.rpm
-rw-r--r--   1 ahurt  staff    113560 Jun 29 17:47 libguestfs-gobject-1.36.5-1.el7.centos.x86_64.rpm
-rw-r--r--   1 ahurt  staff    124412 Jun 29 17:47 libguestfs-gobject-devel-1.36.5-1.el7.centos.x86_64.rpm
-rw-r--r--   1 ahurt  staff    200980 Jun 29 17:47 libguestfs-gobject-doc-1.36.5-1.el7.centos.noarch.rpm
-rw-r--r--   1 ahurt  staff      2496 Jun 29 17:47 libguestfs-hfsplus-1.36.5-1.el7.centos.x86_64.rpm
-rw-r--r--   1 ahurt  staff      2100 Jun 29 17:47 libguestfs-inspect-icons-1.36.5-1.el7.centos.noarch.rpm
-rw-r--r--   1 ahurt  staff    126328 Jun 29 17:47 libguestfs-java-1.36.5-1.el7.centos.x86_64.rpm
-rw-r--r--   1 ahurt  staff     10592 Jun 29 17:47 libguestfs-java-devel-1.36.5-1.el7.centos.x86_64.rpm
-rw-r--r--   1 ahurt  staff    144356 Jun 29 17:47 libguestfs-javadoc-1.36.5-1.el7.centos.noarch.rpm
-rw-r--r--   1 ahurt  staff    260716 Jun 29 17:47 libguestfs-live-service-1.36.5-1.el7.centos.x86_64.rpm
-rw-r--r--   1 ahurt  staff    724492 Jun 29 17:47 libguestfs-man-pages-ja-1.36.5-1.el7.centos.noarch.rpm
-rw-r--r--   1 ahurt  staff    730232 Jun 29 17:47 libguestfs-man-pages-uk-1.36.5-1.el7.centos.noarch.rpm
-rw-r--r--   1 ahurt  staff      2624 Jun 29 17:47 libguestfs-rescue-1.36.5-1.el7.centos.x86_64.rpm
-rw-r--r--   1 ahurt  staff      2460 Jun 29 17:47 libguestfs-rsync-1.36.5-1.el7.centos.x86_64.rpm
-rw-r--r--   1 ahurt  staff     21288 Jun 29 17:47 libguestfs-tools-1.36.5-1.el7.centos.noarch.rpm
-rw-r--r--   1 ahurt  staff   3205492 Jun 29 17:47 libguestfs-tools-c-1.36.5-1.el7.centos.x86_64.rpm
-rw-r--r--   1 ahurt  staff      2436 Jun 29 17:47 libguestfs-xfs-1.36.5-1.el7.centos.x86_64.rpm
-rw-r--r--   1 ahurt  staff    130820 Jun 29 17:47 lua-guestfs-1.36.5-1.el7.centos.x86_64.rpm
-rw-r--r--   1 ahurt  staff    249380 Jun 29 17:47 ocaml-libguestfs-1.36.5-1.el7.centos.x86_64.rpm
-rw-r--r--   1 ahurt  staff    269324 Jun 29 17:47 ocaml-libguestfs-devel-1.36.5-1.el7.centos.x86_64.rpm
-rw-r--r--   1 ahurt  staff    159573 Jun 29 17:47 ocaml-libvirt-0.6.1.4-18.el7.centos.src.rpm
-rw-r--r--   1 ahurt  staff     96188 Jun 29 17:47 ocaml-libvirt-0.6.1.4-18.el7.centos.x86_64.rpm
-rw-r--r--   1 ahurt  staff     71752 Jun 29 17:47 ocaml-libvirt-debuginfo-0.6.1.4-18.el7.centos.x86_64.rpm
-rw-r--r--   1 ahurt  staff    109524 Jun 29 17:47 ocaml-libvirt-devel-0.6.1.4-18.el7.centos.x86_64.rpm
-rw-r--r--   1 ahurt  staff    319556 Jun 29 17:47 perl-Sys-Guestfs-1.36.5-1.el7.centos.x86_64.rpm
-rw-r--r--   1 ahurt  staff     79364 Jun 29 17:47 php-libguestfs-1.36.5-1.el7.centos.x86_64.rpm
-rw-r--r--   1 ahurt  staff    195836 Jun 29 17:47 python2-libguestfs-1.36.5-1.el7.centos.x86_64.rpm
-rw-r--r--   1 ahurt  staff    156888 Jun 29 17:47 ruby-libguestfs-1.36.5-1.el7.centos.x86_64.rpm
-rw-r--r--   1 ahurt  staff    547463 Jun 29 17:47 supermin-5.1.17-5.el7.centos.src.rpm
-rw-r--r--   1 ahurt  staff    632768 Jun 29 17:47 supermin-5.1.17-5.el7.centos.x86_64.rpm
-rw-r--r--   1 ahurt  staff      3120 Jun 29 17:47 supermin-devel-5.1.17-5.el7.centos.x86_64.rpm
-rw-r--r--   1 ahurt  staff    467152 Jun 29 17:47 virt-dib-1.36.5-1.el7.centos.x86_64.rpm
-rw-r--r--   1 ahurt  staff    206708 Jun 29 17:47 virt-p2v-maker-1.36.5-1.el7.centos.x86_64.rpm
-rw-r--r--   1 ahurt  staff   1027448 Jun 29 17:47 virt-v2v-1.36.5-1.el7.centos.x86_64.rpm
```
