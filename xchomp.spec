Summary:	A Pac-Man style game for the X Window System
Summary(pl):	Gra w stylu Pac-Mana pod X
Name:		xchomp
Version:	1.0
Release:	16
License:	distributable
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry
# ugh, why in "tetris" directory???
Source0:	ftp://ibiblio.org/pub/Linux/games/arcade/tetris/%{name}-linux.tar.z
Source1:	%{name}.desktop
Patch0:		%{name}-imake.patch
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
xchomp is an X Window System based game like Pac-Man.

%description -l pl
xchomp jest gr± podobn± do Pac-Mana pod X Window System.

%prep
%setup -q -n xchomp
%patch -p1

%build
xmkmf
%{__make} CDEBUGFLAGS="%{rpmcflags} -DFRAME_DELAY=2000"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Games
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Games/*
