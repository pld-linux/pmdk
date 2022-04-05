#
# Conditional build:
%bcond_without	libfabric	# RPMEM component
%bcond_without	ndctl		# daxio component
%bcond_without	pandoc		# do not build manpages using pandoc
#
Summary:	Persistent Memory Development Kit
Summary(pl.UTF-8):	Persistent Memory Development Kit - oprogramowanie do obsługi pamięci nieulotnej
Name:		pmdk
Version:	1.8
Release:	2
License:	BSD
Group:		Applications/System
#Source0Download: https://github.com/pmem/pmdk/releases
Source0:	https://github.com/pmem/pmdk/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	c291191dc6c0a31c7b794de3eb85fd7f
URL:		http://pmem.io/pmdk/
%{?with_ndctl:BuildRequires:	daxctl-devel >= 64.1}
%{?with_libfabric:BuildRequires:	libfabric-devel >= 1.4.2}
%{?with_ndctl:BuildRequires:	ndctl-devel >= 64.1}
%{?with_pandoc:BuildRequires:	pandoc}
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.673
Requires:	%{name}-libs = %{version}-%{release}
ExclusiveArch:	%{x8664} aarch64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PMDK is a collection of libraries and utilities for using Non-Volatile
Memory.

This package contains command-line utility pmempool - standalone tool
for off-line pool management.

%description -l pl.UTF-8
PMDK to zbiór bibliotek i narzędzi do wykorzystywania pamięci
nieulotnej (Non-Volatile Memory).

Ten pakiet zawiera narzędzie linii poleceń pmemtool - samodzielne
narzędzie do zarządzania pamięcią off-line.

%package python
Summary:	Python based PMDK utilities
Summary(pl.UTF-8):	Narzędzia PMDK napisane w Pythonie
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description python
Python based PMDK utilities. Currently it contains:
- pmreorder: store reordering tool

%description python -l pl.UTF-8
Narzędzia PMDK napisane w Pythonie. Obecnie zawierają:
- pmreorder: narzędzie do zmiany kolejności zapisów

%package -n bash-completion-pmdk
Summary:	Bash completion for PMDK utilities
Summary(pl.UTF-8):	Bashowe uzupełnianie parametrów poleceń PMDK
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 2.0

%description -n bash-completion-pmdk
Bash completion for PMDK pmempool utility.

%description -n bash-completion-pmdk -l pl.UTF-8
Bashowe uzupełnianie parametrów polecenia PMDK pmempool.

%package libs
Summary:	Persistent Memory Development Kit shared libraries
Summary(pl.UTF-8):	Biblioteki współdzielone Persistent Memory Development Kit
Group:		Libraries

%description libs
This package contains a collection of libraries for using Non-Volatile
Memory (NVM):
- libpmem - basic pmem operations like flushing
- libpmemblk, libpmemlog, libpmemobj - pmem transactions
- libpmempool - persistent memory pool management

%description libs -l pl.UTF-8
Ten pakiet zawiera zestaw bibliotek do wykorzystywania pamięci
nieulotnej (NVM - Non-Volatile Memory):
- libpmem - podstawowe operacje pmem, takie jak flush
- libpmemblk, libpmemlog, libpmemobj - transakcje pmem
- libpmempool - zarządzanie pulą pamięci nieulotnej

%package devel
Summary:	Header files for PMDK libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek PMDK
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for PMDK libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek PMDK.

%package static
Summary:	Static PMDK libraries
Summary(pl.UTF-8):	Statyczne biblioteki PMDK
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static PMDK libraries.

%description static -l pl.UTF-8
Statyczne biblioteki PMDK.

%package dax
Summary:	PMDK utility for Device-DAX devices
Summary(pl.UTF-8):	Narzędzie PMDK do urządzeń Device-DAX
Group:		Applications/System
Requires:	%{name}-libs = %{version}-%{release}
Requires:	daxctl-libs >= 64.1
Requires:	ndctl-libs >= 64.1

%description dax
PMDK is a collection of libraries and utilities for using Non-Volatile
Memory.

This package contains command-line utility daxio - perform I/O on
Device-DAX devices or zero a Device-DAX device.

