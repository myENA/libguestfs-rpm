# Architectures on which golang works.
%global golang_arches aarch64 % {arm} % {ix86} x86_64

%global _hardened_build 1

# Trim older changelog entries.
# https://lists.fedoraproject.org/pipermail/devel/2013-April/thread.html#181627
%global _changelog_trimtime %(date +%s -d "2 years ago")

# Verify tarball signature with GPGv2 (only possible for stable branches).
%global verify_tarball_signature 1

# Filter perl provides
%{?perl_default_filter}

Summary:       Access and modify virtual machine disk images
Name:          libguestfs
Epoch:         1
Version:       1.36.5
Release:       1%{?dist}
License:       LGPLv2+

# Source and patches.
URL:           http://libguestfs.org/
Source0:       http://libguestfs.org/download/1.36-stable/%{name}-%{version}.tar.gz
%if 0%{verify_tarball_signature}
Source1:       http://libguestfs.org/download/1.36-stable/%{name}-%{version}.tar.gz.sig
%endif

# libguestfs live service
Source2:       guestfsd.service
Source3:       99-guestfsd.rules

# Include rewritten and greatly improved virt-rescue from upstream.
# Patches can be found on the 'fedora-26' branch upstream:
# https://github.com/libguestfs/libguestfs/tree/fedora-26
Patch0001:     0001-generator-Deprecate-direct-mode-guestfs_set_direct-g.patch
Patch0002:     0002-New-API-internal-get-console-socket-to-support-virt-.patch
Patch0003:     0003-lib-Return-EPIPE-for-appliance-closed-the-connection.patch
Patch0004:     0004-rescue-Modify-virt-rescue-so-it-doesn-t-use-direct-m.patch
Patch0005:     0005-rescue-Implement-m-and-i-options.patch
Patch0006:     0006-rescue-Implement-escape-sequences.patch
Patch0007:     0007-rescue-Move-suggest-code-to-separate-file.patch
Patch0008:     0008-rescue-docs-It-is-no-longer-necessary-to-mount-files.patch
Patch0009:     0009-rescue-docs-Note-that-you-can-run-virt-rescue-on-dis.patch
Patch0010:     0010-rescue-Don-t-document-suggest-option-in-help-output.patch

# Replacement README file for Fedora users.
Source4:       README-replacement.in

# Guestfish colour prompts.
Source5:       guestfish.sh

# Used to build the supermin appliance in Koji.
Source6:       yum.conf.in

# Keyring used to verify tarball signature.
%if 0%{verify_tarball_signature}
Source7:       libguestfs.keyring
%endif

# Basic build requirements for the library and virt tools.
BuildRequires: gcc
BuildRequires: supermin-devel >= 5.1.12-4
BuildRequires: hivex-devel >= 1.2.7-7
BuildRequires: perl(Pod::Simple)
BuildRequires: perl(Pod::Man)
BuildRequires: /usr/bin/pod2text
BuildRequires: po4a
BuildRequires: augeas-devel >= 1.0.0-4
BuildRequires: readline-devel
BuildRequires: genisoimage
BuildRequires: libxml2-devel
BuildRequires: createrepo
BuildRequires: glibc-static
BuildRequires: libselinux-utils
BuildRequires: libselinux-devel
BuildRequires: fuse, fuse-devel
BuildRequires: pcre-devel
BuildRequires: file-devel
BuildRequires: libvirt-devel
BuildRequires: gperf
BuildRequires: flex
BuildRequires: bison
BuildRequires: libdb-utils
BuildRequires: cpio
BuildRequires: libconfig-devel
BuildRequires: xz-devel
BuildRequires: zip
BuildRequires: unzip
BuildRequires: systemd-units
BuildRequires: netpbm-progs
BuildRequires: icoutils
BuildRequires: qemu-kvm
BuildRequires: perl(Expect)
BuildRequires: libacl-devel
BuildRequires: libcap-devel
BuildRequires: yajl-devel
BuildRequires: systemd-devel
BuildRequires: bash-completion
BuildRequires: /usr/bin/ping
BuildRequires: /usr/bin/wget
BuildRequires: curl
BuildRequires: xz
BuildRequires: gtk3-devel
BuildRequires: /usr/bin/qemu-img
BuildRequires: perl(Win::Hivex)
BuildRequires: perl(Win::Hivex::Regedit)
%if 0%{verify_tarball_signature}
BuildRequires: gnupg2
%endif

# For language bindings.
BuildRequires: ocaml
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-findlib-devel
BuildRequires: ocaml-gettext-devel
BuildRequires: ocaml-ounit-devel
BuildRequires: ocaml-libvirt-devel >= 0.6.1.4-5
BuildRequires: lua
BuildRequires: lua-devel
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl-macros
BuildRequires: perl(Sys::Virt)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod) >= 1.00
BuildRequires: perl(Test::Pod::Coverage) >= 1.00
BuildRequires: perl(Module::Build)
BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(Locale::TextDomain)
BuildRequires: python-devel
BuildRequires: libvirt-python
BuildRequires: ruby-devel
BuildRequires: rubygem-rake
# json is not pulled in automatically, see RHBZ#1325022
BuildRequires: rubygem(json)
BuildRequires: rubygem(rdoc)
BuildRequires: rubygem(test-unit)
BuildRequires: ruby-irb
BuildRequires: java-1.8.0-openjdk
BuildRequires: java-1.8.0-openjdk-devel
BuildRequires: jpackage-utils
BuildRequires: php-devel
BuildRequires: erlang-erts
BuildRequires: erlang-erl_interface
BuildRequires: gobject-introspection-devel
BuildRequires: gjs
%ifarch %{golang_arches}
BuildRequires: golang
# This version is required for aarch64 to be supported by gcc-go.
%ifarch aarch64
BuildRequires: gcc >= 5.0.0-0.19.fc23
%endif
%endif

