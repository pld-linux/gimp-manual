Summary:	The HTML version of the GIMP User Manual (GUM)
Summary(pl):	Wersja HTML podrêcznika u¿ytkownika do GIMP-a
Name:		gimp-manual
Version:	1.0.0
Release:	6
License:	OpenContent
Group:		Documentation
Group(de):	Dokumentation
Group(es):	Documentación
Group(pl):	Dokumentacja
Source0:	ftp://manual.gimp.org/pub/manual/GimpUserManual-%{version}-html.tar.bz2
URL:		http://manual.gimp.org/pub/manual/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
The gimp-manual package contains the GIMP (GNU Image Manipulation
Program) User Manual (GUM) in HTML format. Please note that the HTML
version of the GUM is not as good a quality as the other versions,
which can be obtained from the GUM website at
http://manual.gimp.org/pub/manual. On the GUM website, The manual is
provided in HTML (for viewing the GUM online), in PostScript(TM) and
PDF formats (for printing) as well as in FM (FrameMaker) source code.
The FrameMaker source code is provided for people who would like to
contribute to the Graphic Documentation Project. Submissions to the
GUM are covered by the manual's license agreement and terms, included
in the file COPYING.

The GUM is a complete guide for using the GIMP. This version of the
GUM includes improvements over previous versions. Be sure to check out
the new Gallery chapter, which provides a good overview of what the
GIMP can do. The Gallery displays cool images and give you hints on
how to create them with the GIMP.

For more information about the GUM, check the GUM website at
http://manual.gimp.org/.

%description -l pl
Pakiet gimp-manual zawiera podrêcznik u¿ytkownika (GUM) programu GIMP
(GNU Image Manipulation Program) w formacie HTML. Nale¿y zwróciæ uwagê
na fakt, ¿e HTML-owa wersja podrêcznika nie jest tak dobrej jako¶ci
jak inne wersje, które mo¿na ¶ci±gn±æ z oficjalnej strony GUM:
http://manual.gimp.org/pub/manual/. Na internetowej stronie GUM mo¿na
zaopatrzyæ siê w postscriptow± i pdf-ow± wersjê podrêcznika, jak
równie¿ uzyskaæ ¼ród³a dla FrameMakera. Kod ¼ród³owy FrameMakera jest
dla tych, którzy chcieliby mieæ swój udzia³ w Projekcie Dokumentacji
Graficznej. Dodatki do podrêcznika s± przyjmowane na zasadach licencji
podrêcznika, które mo¿na znale¼æ w pliku COPYING. GUM jest kompletnym
podrêcznikiem GIMP-a. Obecna wersja podrêcznika zawiera ulepszenia w
stosunku do poprzednich wersji. Nale¿y zapoznaæ siê z nowym rozdzia³em
"Galeria", który prezentuje przyzwoity przegl±d mo¿liwo¶ci GIMP-a.
Galeria zawiera interesuj±ce obrazki i zawiera wskazówki mówi±ce o
tym, jak samemu stworzyæ podobne dzie³a przy pomocy GIMP-a. Aby
dowiedzieæ siê wiêcej o GUM-ie, nale¿y odwiedziæ stronê WWW GUM-a:
http://manual.gimp.org/.

%prep
%setup -q -n GimpUserManaul_v1.0.0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *
