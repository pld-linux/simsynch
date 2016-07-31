Summary:	SIMSYNTH - digital logic simulator
Summary(pl.UTF-8):	SIMSYNTH - cyfrowy symulator stanów logicznych
Name:		simsynch
Version:	1c5
Release:	1
License:	GPL v3+
Group:		Development/Languages/Scheme
Source0:	http://groups.csail.mit.edu/mac/ftpdir/scm/synch-%{version}.zip
# Source0-md5:	d1865c3448403fd76e45b049d882c54e
Patch0:		%{name}-info.patch
Patch1:		%{name}-texinfo.patch
URL:		http://people.csail.mit.edu/jaffer/SIMSYNCH.html
BuildRequires:	texinfo
Requires:	scm
Requires:	slib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SIMSYNCH is a digital logic simulator. The design files are comprised
of Scheme definitions and expressions. These design files can be run
as a Scheme program at high speed. The design files can also be
translated into formats suitable for logic compilers.

%description -l pl.UTF-8
SIMSYNCH to cyfrowy symulator stanów logicznych. Pliki projektów
składają się z definicji i wyrażeń w języku Scheme. Mogą być
uruchamiane jako program Scheme z dużą szybkością. Pliki projektów
mogą być także tłumaczone na formaty nadające się dla kompilatorów
logicznych.

%prep
%setup -q -n synch
%patch0 -p1
%patch1 -p1

%build
# not autoconf-generated
./configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir}

%{__make} synch.info

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_infodir}

%{__make} install-info \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/synch
cp -p *.scm *.v *.vhd usercat $RPM_BUILD_ROOT%{_datadir}/synch

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc ANNOUNCE ChangeLog
%{_datadir}/synch
%{_infodir}/synch.info*