# Build requirements for the appliance.
#
# Get the initial list by doing:
#   for f in `cat appliance/packagelist`; do echo $f; done | sort -u
# However you have to edit the list down to packages which exist in
# current Fedora, since supermin ignores non-existent packages.
BuildRequires: acl attr augeas-libs bash binutils btrfs-progs bzip2 coreutils cpio cryptsetup curl debootstrap dhclient diffutils dosfstools e2fsprogs file findutils gawk gdisk genisoimage gfs2-utils grep gzip hivex iproute iputils kernel kmod kpartx less libcap libselinux libxml2 lsof lsscsi lvm2 lzop mdadm openssh-clients parted pciutils pcre policycoreutils procps psmisc qemu-img rsync scrub sed sleuthkit strace systemd tar udev util-linux vim-minimal which xfsprogs xz yajl zerofree
%ifnarch ppc
BuildRequires: hfsplus-tools
%endif
BuildRequires: ntfs-3g ntfsprogs
%ifarch %{ix86} x86_64
BuildRequires: syslinux syslinux-extlinux
%endif

# For complicated reasons, this is required so that
# /bin/kernel-install puts the kernel directly into /boot, instead of
# into a /boot/<machine-id> subdirectory (in Fedora >= 23).  Read the
# kernel-install script to understand why.
BuildRequires: grubby

# For building the appliance.
Requires:      supermin >= 5.1.12

# The daemon dependencies are not included automatically, because it
# is buried inside the appliance, so list them here.
Requires:      augeas-libs
Requires:      libacl
Requires:      libcap
Requires:      hivex
Requires:      pcre
Requires:      libselinux
Requires:      systemd-libs
Requires:      yajl

# For core inspection API.
Requires:      libdb-utils
Requires:      libosinfo

# For core mount-local (FUSE) API.
Requires:      fuse

# For core disk-create API.
Requires:      /usr/bin/qemu-img

Requires:      selinux-policy >= 3.11.1-63

# For UML backend (this backend only works on x86).
# UML has been broken upstream (in the kernel) for a while, so don't
# include this.  Note that uml_utilities also depends on Perl.
#% ifarch % {ix86} x86_64
#Requires:      uml_utilities
#% endif

# https://fedoraproject.org/wiki/Packaging:No_Bundled_Libraries#Packages_granted_exceptions
Provides:      bundled(gnulib)

# Someone managed to install libguestfs-winsupport (from RHEL!)  on
# Fedora, which breaks everything.  Thus:
Conflicts:     libguestfs-winsupport


%description
Libguestfs is a library for accessing and modifying virtual machine
disk images.  http://libguestfs.org

It can be used to make batch configuration changes to guests, get
disk used/free statistics (virt-df), migrate between hypervisors
(virt-p2v, virt-v2v), perform backups and guest clones, change
registry/UUID/hostname info, build guests from scratch (virt-builder)
and much more.

Libguestfs uses Linux kernel and qemu code, and can access any type of
guest filesystem that Linux and qemu can, including but not limited
to: ext2/3/4, btrfs, FAT and NTFS, LVM, many different disk partition
schemes, qcow, qcow2, vmdk.

Libguestfs for Fedora is split into several subpackages.  The basic
subpackages are:

               libguestfs  C library
         libguestfs-tools  virt-* tools, guestfish and guestmount (FUSE)
       libguestfs-tools-c  only the subset of virt tools written in C
                             (for reduced dependencies)
                 virt-dib  safe and secure diskimage-builder replacement
                 virt-v2v  convert virtual machines to run on KVM
                             (also known as V2V)
           virt-p2v-maker  convert physical machines to run on KVM
                             (also known as P2V)

For enhanced features, install:

     libguestfs-forensics  adds filesystem forensics support
          libguestfs-gfs2  adds Global Filesystem (GFS2) support
       libguestfs-hfsplus  adds HFS+ (Mac filesystem) support
 libguestfs-inspect-icons  adds support for inspecting guest icons
        libguestfs-rescue  enhances virt-rescue shell with more tools
         libguestfs-rsync  rsync to/from guest filesystems
           libguestfs-xfs  adds XFS support

Language bindings:

        erlang-libguestfs  Erlang bindings
 libguestfs-gobject-devel  GObject bindings and GObject Introspection
           golang-guestfs  Go language bindings
    libguestfs-java-devel  Java bindings
              lua-guestfs  Lua bindings
   ocaml-libguestfs-devel  OCaml bindings
         perl-Sys-Guestfs  Perl bindings
           php-libguestfs  PHP bindings
       python2-libguestfs  Python 2 bindings
          ruby-libguestfs  Ruby bindings

For developers:

         libguestfs-devel  C/C++ header files and library
  libguestfs-benchmarking  Benchmarking utilities


%ifarch aarch64 x86_64
%package benchmarking
Summary:       Benchmarking utilities for %{name}
Requires:      %{name} = %{epoch}:%{version}-%{release}


%description benchmarking
%{name}-benchmarking contains utilities for benchmarking and
performance analysis of %{name}, and also for general
understanding of the performance of the kernel and qemu when booting
small appliances.
%endif


%package devel
Summary:       Development tools and libraries for %{name}
Requires:      %{name} = %{epoch}:%{version}-%{release}
Requires:      pkgconfig

# For libguestfs-make-fixed-appliance.
Requires:      xz
Requires:      %{name}-tools-c = %{epoch}:%{version}-%{release}


%description devel
%{name}-devel contains development tools and libraries
for %{name}.