%description dax -l pl.UTF-8
PMDK to zbiór bibliotek i narzędzi do wykorzystywania pamięci
nieulotnej (Non-Volatile Memory).

Ten pakiet zawiera narzędzie linii poleceń daxio - wykonywanie
operacji we/wy lub zerowanie urządzeń Device-DAX.

%package rpmem
Summary:	PMDK process for remote persistent memory access
Summary(pl.UTF-8):	Proces PMDK do zdalnego dostępu do pamięci nieulotnej
Group:		Applications/System
Requires:	%{name}-rpmem-libs = %{version}-%{release}

%description rpmem
PMDK is a collection of libraries and utilities for using Non-Volatile
Memory.

This package contains rpmemd - librpmem target node process.

%description rpmem -l pl.UTF-8
PMDK to zbiór bibliotek i narzędzi do wykorzystywania pamięci
nieulotnej (Non-Volatile Memory).

Ten pakiet zawiera rpmemd - proces librpmem uruchamiany na docelowych
węzłach.

%package rpmem-libs
Summary:	Library for remote access to persistent memory
Summary(pl.UTF-8):	Biblioteka do zdalnego dostępu do pamięci nieulotnej
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libfabric >= 1.4.2

%description rpmem-libs
This package contains a collection of libraries for using Non-Volatile
Memory (NVM):
- librpmem - remote access to persistent memory (EXPERIMENTAL)

%description rpmem-libs -l pl.UTF-8
Ten pakiet zawiera zestaw bibliotek do wykorzystywania pamięci
nieulotnej (NVM - Non-Volatile Memory):
- librpmem - zdalny dostęp do pamięci nieulotnej (EKSPERYMENTALNA)

%package rpmem-devel
Summary:	Header file for rpmem library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki rpmem
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-rpmem-libs = %{version}-%{release}
Requires:	libfabric-devel >= 1.4.2

%description rpmem-devel
Header file for rpmem library.

%description rpmem-devel -l pl.UTF-8
Plik nagłówkowy biblioteki rpmem.

%package rpmem-static
Summary:	Static rpmem library
Summary(pl.UTF-8):	Statyczna biblioteka rpmem
Group:		Development/Libraries
Requires:	%{name}-rpmem-devel = %{version}-%{release}

%description rpmem-static
Static rpmem library.

%description rpmem-static -l pl.UTF-8
Statyczna biblioteka rpmem.

%prep
%setup -q

%build
%if !%{with pandoc}
touch .skip-doc
%endif
CFLAGS="%{rpmcflags} %{rpmcppflags}" \
%{__make} -j1 \
	CC="%{__cc}" \
	%{!?with_libfabric:BUILD_RPMEM=n} \
	%{?with_ndctl:NDCTL_ENABLE=y} \
	includedir=%{_includedir} \
	libdir=%{_libdir} \
	prefix=%{_prefix} \
	sysconfdir=%{_sysconfdir}

%install
rm -rf $RPM_BUILD_ROOT

%if %{with pandoc}
%{__make} install \
%else
%{__make} -C src install \
%endif
	DESTDIR=$RPM_BUILD_ROOT \
	%{!?with_libfabric:BUILD_RPMEM=n} \
	%{?with_ndctl:NDCTL_ENABLE=y} \
	bashcompdir=%{bash_compdir} \
	includedir=%{_includedir} \
	libdir=%{_libdir} \
	prefix=%{_prefix} \
	sysconfdir=%{_sysconfdir}

# debug libraries - needed for anything?
%{__rm} -r $RPM_BUILD_ROOT%{_libdir}/pmdk_debug

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%post	rpmem-libs -p /sbin/ldconfig
%postun	rpmem-libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc src/tools/pmempool/README
%attr(755,root,root) %{_bindir}/pmempool
%if %{with pandoc}
%{_mandir}/man1/pmempool.1*
%{_mandir}/man1/pmempool-check.1*
%{_mandir}/man1/pmempool-convert.1*
%{_mandir}/man1/pmempool-create.1*
%{_mandir}/man1/pmempool-dump.1*
%{_mandir}/man1/pmempool-feature.1*
%{_mandir}/man1/pmempool-info.1*
%{_mandir}/man1/pmempool-rm.1*
%{_mandir}/man1/pmempool-sync.1*
%{_mandir}/man1/pmempool-transform.1*
%{_mandir}/man5/pmem_ctl.5*
%{_mandir}/man5/poolset.5*
%endif

