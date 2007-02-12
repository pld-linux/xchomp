Summary:	A Pac-Man style game for the X Window System
Summary(de.UTF-8):	Spiel im PacMan-Stil für X
Summary(es.UTF-8):	Juego tipo PacMan para X
Summary(fr.UTF-8):	Jeu de type PacMan pour X
Summary(pl.UTF-8):	Gra w stylu Pac-Mana pod X
Summary(pt_BR.UTF-8):	Jogo tipo PacMan para X
Summary(tr.UTF-8):	PacMan tarzı bilgisayar oyunu
Name:		xchomp
Version:	1.0
Release:	19
License:	distributable
Group:		X11/Applications/Games
Source0:	ftp://ibiblio.org/pub/Linux/games/arcade/tetris/%{name}-linux.tar.z
# Source0-md5:	f1556376445f2f38e61dc1f774e0d155
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-imake.patch
URL:		http://www.chez.com/vidalc/xchomp/xchomp.html
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xchomp is an X Window System based game like Pac-Man.

%description -l de.UTF-8
Mit xchomp kommt ein Arcade-Klassiker auf Ihren Bildschirm, hat
Ähnlichkeiten mit PacMan. Nicht so umfangreich wie das Original, macht
aber trotzdem noch viel Spaß!

%description -l es.UTF-8
El clásico PacMan llega a su pantalla con xchomp. No tan extenso como
el juego original, pero aún ¡muy genial!

%description -l fr.UTF-8
Le classique du jeu d'action sur arcade arrive sur votre ecran avec
xchomp, le clone du jeu PacMan.Il n'est certes pas aussi complet que
l'original, mais vous promet tout de meme de bon moments.

%description -l pl.UTF-8
xchomp jest grą podobną do Pac-Mana pod X Window System.

%description -l pt_BR.UTF-8
O clássico PacMan chega a sua tela com xchomp. Não tão extenso quanto
o jogo original, mas ainda muito legal!

%description -l tr.UTF-8
xchomp, PacMan'in (dobişko) Linux'a uyarlanmış hali.

%prep
%setup -q -n xchomp
%patch0 -p1

%build
xmkmf
%{__make} \
	CC="%{__cc}" \
	CDEBUGFLAGS="%{rpmcflags} -DFRAME_DELAY=2000"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