%package forensics
Summary:       Filesystem forensics support for %{name}
License:       LGPLv2+
Requires:      %{name} = %{epoch}:%{version}-%{release}

%description forensics
This adds filesystem forensics support to %{name}.  Install it if you
want to forensically analyze disk images using The Sleuth Kit.


%package gfs2
Summary:       GFS2 support for %{name}
License:       LGPLv2+
Requires:      %{name} = %{epoch}:%{version}-%{release}

%description gfs2
This adds GFS2 support to %{name}.  Install it if you want to process
disk images containing GFS2.


%ifnarch ppc
%package hfsplus
Summary:       HFS+ support for %{name}
License:       LGPLv2+
Requires:      %{name} = %{epoch}:%{version}-%{release}

%description hfsplus
This adds HFS+ support to %{name}.  Install it if you want to process
disk images containing HFS+ / Mac OS Extended filesystems.
%endif


%package rescue
Summary:       Additional tools for virt-rescue
License:       LGPLv2+
Requires:      %{name}-tools-c = %{epoch}:%{version}-%{release}

%description rescue
This adds additional tools to use inside the virt-rescue shell,
such as ssh, network utilities, editors and debugging utilities.


%package rsync
Summary:       rsync support for %{name}
License:       LGPLv2+
Requires:      %{name} = %{epoch}:%{version}-%{release}

%description rsync
This adds rsync support to %{name}.  Install it if you want to use
rsync to upload or download files into disk images.


%package xfs
Summary:       XFS support for %{name}
License:       LGPLv2+
Requires:      %{name} = %{epoch}:%{version}-%{release}

%description xfs
This adds XFS support to %{name}.  Install it if you want to process
disk images containing XFS.


%package inspect-icons
Summary:       Additional dependencies for inspecting guest icons
License:       LGPLv2+
BuildArch:     noarch
Requires:      %{name} = %{epoch}:%{version}-%{release}

Requires:      netpbm-progs
Requires:      icoutils


%description inspect-icons
%{name}-inspect-icons is a metapackage that pulls in additional
dependencies required by libguestfs to pull icons out of non-Linux
guests.  Install this package if you want libguestfs to be able to
inspect non-Linux guests and display icons from them.

The only reason this is a separate package is to avoid core libguestfs
having to depend on Perl.  See https://bugzilla.redhat.com/1194158


%package tools-c
Summary:       System administration tools for virtual machines
License:       GPLv2+
Requires:      %{name} = %{epoch}:%{version}-%{release}

# for guestfish:
#Requires:      /usr/bin/emacs #theoretically, but too large
Requires:      /usr/bin/hexedit
Requires:      /usr/bin/less
Requires:      /usr/bin/man
Requires:      /usr/bin/vi

# for virt-builder:
Requires:      gnupg
Requires:      xz
#Requires:     nbdkit, nbdkit-plugin-xz
Requires:      curl

%if 0%{?fedora} >= 23
Recommends:    libguestfs-xfs
%endif


%description tools-c
This package contains miscellaneous system administrator command line
tools for virtual machines.

Note that you should install %{name}-tools (which pulls in
this package).  This package is only used directly when you want
to avoid dependencies on Perl.


%package tools
Summary:       System administration tools for virtual machines
License:       GPLv2+
BuildArch:     noarch
Requires:      %{name} = %{epoch}:%{version}-%{release}
Requires:      %{name}-tools-c = %{epoch}:%{version}-%{release}

# NB: Only list deps here which are not picked up automatically.
Requires:      perl(Sys::Virt)
Requires:      perl(Win::Hivex) >= 1.2.7


%description tools
This package contains miscellaneous system administrator command line
tools for virtual machines.

Guestfish is the Filesystem Interactive SHell, for accessing and
modifying virtual machine disk images from the command line and shell
scripts.

The guestmount command lets you mount guest filesystems on the host
using FUSE and %{name}.

Virt-alignment-scan scans virtual machines looking for partition
alignment problems.

Virt-builder is a command line tool for rapidly making disk images
of popular free operating systems.

Virt-cat is a command line tool to display the contents of a file in a
virtual machine.

Virt-copy-in and virt-copy-out are command line tools for uploading
and downloading files and directories to and from virtual machines.

Virt-customize is a command line tool for customizing virtual machine
disk images.

Virt-df is a command line tool to display free space on virtual
machine filesystems.  Unlike other tools, it doesn’t just display the
amount of space allocated to a virtual machine, but can look inside
the virtual machine to see how much space is really being used.  It is
like the df(1) command, but for virtual machines, except that it also
works for Windows virtual machines.

Virt-diff shows the differences between virtual machines.

Virt-edit is a command line tool to edit the contents of a file in a
virtual machine.

Virt-filesystems is a command line tool to display the filesystems,
partitions, block devices, LVs, VGs and PVs found in a disk image
or virtual machine.  It replaces the deprecated programs
virt-list-filesystems and virt-list-partitions with a much more
capable tool.

Virt-format is a command line tool to erase and make blank disks.

Virt-get-kernel extracts a kernel/initrd from a disk image.

Virt-inspector examines a virtual machine and tries to determine the
version of the OS, the kernel version, what drivers are installed,
whether the virtual machine is fully virtualized (FV) or
para-virtualized (PV), what applications are installed and more.

Virt-log is a command line tool to display the log files from a
virtual machine.

Virt-ls is a command line tool to list out files in a virtual machine.

Virt-make-fs is a command line tool to build a filesystem out of
a collection of files or a tarball.

Virt-rescue provides a rescue shell for making interactive,
unstructured fixes to virtual machines.

Virt-resize can resize existing virtual machine disk images.

Virt-sparsify makes virtual machine disk images sparse (thin-provisioned).

Virt-sysprep lets you reset or unconfigure virtual machines in
preparation for cloning them.

Virt-tail follows (tails) a log file within a guest, like 'tail -f'.

Virt-tar-in and virt-tar-out are archive, backup and upload tools
for virtual machines.  These replace the deprecated program virt-tar.

Virt-win-reg lets you look at and modify the Windows Registry of
Windows virtual machines.


%package -n virt-dib
Summary:       Safe and secure diskimage-builder replacement
License:       GPLv2+

Requires:      %{name} = %{epoch}:%{version}-%{release}


%description -n virt-dib
Virt-dib is a safe and secure alternative to the OpenStack
diskimage-builder command.  It is compatible with most
diskimage-builder elements.


%package -n virt-v2v
Summary:       Convert a virtual machine to run on KVM
License:       GPLv2+

Requires:      %{name} = %{epoch}:%{version}-%{release}
Requires:      %{name}-tools-c = %{epoch}:%{version}-%{release}

Requires:      gawk
Requires:      gzip
Requires:      unzip
Requires:      curl
Requires:      /usr/bin/virsh

# For rhsrvany.exe, used to install firstboot scripts in Windows guests.
Requires:      mingw32-srvany >= 1.0-13


%description -n virt-v2v
Virt-v2v converts virtual machines from non-KVM hypervisors
to run under KVM.

To convert physical machines, see the virt-p2v-maker package.


%package -n virt-p2v-maker
Summary:       Convert a physical machine to run on KVM
License:       GPLv2+

Requires:      gawk
Requires:      gzip

# virt-p2v-make-disk runs virt-builder:
Requires:      %{name}-tools-c = %{epoch}:%{version}-%{release}

# virt-p2v-make-kickstart runs strip:
Requires:      binutils


%description -n virt-p2v-maker
Virt-p2v converts (virtualizes) physical machines so they can be run
as virtual machines under KVM.

This package contains the tools needed to make a virt-p2v boot CD or
USB key which is booted on the physical machine to perform the
conversion.  You also need virt-v2v installed somewhere else to
complete the conversion.

To convert virtual machines from other hypervisors, see virt-v2v.


%package bash-completion
Summary:       Bash tab-completion scripts for %{name} tools
BuildArch:     noarch
Requires:      bash-completion >= 2.0
Requires:      %{name}-tools-c = %{epoch}:%{version}-%{release}


%description bash-completion
Install this package if you want intelligent bash tab-completion
for guestfish, guestmount and various virt-* tools.


%package live-service
Summary:       %{name} live service
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units


%description live-service
You can install just this package in virtual machines in order to
enable libguestfs live service (eg. guestfish --live), which lets you
safely edit files in running guests.

This daemon is *not* required by %{name}.


# https://fedoraproject.org/wiki/Packaging:ScriptletSnippets#Systemd
%post live-service
%systemd_post guestfsd.service
%preun live-service
%systemd_preun guestfsd.service
%postun live-service
%systemd_postun_with_restart guestfsd.service


%package -n ocaml-%{name}
Summary:       OCaml bindings for %{name}
Requires:      %{name} = %{epoch}:%{version}-%{release}


%description -n ocaml-%{name}
ocaml-%{name} contains OCaml bindings for %{name}.

This is for toplevel and scripting access only.  To compile OCaml
programs which use %{name} you will also need ocaml-%{name}-devel.


%package -n ocaml-%{name}-devel
Summary:       OCaml bindings for %{name}
Requires:      ocaml-%{name} = %{epoch}:%{version}-%{release}


%description -n ocaml-%{name}-devel
ocaml-%{name}-devel contains development libraries
required to use the OCaml bindings for %{name}.


%package -n perl-Sys-Guestfs
Summary:       Perl bindings for %{name} (Sys::Guestfs)
Requires:      %{name} = %{epoch}:%{version}-%{release}
Requires:      perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))


%description -n perl-Sys-Guestfs
perl-Sys-Guestfs contains Perl bindings for %{name} (Sys::Guestfs).


%package -n python2-%{name}
Summary:       Python 2 bindings for %{name}
Requires:      %{name} = %{epoch}:%{version}-%{release}
%{?python_provide:%python_provide python2-%{name}}


%description -n python2-%{name}
python2-%{name} contains Python 2 bindings for %{name}.


%package -n ruby-%{name}
Summary:       Ruby bindings for %{name}
Requires:      %{name} = %{epoch}:%{version}-%{release}
Requires:      ruby(release)
Requires:      ruby
Provides:      ruby(guestfs) = %{version}

%description -n ruby-%{name}
ruby-%{name} contains Ruby bindings for %{name}.


%package java
Summary:       Java bindings for %{name}
Requires:      %{name} = %{epoch}:%{version}-%{release}
Requires:      java-headless >= 1.5.0
Requires:      jpackage-utils

%description java
%{name}-java contains Java bindings for %{name}.

If you want to develop software in Java which uses %{name}, then
you will also need %{name}-java-devel.


%package java-devel
Summary:       Java development package for %{name}
Requires:      %{name} = %{epoch}:%{version}-%{release}
Requires:      %{name}-java = %{epoch}:%{version}-%{release}

%description java-devel
%{name}-java-devel contains the tools for developing Java software
using %{name}.

See also %{name}-javadoc.


%package javadoc
Summary:       Java documentation for %{name}
BuildArch:     noarch
Requires:      %{name} = %{epoch}:%{version}-%{release}
Requires:      %{name}-java = %{epoch}:%{version}-%{release}
Requires:      jpackage-utils

%description javadoc
%{name}-javadoc contains the Java documentation for %{name}.


%package -n php-%{name}
Summary:       PHP bindings for %{name}
Requires:      %{name} = %{epoch}:%{version}-%{release}
Requires:      php

%description -n php-%{name}
php-%{name} contains PHP bindings for %{name}.


%package -n erlang-%{name}
Summary:       Erlang bindings for %{name}
Requires:      %{name} = %{epoch}:%{version}-%{release}
Requires:      erlang-erts

%description -n erlang-%{name}
erlang-%{name} contains Erlang bindings for %{name}.


%package -n lua-guestfs
Summary:       Lua bindings for %{name}
Requires:      %{name} = %{epoch}:%{version}-%{release}
Requires:      lua

%description -n lua-guestfs
lua-guestfs contains Lua bindings for %{name}.


%package gobject
Summary:       GObject bindings for %{name}
Requires:      %{name} = %{epoch}:%{version}-%{release}

%description gobject
%{name}-gobject contains GObject bindings for %{name}.

To develop software against these bindings, you need to install
%{name}-gobject-devel.


%package gobject-devel
Summary:       GObject bindings for %{name}
Requires:      %{name}-gobject = %{epoch}:%{version}-%{release}
Requires:      gtk-doc

%description gobject-devel
%{name}-gobject contains GObject bindings for %{name}.

This package is needed if you want to write software using the
GObject bindings.  It also contains GObject Introspection information.


%package gobject-doc
Summary:       Documentation for %{name} GObject bindings
BuildArch:     noarch
Requires:      %{name}-gobject-devel = %{epoch}:%{version}-%{release}

%description gobject-doc
%{name}-gobject-doc contains documentation for
%{name} GObject bindings.


%ifarch %{golang_arches}
%package -n golang-guestfs
Summary:       Golang bindings for %{name}
BuildArch:     noarch
Requires:      %{name} = %{epoch}:%{version}-%{release}
Requires:      golang
Provides:      golang(libguestfs.org) = %{epoch}:%{version}-%{release}

%description -n golang-guestfs
golang-%{name} contains Go language bindings for %{name}.
%endif


%package man-pages-ja
Summary:       Japanese (ja) man pages for %{name}
BuildArch:     noarch
Requires:      %{name} = %{epoch}:%{version}-%{release}

%description man-pages-ja
%{name}-man-pages-ja contains Japanese (ja) man pages
for %{name}.


%package man-pages-uk
Summary:       Ukrainian (uk) man pages for %{name}
BuildArch:     noarch
Requires:      %{name} = %{epoch}:%{version}-%{release}

%description man-pages-uk
%{name}-man-pages-uk contains Ukrainian (uk) man pages
for %{name}.


%prep
%if 0%{verify_tarball_signature}
tmphome="$(mktemp -d)"
gpgv2 --homedir "$tmphome" --keyring %{SOURCE7} %{SOURCE1} %{SOURCE0}
%endif
%setup -q
%autopatch -p1

# For sVirt to work, the local temporary directory we use in the tests
# must be labelled the same way as /tmp.  This doesn't work if either
# the directory is on NFS (no SELinux labels) or if SELinux is
# disabled, hence the tests.
if [ "$(stat -f -L -c %T .)" != "nfs" ] && \
   [ "$(getenforce | tr '[A-Z]' '[a-z]')" != "disabled" ]; then
    chcon --reference=/tmp tmp
fi

# Replace developer-centric README that ships with libguestfs, with
# our replacement file.
mv README README.orig
sed 's/@VERSION@/%{version}/g' < %{SOURCE4} > README


%build
# Test if network is available.
ip addr list ||:
ip route list ||:
if ping -c 3 -w 20 8.8.8.8 && wget http://libguestfs.org -O /dev/null; then
  extra=
else
  mkdir repo
  # -n 1 because of RHBZ#980502.
  find /var/cache/{dnf,yum} -type f -name '*.rpm' -print0 | \
    xargs -0 -n 1 cp -t repo
  createrepo repo
  sed -e "s|@PWD@|$(pwd)|" %{SOURCE6} > yum.conf
  extra=--with-supermin-packager-config=$(pwd)/yum.conf
fi

%global localconfigure \
  %{configure} \\\
    --with-default-backend=libvirt \\\
    --with-extra="fedora=%{fedora},release=%{release},libvirt" \\\
    --enable-install-daemon \\\
    $extra
%ifnarch %{golang_arches}
%global localconfigure %{localconfigure} --disable-golang
%endif

# Building index-parse.c by hand works around a race condition in the
# autotools cruft, where two or more copies of yacc race with each
# other, resulting in a corrupted file.
#
# 'INSTALLDIRS' ensures that Perl and Ruby libs are installed in the
# vendor dir not the site dir.
%global localmake \
  make -j1 -C builder index-parse.c \
  make V=1 INSTALLDIRS=vendor %{?_smp_mflags}

%{localconfigure}
%{localmake}

# Tests are hard to run under docker / vagrant - nuke em

%install
# This file is creeping over 1 MB uncompressed, and since it is
# included in the -devel subpackage, compress it to reduce
# installation size.
gzip -9 ChangeLog

# 'INSTALLDIRS' ensures that Perl and Ruby libs are installed in the
# vendor dir not the site dir.
make DESTDIR=$RPM_BUILD_ROOT INSTALLDIRS=vendor install

# Delete static libraries.
rm $( find $RPM_BUILD_ROOT -name '*.a' | grep -v /ocaml/ )

# Delete libtool files.
find $RPM_BUILD_ROOT -name '*.la' -delete

# Delete some bogus Perl files.
find $RPM_BUILD_ROOT -name perllocal.pod -delete
find $RPM_BUILD_ROOT -name .packlist -delete
find $RPM_BUILD_ROOT -name '*.bs' -delete
find $RPM_BUILD_ROOT -name 'bindtests.pl' -delete

# Remove obsolete binaries (RHBZ#1213298).
rm $RPM_BUILD_ROOT%{_bindir}/virt-list-filesystems
rm $RPM_BUILD_ROOT%{_bindir}/virt-list-partitions
rm $RPM_BUILD_ROOT%{_bindir}/virt-tar
rm $RPM_BUILD_ROOT%{_mandir}/man1/virt-list-filesystems.1*
rm $RPM_BUILD_ROOT%{_mandir}/man1/virt-list-partitions.1*
rm $RPM_BUILD_ROOT%{_mandir}/man1/virt-tar.1*

# Don't use versioned jar file (RHBZ#1022133).
# See: https://bugzilla.redhat.com/show_bug.cgi?id=1022184#c4
mv $RPM_BUILD_ROOT%{_datadir}/java/%{name}-%{version}.jar \
  $RPM_BUILD_ROOT%{_datadir}/java/%{name}.jar

# golang: Ignore what libguestfs upstream installs, and just copy the
# source files to %{_datadir}/gocode/src.
%ifarch %{golang_arches}
rm -r $RPM_BUILD_ROOT/usr/lib/golang
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gocode/src
cp -a golang/src/libguestfs.org $RPM_BUILD_ROOT%{_datadir}/gocode/src
%endif

# Move installed documentation back to the source directory so
# we can install it using a %%doc rule.
mv $RPM_BUILD_ROOT%{_docdir}/libguestfs installed-docs
gzip --best installed-docs/*.xml

# Split up the monolithic packages file in the supermin appliance so
# we can install dependencies in subpackages.
pushd $RPM_BUILD_ROOT%{_libdir}/guestfs/supermin.d
function move_to
{
    grep -Ev "^$1$" < packages > packages-t
    mv packages-t packages
    echo "$1" >> "$2"
}
move_to curl            zz-packages-dib
move_to debootstrap     zz-packages-dib
move_to kpartx          zz-packages-dib
move_to qemu-img        zz-packages-dib
move_to which           zz-packages-dib
move_to sleuthkit       zz-packages-forensics
move_to gfs2-utils      zz-packages-gfs2
move_to hfsplus-tools   zz-packages-hfsplus
move_to iputils         zz-packages-rescue
move_to lsof            zz-packages-rescue
move_to openssh-clients zz-packages-rescue
move_to pciutils        zz-packages-rescue
move_to strace          zz-packages-rescue
move_to vim-minimal     zz-packages-rescue
move_to rsync           zz-packages-rsync
move_to xfsprogs        zz-packages-xfs
popd

# If there is a bogus dependency on kernel-*, rename it to 'kernel'
# instead.  This can happen for various reasons:
# - DNF picks kernel-debug instead of kernel.
# - Version of kernel-rt in brew > version of kernel.
# On all known architectures, depending on 'kernel' should
# mean "we need a kernel".
pushd $RPM_BUILD_ROOT%{_libdir}/guestfs/supermin.d
sed 's/^kernel-.*/kernel/' < packages > packages-t
mv packages-t packages
popd

# For the libguestfs-live-service subpackage install the systemd
# service and udev rules.
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/udev/rules.d
install -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_unitdir}
install -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_prefix}/lib/udev/rules.d
# This deals with UsrMove:
mv $RPM_BUILD_ROOT/lib/udev/rules.d/99-guestfs-serial.rules \
  $RPM_BUILD_ROOT%{_prefix}/lib/udev/rules.d

# Guestfish colour prompts.
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
install -m 0644 %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/profile.d

# Virt-tools data directory.  This contains a symlink to rhsrvany.exe
# which is satisfied by the dependency on mingw32-srvany.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/virt-tools
pushd $RPM_BUILD_ROOT%{_datadir}/virt-tools
ln -sf /usr/i686-w64-mingw32/sys-root/mingw/bin/rhsrvany.exe
popd

# Delete the v2v test harness (except for the man page).
rm -r $RPM_BUILD_ROOT%{_libdir}/ocaml/v2v_test_harness
rm -r $RPM_BUILD_ROOT%{_libdir}/ocaml/stublibs/dllv2v_test_harness*

# Remove the .gitignore file from ocaml/html which will be copied to docdir.
rm ocaml/html/.gitignore

%ifarch aarch64 x86_64
# Copy the benchmarking tools and man pages, since upstream doesn't
# install them by default.  NB Don't install the libtool wrapper scripts.
libtool --mode=install install -m 0755 utils/boot-analysis/boot-analysis $RPM_BUILD_ROOT%{_bindir}/libguestfs-boot-analysis
libtool --mode=install install -m 0755 utils/boot-benchmark/boot-benchmark $RPM_BUILD_ROOT%{_bindir}/libguestfs-boot-benchmark
install -m 0755 utils/boot-benchmark/boot-benchmark-range.pl $RPM_BUILD_ROOT%{_bindir}/libguestfs-boot-benchmark-range.pl
install -m 0644 utils/boot-analysis/boot-analysis.1 $RPM_BUILD_ROOT%{_mandir}/man1/libguestfs-boot-analysis.1
install -m 0644 utils/boot-benchmark/boot-benchmark.1 $RPM_BUILD_ROOT%{_mandir}/man1/libguestfs-boot-benchmark.1
%endif

# Find locale files.
%find_lang %{name}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post java -p /sbin/ldconfig

%postun java -p /sbin/ldconfig


%files -f %{name}.lang
%doc COPYING README
%{_bindir}/libguestfs-test-tool
%{_libdir}/guestfs/
%exclude %{_libdir}/guestfs/supermin.d/zz-packages-*
%{_libdir}/libguestfs.so.*
%{_mandir}/man1/guestfs-faq.1*
%{_mandir}/man1/guestfs-performance.1*
%{_mandir}/man1/guestfs-recipes.1*
%{_mandir}/man1/guestfs-release-notes.1*
%{_mandir}/man1/guestfs-security.1*
%{_mandir}/man1/libguestfs-test-tool.1*


%ifarch aarch64 x86_64
%files benchmarking
%{_bindir}/libguestfs-boot-analysis
%{_bindir}/libguestfs-boot-benchmark
%{_bindir}/libguestfs-boot-benchmark-range.pl
%{_mandir}/man1/libguestfs-boot-analysis.1*
%{_mandir}/man1/libguestfs-boot-benchmark.1*
%endif


%files devel
%doc AUTHORS BUGS ChangeLog.gz HACKING TODO README
%doc examples/*.c
%doc installed-docs/*
%{_libdir}/libguestfs.so
%{_sbindir}/libguestfs-make-fixed-appliance
%{_mandir}/man1/guestfs-building.1*
%{_mandir}/man1/guestfs-hacking.1*
%{_mandir}/man1/guestfs-internals.1*
%{_mandir}/man1/guestfs-testing.1*
%{_mandir}/man1/libguestfs-make-fixed-appliance.1*
%{_mandir}/man3/guestfs.3*
%{_mandir}/man3/guestfs-examples.3*
%{_mandir}/man3/libguestfs.3*
%{_includedir}/guestfs.h
%{_libdir}/pkgconfig/libguestfs.pc


%files forensics
%{_libdir}/guestfs/supermin.d/zz-packages-forensics

%files gfs2
%{_libdir}/guestfs/supermin.d/zz-packages-gfs2

%ifnarch ppc
%files hfsplus
%{_libdir}/guestfs/supermin.d/zz-packages-hfsplus
%endif

%files rsync
%{_libdir}/guestfs/supermin.d/zz-packages-rsync

%files rescue
%{_libdir}/guestfs/supermin.d/zz-packages-rescue

%files xfs
%{_libdir}/guestfs/supermin.d/zz-packages-xfs

%files inspect-icons
# no files


%files tools-c
%doc README
%config(noreplace) %{_sysconfdir}/libguestfs-tools.conf
%{_sysconfdir}/virt-builder
%dir %{_sysconfdir}/xdg/virt-builder
%dir %{_sysconfdir}/xdg/virt-builder/repos.d
%config %{_sysconfdir}/xdg/virt-builder/repos.d/*
%config %{_sysconfdir}/profile.d/guestfish.sh
%{_mandir}/man5/libguestfs-tools.conf.5*
%{_bindir}/guestfish
%{_mandir}/man1/guestfish.1*
%{_bindir}/guestmount
%{_mandir}/man1/guestmount.1*
%{_bindir}/guestunmount
%{_mandir}/man1/guestunmount.1*
%{_bindir}/virt-alignment-scan
%{_mandir}/man1/virt-alignment-scan.1*
%{_bindir}/virt-builder
%{_mandir}/man1/virt-builder.1*
%{_bindir}/virt-cat
%{_mandir}/man1/virt-cat.1*
%{_bindir}/virt-copy-in
%{_mandir}/man1/virt-copy-in.1*
%{_bindir}/virt-copy-out
%{_mandir}/man1/virt-copy-out.1*
%{_bindir}/virt-customize
%{_mandir}/man1/virt-customize.1*
%{_bindir}/virt-df
%{_mandir}/man1/virt-df.1*
%{_bindir}/virt-diff
%{_mandir}/man1/virt-diff.1*
%{_bindir}/virt-edit
%{_mandir}/man1/virt-edit.1*
%{_bindir}/virt-filesystems
%{_mandir}/man1/virt-filesystems.1*
%{_bindir}/virt-format
%{_mandir}/man1/virt-format.1*
%{_bindir}/virt-get-kernel
%{_mandir}/man1/virt-get-kernel.1*
%{_bindir}/virt-index-validate
%{_mandir}/man1/virt-index-validate.1*
%{_bindir}/virt-inspector
%{_mandir}/man1/virt-inspector.1*
%{_bindir}/virt-log
%{_mandir}/man1/virt-log.1*
%{_bindir}/virt-ls
%{_mandir}/man1/virt-ls.1*
%{_bindir}/virt-make-fs
%{_mandir}/man1/virt-make-fs.1*
%{_bindir}/virt-rescue
%{_mandir}/man1/virt-rescue.1*
%{_bindir}/virt-resize
%{_mandir}/man1/virt-resize.1*
%{_bindir}/virt-sparsify
%{_mandir}/man1/virt-sparsify.1*
%{_bindir}/virt-sysprep
%{_mandir}/man1/virt-sysprep.1*
%{_bindir}/virt-tail
%{_mandir}/man1/virt-tail.1*
%{_bindir}/virt-tar-in
%{_mandir}/man1/virt-tar-in.1*
%{_bindir}/virt-tar-out
%{_mandir}/man1/virt-tar-out.1*


%files tools
%doc README
%{_bindir}/virt-win-reg
%{_mandir}/man1/virt-win-reg.1*


%files -n virt-dib
%doc COPYING README
%{_bindir}/virt-dib
%{_mandir}/man1/virt-dib.1*
%{_libdir}/guestfs/supermin.d/zz-packages-dib


%files -n virt-v2v
%doc COPYING README v2v/TODO
%{_bindir}/virt-v2v
%{_bindir}/virt-v2v-copy-to-local
%{_mandir}/man1/virt-v2v.1*
%{_mandir}/man1/virt-v2v-copy-to-local.1*
%{_mandir}/man1/virt-v2v-test-harness.1*
%{_datadir}/virt-tools


%files -n virt-p2v-maker
%doc COPYING README
%{_bindir}/virt-p2v-make-disk
%{_bindir}/virt-p2v-make-kickstart
%{_bindir}/virt-p2v-make-kiwi
%{_mandir}/man1/virt-p2v.1*
%{_mandir}/man1/virt-p2v-make-disk.1*
%{_mandir}/man1/virt-p2v-make-kickstart.1*
%{_mandir}/man1/virt-p2v-make-kiwi.1*
%{_datadir}/virt-p2v
%{_libdir}/virt-p2v


%files bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/guestfish
%{_datadir}/bash-completion/completions/guestmount
%{_datadir}/bash-completion/completions/guestunmount
%{_datadir}/bash-completion/completions/virt-*


%files live-service
%doc COPYING README
%{_sbindir}/guestfsd
%{_unitdir}/guestfsd.service
%{_mandir}/man8/guestfsd.8*
%{_prefix}/lib/udev/rules.d/99-guestfsd.rules
%{_prefix}/lib/udev/rules.d/99-guestfs-serial.rules


%files -n ocaml-%{name}
%{_libdir}/ocaml/guestfs
%exclude %{_libdir}/ocaml/guestfs/*.a
%exclude %{_libdir}/ocaml/guestfs/*.cmxa
%exclude %{_libdir}/ocaml/guestfs/*.cmx
%exclude %{_libdir}/ocaml/guestfs/*.mli
%{_libdir}/ocaml/stublibs/dllmlguestfs.so
%{_libdir}/ocaml/stublibs/dllmlguestfs.so.owner


%files -n ocaml-%{name}-devel
%doc ocaml/examples/*.ml ocaml/html
%{_libdir}/ocaml/guestfs/*.a
%{_libdir}/ocaml/guestfs/*.cmxa
%{_libdir}/ocaml/guestfs/*.cmx
%{_libdir}/ocaml/guestfs/*.mli
%{_mandir}/man3/guestfs-ocaml.3*


%files -n perl-Sys-Guestfs
%doc perl/examples/*.pl
%{perl_vendorarch}/*
%{_mandir}/man3/Sys::Guestfs.3pm*
%{_mandir}/man3/guestfs-perl.3*


%files -n python2-%{name}
%doc python/examples/*.py
%{python2_sitearch}/libguestfsmod.so
%{python2_sitearch}/guestfs.py
%{python2_sitearch}/guestfs.pyc
%{python2_sitearch}/guestfs.pyo
%{_mandir}/man3/guestfs-python.3*


%files -n ruby-%{name}
%doc ruby/examples/*.rb
%doc ruby/doc/site/*
%{ruby_vendorlibdir}/guestfs.rb
%{ruby_vendorarchdir}/_guestfs.so
%{_mandir}/man3/guestfs-ruby.3*


%files java
%{_libdir}/libguestfs_jni*.so.*
%{_datadir}/java/*.jar


%files java-devel
%doc java/examples/*.java
%{_libdir}/libguestfs_jni*.so
%{_mandir}/man3/guestfs-java.3*


%files javadoc
%{_javadocdir}/%{name}


%files -n php-%{name}
%doc php/README-PHP
%dir %{_sysconfdir}/php.d
%{_sysconfdir}/php.d/guestfs_php.ini
%{_libdir}/php/modules/guestfs_php.so


%files -n erlang-%{name}
%doc erlang/README
%doc erlang/examples/*.erl
%doc erlang/examples/LICENSE
%{_bindir}/erl-guestfs
%{_libdir}/erlang/lib/%{name}-%{version}
%{_mandir}/man3/guestfs-erlang.3*


%files -n lua-guestfs
%doc lua/examples/*.lua
%doc lua/examples/LICENSE
%{_libdir}/lua/*/guestfs.so
%{_mandir}/man3/guestfs-lua.3*


