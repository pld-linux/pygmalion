Summary:	Multi platform oriented 3DCG environment for mainly POV-Ray
Summary(pl):	Wieloplatformowe ¶rodowisko 3DCG g³ównie dla POV-Raya
Name:		pygmalion
Version:	0.4pre2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/pygmalion3d/Pygmalion-%{version}.tar.gz
# Source0-md5:	4699189bb5e9bb72fe6601b3c384482e
Patch0:		%{name}-typos.patch
URL:		http://pygmalion3d.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel
BuildRequires:	automake
BuildRequires:	fltk-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A modeler for POVRAY.

%description -l pl
Modeler dla POV-Raya.

%prep
%setup -q -n Pygmalion-%{version}
%patch0 -p1

%build
install /usr/share/automake/config.* .
%configure2_13 \
	--with-includes=%{_includedir} \
	--with-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
