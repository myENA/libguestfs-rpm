%global opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)

Name:           ocaml-libvirt
Version:        0.6.1.4
Release:        18%{?dist}
Summary:        OCaml binding for libvirt
License:        LGPLv2+

URL:            http://libvirt.org/ocaml/
Source0:        http://libvirt.org/sources/ocaml/%{name}-%{version}.tar.gz

# Upstream patch to fix int types.
Patch1:         0001-Use-C99-standard-int64_t-instead-of-OCaml-defined-an.patch

# Upstream patch to add virDomainCreateXML binding.
Patch2:         0001-Add-a-binding-for-virDomainCreateXML.patch

# Upstream patches to fix error handling.
Patch3:         0001-Suppress-errors-to-stderr-and-use-thread-local-virEr.patch
Patch4:         0002-Don-t-bother-checking-return-from-virInitialize.patch

# Upstream patch to remove unused function.
Patch5:         0001-Remove-unused-not_supported-function.patch

# Upstream patches to tidy up warnings.
Patch6:         0001-Use-g-warn-error.patch
Patch7:         0002-Update-dependencies.patch

# Upstream patches to add binding for virConnectGetAllDomainStats.
Patch8:         0003-Add-a-binding-for-virConnectGetAllDomainStats-RHBZ-1.patch
Patch9:         0004-examples-Print-more-stats-in-the-get_all_domain_stat.patch
Patch10:        0005-Change-binding-of-virConnectGetAllDomainStats-to-ret.patch

BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-findlib-devel

BuildRequires:  libvirt-devel >= 0.2.1
BuildRequires:  perl
BuildRequires:  gawk


%description
OCaml binding for libvirt.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1


%build
%configure
make all doc
%if %opt
make opt
%endif


%install
# These rules work if the library uses 'ocamlfind install' to install itself.
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
mkdir -p $RPM_BUILD_ROOT%{_bindir}
%if %opt
make install-opt
%else
make install-byte
%endif


%files
%doc COPYING.LIB README ChangeLog
%{_libdir}/ocaml/libvirt
%if %opt
%exclude %{_libdir}/ocaml/libvirt/*.a
%exclude %{_libdir}/ocaml/libvirt/*.cmxa
%exclude %{_libdir}/ocaml/libvirt/*.cmx
%endif
%exclude %{_libdir}/ocaml/libvirt/*.mli
%{_libdir}/ocaml/stublibs/*.so
%{_libdir}/ocaml/stublibs/*.so.owner


%files devel
%doc COPYING.LIB README TODO.libvirt ChangeLog html/*
%if %opt
%{_libdir}/ocaml/libvirt/*.a
%{_libdir}/ocaml/libvirt/*.cmxa
%{_libdir}/ocaml/libvirt/*.cmx
%endif
%{_libdir}/ocaml/libvirt/*.mli


%changelog