%files python
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pmreorder
%if %{with pandoc}
%{_mandir}/man1/pmreorder.1*
%endif
%{_datadir}/pmreorder

%files -n bash-completion-pmdk
%defattr(644,root,root,755)
%{bash_compdir}/pmempool

%files libs
%defattr(644,root,root,755)
%doc ChangeLog LICENSE
%attr(755,root,root) %{_libdir}/libpmem.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpmem.so.1
%attr(755,root,root) %{_libdir}/libpmemblk.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpmemblk.so.1
%attr(755,root,root) %{_libdir}/libpmemlog.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpmemlog.so.1
%attr(755,root,root) %{_libdir}/libpmemobj.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpmemobj.so.1
%attr(755,root,root) %{_libdir}/libpmempool.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpmempool.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpmem.so
%attr(755,root,root) %{_libdir}/libpmemblk.so
%attr(755,root,root) %{_libdir}/libpmemlog.so
%attr(755,root,root) %{_libdir}/libpmemobj.so
%attr(755,root,root) %{_libdir}/libpmempool.so
%{_includedir}/libpmemobj
%{_includedir}/libpmem*.h
%{_pkgconfigdir}/libpmem.pc
%{_pkgconfigdir}/libpmemblk.pc
%{_pkgconfigdir}/libpmemlog.pc
%{_pkgconfigdir}/libpmemobj.pc
%{_pkgconfigdir}/libpmempool.pc
%if %{with pandoc}
%{_mandir}/man3/d_ro.3*
%{_mandir}/man3/d_rw.3*
%{_mandir}/man3/direct_ro.3*
%{_mandir}/man3/direct_rw.3*
%{_mandir}/man3/oid_equals.3*
%{_mandir}/man3/oid_instanceof.3*
%{_mandir}/man3/oid_is_null.3*
%{_mandir}/man3/pmem_*.3*
%{_mandir}/man3/pmemblk_*.3*
%{_mandir}/man3/pmemlog_*.3*
%{_mandir}/man3/pmemobj_*.3*
%{_mandir}/man3/pmempool_*.3*
%{_mandir}/man3/pobj_*.3*
%{_mandir}/man3/toid.3*
%{_mandir}/man3/toid_*.3*
%{_mandir}/man3/tx_*.3*
%{_mandir}/man7/libpmem.7*
%{_mandir}/man7/libpmemblk.7*
%{_mandir}/man7/libpmemlog.7*
%{_mandir}/man7/libpmemobj.7*
%{_mandir}/man7/libpmempool.7*
%endif

%files static
%defattr(644,root,root,755)
%{_libdir}/libpmem.a
%{_libdir}/libpmemblk.a
%{_libdir}/libpmemlog.a
%{_libdir}/libpmemobj.a
%{_libdir}/libpmempool.a

%if %{with ndctl}
%files dax
%defattr(644,root,root,755)
%doc src/tools/daxio/README
%attr(755,root,root) %{_bindir}/daxio
%if %{with pandoc}
%{_mandir}/man1/daxio.1*
%endif
%endif

%if %{with libfabric}
%files rpmem
%defattr(644,root,root,755)
%doc src/tools/rpmemd/README
%attr(755,root,root) %{_bindir}/rpmemd
%if %{with pandoc}
%{_mandir}/man1/rpmemd.1*
%endif

%files rpmem-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librpmem.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librpmem.so.1

%files rpmem-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librpmem.so
%{_includedir}/librpmem.h
%{_pkgconfigdir}/librpmem.pc
%if %{with pandoc}
%{_mandir}/man3/rpmem_*.3*
%{_mandir}/man7/librpmem.7*
%endif

%files rpmem-static
%defattr(644,root,root,755)
%{_libdir}/librpmem.a
%endif
