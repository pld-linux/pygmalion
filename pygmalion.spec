# TODO:
#  - fix Patch8
Summary:	Multi platform oriented 3DCG environment for mainly POV-Ray
Summary(pl):	Wieloplatformowe ¶rodowisko 3DCG g³ównie dla POV-Raya
Name:		pygmalion
Version:	0.4
Release:	0.2
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/pygmalion3d/%7EPygmalion-%{version}.tar.gz
# Source0-md5:	2b0db1f647628288192fadf9b4eacf4c
Patch0:		%{name}-typos.patch
Patch1:		%{name}-makefile.patch
Patch2:		%{name}-fltk_gl.patch
Patch3:		%{name}-namespace.patch
Patch4:		%{name}-iostream.patch
Patch5:		%{name}-sqrt.patch
Patch6:		%{name}-c++_erase.patch
Patch7:		%{name}-c++_insert.patch
# WARNING: this patch is obviously WRONG
Patch8:		%{name}-c++_push_back.patch
URL:		http://pygmalion3d.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fltk-gl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A modeler for POVRAY.

%description -l pl
Modeler dla POV-Raya.

%prep
%setup -q -n Pygmalion-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
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
