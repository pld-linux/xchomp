Summary:	A Pac-Man style game for the X Window System
Summary(de):	Spiel im PacMan-Stil für X
Summary(es):	Juego tipo PacMan para X
Summary(fr):	Jeu de type PacMan pour X
Summary(pl):	Gra w stylu Pac-Mana pod X
Summary(pt_BR):Jogo tipo PacMan para X
Summary(tr):	PacMan tarzý bilgisayar oyunu
Name:		xchomp
Version:	1.0
Release:	16
License:	distributable
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry
Source0:	ftp://ibiblio.org/pub/Linux/games/arcade/tetris/%{name}-linux.tar.z
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-imake.patch
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
xchomp is an X Window System based game like Pac-Man.

%description -l de
Mit xchomp kommt ein Arcade-Klassiker auf Ihren Bildschirm, hat
Ähnlichkeiten mit PacMan. Nicht so umfangreich wie das Original, macht
aber trotzdem noch viel Spaß!

%description -l es
El clásico PacMan llega a su pantalla con xchomp. No tan extenso como
el juego original, pero aún ¡muy genial!

%description -l fr
Le classique du jeu d'action sur arcade arrive sur votre ecran avec
xchomp, le clone du jeu PacMan.Il n'est certes pas aussi complet que
l'original, mais vous promet tout de meme de bon moments.

%description -l pl
xchomp jest gr± podobn± do Pac-Mana pod X Window System.

%description -l pt_BR
O clássico PacMan chega a sua tela com xchomp. Não tão extenso quanto
o jogo original, mas ainda muito legal!

%description -l tr
xchomp, PacMan'in (dobiþko) Linux'a uyarlanmýþ hali.

%prep
%setup -q -n xchomp
%patch -p1

%build
xmkmf
%{__make} CDEBUGFLAGS="%{rpmcflags} -DFRAME_DELAY=2000"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Games,%{_pixmapsdir}}

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Games/*
%{_pixmapsdir}/*
