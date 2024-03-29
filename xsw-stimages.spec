Summary:	XShipWars graphics (Star Trek theme)
Summary(pl.UTF-8):	Grafika do XShipWars (motyw Star Trek)
Name:		xsw-stimages
Version:	1.7
Release:	2
License:	GPL-like
Group:		Applications/Games
Source0:	ftp://gd.tuwien.ac.at/games/wolfpack/stimages%{version}.tar.bz
# Source0-md5:	a555d638f5276d01bf716685fec2e9ee
URL:		http://wolfpack.twu.net/ShipWars/XShipWars/
Provides:	xsw-images
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
XShipWars is a highly customizable and massivly multiplayer space
gamming system designed for play entirly over the Internet. This
package contains StarTrek graphics theme for the game.

%description -l pl.UTF-8
XShipWars to wysoko konfigurowalny system gry w przestrzeni kosmicznej
dla wielu graczy, zaprojektowany do grania przez Internet. Ten pakiet
zawiera motyw graficzny Star Trek dla tej gry.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xshipwars

cd $RPM_BUILD_ROOT%{_datadir}/xshipwars
tar xzf %{SOURCE0}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/xshipwars/images/*
