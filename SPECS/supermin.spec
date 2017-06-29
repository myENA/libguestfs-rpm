%ifnarch %{ocaml_native_compiler}
%global __strip /bin/true
%global debug_package %{nil}
%endif

# _hardened_build breaks building the static 'init' binary.
# https://bugzilla.redhat.com/show_bug.cgi?id=1202091
# https://bugzilla.redhat.com/show_bug.cgi?id=1204162
%undefine _hardened_build

# Whether we should verify tarball signature with GPGv2.
%global verify_tarball_signature 1

Summary:       Tool for creating supermin appliances
Name:          supermin
Version:       5.1.17
Release:       5%{?dist}
License:       GPLv2+

%if 0%{?rhel} >= 7
ExclusiveArch: x86_64
%endif

URL:           http://people.redhat.com/~rjones/supermin/
Source0:       http://libguestfs.org/download/supermin/%{name}-%{version}.tar.gz
%if 0%{verify_tarball_signature}
Source1:       http://libguestfs.org/download/supermin/%{name}-%{version}.tar.gz.sig
%endif

# Keyring used to verify tarball signature.
%if 0%{verify_tarball_signature}
Source2:       libguestfs.keyring
%endif

BuildRequires: /usr/bin/pod2man
BuildRequires: /usr/bin/pod2html
BuildRequires: rpm
BuildRequires: rpm-devel
BuildRequires: yum
BuildRequires: yum-utils
BuildRequires: /usr/sbin/mke2fs
BuildRequires: e2fsprogs-devel
BuildRequires: findutils
BuildRequires: glibc-static
BuildRequires: ocaml, ocaml-findlib-devel
%if 0%{verify_tarball_signature}
BuildRequires: gnupg2
%endif

# These are required only to run the tests.  We could patch out the
# tests to not require these packages.
BuildRequires: augeas hivex kernel tar

# For complicated reasons, this is required so that
# /bin/kernel-install puts the kernel directly into /boot, instead of
# into a /boot/<machine-id> subdirectory (in Fedora >= 23).  Read the
# kernel-install script to understand why.
BuildRequires: grubby
# https://bugzilla.redhat.com/show_bug.cgi?id=1331012
#BuildRequires: systemd-udev

Requires:      rpm
Requires:      yum
Requires:      yum-utils
Requires:      util-linux-ng
Requires:      cpio
Requires:      tar
Requires:      /usr/sbin/mke2fs
# RHBZ#771310
Requires:      e2fsprogs-libs >= 1.42
Requires:      findutils

# For automatic RPM dependency generation.
# See: http://www.rpm.org/wiki/PackagerDocs/DependencyGenerator
Source3:       supermin.attr
Source4:       supermin-find-requires


%description
Supermin is a tool for building supermin appliances.  These are tiny
appliances (similar to virtual machines), usually around 100KB in
size, which get fully instantiated on-the-fly in a fraction of a
second when you need to boot one of them.


%package devel
Summary:       Development tools for %{name}
Requires:      %{name} = %{version}-%{release}
Requires:      rpm-build


%description devel
%{name}-devel contains development tools for %{name}.

It just contains tools for automatic RPM dependency generation
from supermin appliances.


%prep
%if 0%{verify_tarball_signature}
tmphome="$(mktemp -d)"
gpgv2 --homedir "$tmphome" --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%endif
%setup -q
%autopatch -p1


%build
%configure --disable-network-tests
make %{?_smp_mflags}


%install
make DESTDIR=$RPM_BUILD_ROOT install

mkdir -p $RPM_BUILD_ROOT%{_rpmconfigdir}/fileattrs/
install -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_rpmconfigdir}/fileattrs/
install -m 0755 %{SOURCE4} $RPM_BUILD_ROOT%{_rpmconfigdir}/


%check

# Skip execstack test where it is known to fail.
%if 0%{?fedora} <= 20
%ifarch aarch64 %{arm}
export SKIP_TEST_EXECSTACK=1
%endif
%endif

make check || {
    cat tests/test-suite.log
    exit 1
}


%files
%doc COPYING README examples/build-basic-vm.sh
%{_bindir}/supermin
%{_mandir}/man1/supermin.1*


%files devel
%{_rpmconfigdir}/fileattrs/supermin.attr
%{_rpmconfigdir}/supermin-find-requires


%changelog
