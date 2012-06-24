Summary:	The HTML version of the GIMP User Manual (GUM)
Summary(es):	Versi�n HTML del manual del gimp
Summary(pl):	Wersja HTML podr�cznika u�ytkownika do GIMP-a
Summary(pt_BR):	Vers�o HTML do manual do gimp
Name:		gimp-manual
Version:	1.0.0
Release:	6
License:	OpenContent
Group:		Documentation
Group(de):	Dokumentation
Group(es):	Documentaci�n
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

%description -l es
Esta es la versi�n 1.0.0 del Manual del Usuario del GIMP (GUM). Es la
primera versi�n estable del manual, producto de casi un a�o de
trabajo. Est� disponible en HTML, PS, PDF y c�digo fuente FM
(FrameMaker). Por favor, lee el archivo COPYING para informaci�n sobre
los t�rminos de la licencia del manual. El manual tiene m�s o menos
590 p�ginas y varias mejoras con relaci�n a la versi�n anterior.
Aseg�rate de leer el cap�tulo "Gallery" que contiene muchas im�genes
bonitas y trucos de como crearlas. La "Gallery" es un buen ejemplo de
lo que puede ser hecho con GIMP. Todas las im�genes en el manual
fueron hechas exclusivamente con GIMP. La versi�n HTML es apropiada
para un manual online, en cuanto las versiones PS y PDF lo son para
impresi�n, o para tener un manual online con una mayor calidad. El
c�digo fuente FM es �til solamente para los interesados en contribuir
con el Proyecto de Documentaci�n Gr�fica. Las contribuciones para el
Manual del Usuario del GIMP ser�n liberadas de acuerdo con la licencia
contenida en el archivo COPYING. A pesar de la versi�n HTML del manual
ser conveniente para usarse como un manual online no tiene la misma
calidad de los formatos PDF y PostScript. Mejoras se har�n, en el
futuro, en la versi�n HTML. Esta versi�n ha tenido restricciones de
tiempo. Para obtener otros formatos de este manual visita
ftp://manual.gimp.org/pub/manual

%description -l pl
Pakiet gimp-manual zawiera podr�cznik u�ytkownika (GUM) programu GIMP
(GNU Image Manipulation Program) w formacie HTML. Nale�y zwr�ci� uwag�
na fakt, �e HTML-owa wersja podr�cznika nie jest tak dobrej jako�ci
jak inne wersje, kt�re mo�na �ci�gn�� z oficjalnej strony GUM:
http://manual.gimp.org/pub/manual/. Na internetowej stronie GUM mo�na
zaopatrzy� si� w postscriptow� i pdf-ow� wersj� podr�cznika, jak
r�wnie� uzyska� �r�d�a dla FrameMakera. Kod �r�d�owy FrameMakera jest
dla tych, kt�rzy chcieliby mie� sw�j udzia� w Projekcie Dokumentacji
Graficznej. Dodatki do podr�cznika s� przyjmowane na zasadach licencji
podr�cznika, kt�re mo�na znale�� w pliku COPYING. GUM jest kompletnym
podr�cznikiem GIMP-a. Obecna wersja podr�cznika zawiera ulepszenia w
stosunku do poprzednich wersji. Nale�y zapozna� si� z nowym rozdzia�em
"Galeria", kt�ry prezentuje przyzwoity przegl�d mo�liwo�ci GIMP-a.
Galeria zawiera interesuj�ce obrazki i zawiera wskaz�wki m�wi�ce o
tym, jak samemu stworzy� podobne dzie�a przy pomocy GIMP-a. Aby
dowiedzie� si� wi�cej o GUM-ie, nale�y odwiedzi� stron� WWW GUM-a:
http://manual.gimp.org/.

%description -l pt_BR
Esta � a vers�o 1.0.0 do Manual do Usu�rio do GIMP (GUM). � a primeira
vers�o est�vel do manual, produto de quase um ano de trabalho. Est�
dispon�vel em HTML, PS, PDF e c�digo fonte FM (FrameMaker). Por favor
leia o arquivo COPYING para informa��es sobre os termos de licen�a do
manual.

O manual tem mais ou menos 590 p�ginas e v�rias melhorias em rela��o �
vers�o anterior. Certifique-se de ler o cap�tulo "Gallery" que cont�m
muitas imagens bonitas e dicas de como cri�-las. A "Gallery" � um bom
exemplo do que pode ser feito com o GIMP. Todas as imagens no manual
foram feitas exclusivamente com o GIMP.

A vers�o HTML � apropriada para um manual online, enquanto as vers�es
PS e PDF s�o apropriadas para impress�o ou para ter um manual online
com maior qualidade. O c�digo fonte FM � �til somente para os
interessados em contribuir com o Projeto de Documenta��o Gr�fica. As
contribui��es para o Manual do Usu�rio do GIMP ser�o liberadas de
acordo com a licen�a contida no arquivo COPYING.

Apesar da vers�o HTML do manual ser conveniente para ser usada como um
manual on-line, n�o tem a mesma qualidade dos formatos PDF e
PostScript.

Para obter outros formatos deste manual visite
ftp://manual.gimp.org/pub/manual

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
