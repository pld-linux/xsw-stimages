Summary:	XShipWars sounds (Star Trek theme)
Name:		xsw-stimages
Version:	1.7
Release:	1
License:	Modified GPL
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry
Source0:	ftp://fox.mit.edu/pub/%{name}/stimages%{version}.tgz
URL:		http://wolfpack.tfu.net/ShipWars/XShipWars/
Provides:	xsw-images
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix	/usr/X11R6

%description 
XShipWars is a highly customizable and massivly multiplayer space
gamming system designed for play entirly over the Internet.
This package contains StarTrek graphics theme for the game.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_datadir}/xshipwars/

cd $RPM_BUILD_ROOT/%{_datadir}/xshipwars/
tar xzf %{SOURCE0}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/xshipwars/images/*
