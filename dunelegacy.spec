Name:		dunelegacy
Version:	0.96.2
Release:	2
Summary:	Open-source Dune II engine
License:	GPLv2+
Group:		Games/Strategy
URL:		http://dunelegacy.sourceforge.net/
Source0:	http://www.myway.de/richieland/%{name}-%{version}-src.tar.bz2
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL-devel
BuildRequires:	libstdc++-devel

%description
Lead one of three interplanetary houses, Atreides, Harkonnen or Ordos,
in an attempt to harvest the largest amount of spice from the sand
dunes. Exchange your spice stockpiles for credits through refinement
and build an army capable of thwarting attempts of the other houses to
stop your harvesting!

Dune Legacy is an effort by a handful of developers to revitalize the
first-ever real-time strategy game. The original game was the basis
for the hugely successful Command and Conquer series, and the gameplay
has been replicated an extended to a wide variety of storylines and
series.

NOTE: Original Dune 2 game files are needed.

%prep
%setup -q
%__sed -i s,"#!/usr/bin/env xdg-open",,g %{name}.desktop

%build
%configure2_5x
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

%__mkdir_p %{buildroot}%{_datadir}/applications
%__install -m 644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%__mkdir_p %{buildroot}%{_datadir}/pixmaps
%__install -m 644 %{name}-128x128.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%clean
%__rm -rf %{buildroot}

%files
%doc README ToDo.txt ChangeLog
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png



%changelog
* Wed Feb 22 2012 Andrey Bondrov <abondrov@mandriva.org> 0.96.2-1
+ Revision: 779233
- imported package dunelegacy