%files gobject
%{_libdir}/libguestfs-gobject-1.0.so.0*
%{_libdir}/girepository-1.0/Guestfs-1.0.typelib


%files gobject-devel
%{_libdir}/libguestfs-gobject-1.0.so
%{_includedir}/guestfs-gobject.h
%dir %{_includedir}/guestfs-gobject
%{_includedir}/guestfs-gobject/*.h
%{_datadir}/gir-1.0/Guestfs-1.0.gir
%{_libdir}/pkgconfig/libguestfs-gobject-1.0.pc


%files gobject-doc
%{_datadir}/gtk-doc/html/guestfs


%ifarch %{golang_arches}
%files -n golang-guestfs
%doc golang/examples/*.go
%doc golang/examples/LICENSE
%{_datadir}/gocode/src/libguestfs.org
%{_mandir}/man3/guestfs-golang.3*
%endif


%files man-pages-ja
%lang(ja) %{_mandir}/ja/man1/*.1*
%lang(ja) %{_mandir}/ja/man3/*.3*
%lang(ja) %{_mandir}/ja/man5/*.5*


%files man-pages-uk
%lang(uk) %{_mandir}/uk/man1/*.1*
%lang(uk) %{_mandir}/uk/man3/*.3*
%lang(uk) %{_mandir}/uk/man5/*.5*


%changelog
* Thu Jun 29 2017 Aaron Hurt <ahurt@ena.com>
- Backported libguestfs-1.36.5-1.fc25
- https://koji.fedoraproject.org/koji/buildinfo?buildID=910937
