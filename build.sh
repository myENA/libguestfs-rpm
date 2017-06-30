#!/usr/bin/env bash
set -ex  ## we like things verbose

## ensure we have a full dev stack
sudo yum groupinstall -y "Development Tools"

## install other helpers
sudo yum install -y epel-release mock rpmdevtools rpm-devel

## setup our build path
rpmdev-setuptree

## link the specs
ln -sf /tmp/build/SPECS/*.spec $HOME/rpmbuild/SPECS/

## link the sources
find /tmp/build/SOURCES -type f -exec ln -sf {} $HOME/rpmbuild/SOURCES/ \;

## build and install supermin
sudo yum-builddep -y $HOME/rpmbuild/SPECS/supermin.spec
spectool -g -R $HOME/rpmbuild/SPECS/supermin.spec
rpmbuild -ba $HOME/rpmbuild/SPECS/supermin.spec
sudo yum -y install $HOME/rpmbuild/RPMS/x86_64/supermin*.rpm

## build and install ocaml-libvirt bindings
sudo yum-builddep -y $HOME/rpmbuild/SPECS/ocaml-libvirt.spec
spectool -g -R $HOME/rpmbuild/SPECS/ocaml-libvirt.spec
rpmbuild -ba $HOME/rpmbuild/SPECS/ocaml-libvirt.spec
sudo yum -y install $HOME/rpmbuild/RPMS/x86_64/ocaml-libvirt*

## install libguestfs builddeps
sudo yum-builddep -y $HOME/rpmbuild/SPECS/libguestfs.spec

## install newer automake from source
curl http://ftp.gnu.org/gnu/automake/automake-1.15.tar.gz > automake-1.15.tar.gz
tar -xzvf automake-1.15.tar.gz
pushd automake-1.15
./configure && make && sudo make install
popd

## just a little hack
sudo ln -sf /usr/local/bin/automake-1.15 /bin/automake-1.15

## build libguestfs
spectool -g -R $HOME/rpmbuild/SPECS/libguestfs.spec
rpmbuild -ba $HOME/rpmbuild/SPECS/libguestfs.spec

## copy built files out of the vagrant/docker environment
## skip if you are doing this manually
if [ -f /.dockerenv ] || [ -f /.doing_the_vagrant ]; then
    sudo cp -f $HOME/rpmbuild/RPMS/{x86_64,noarch}/*.rpm $HOME/rpmbuild/SRPMS/*.rpm /tmp/artifacts/
fi
