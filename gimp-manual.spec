Summary:	The HTML version of the GIMP User Manual (GUM)
Summary(es.UTF-8):   Versión HTML del manual del gimp
Summary(pl.UTF-8):   Wersja HTML podręcznika użytkownika do GIMP-a
Summary(pt_BR.UTF-8):   Versão HTML do manual do gimp
Name:		gimp-manual
Version:	1.0.0
Release:	7
License:	OpenContent
Group:		Documentation
Source0:	ftp://manual.gimp.org/pub/manual/GimpUserManual-%{version}-html.tar.bz2
# Source0-md5:	e7e07c177c4682609257ea67ecf174d1
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
<http://manual.gimp.org/>.

%description -l es.UTF-8
Esta es la versión 1.0.0 del Manual del Usuario del GIMP (GUM). Es la
primera versión estable del manual, producto de casi un año de
trabajo. Está disponible en HTML, PS, PDF y código fuente FM
(FrameMaker). Por favor, lee el archivo COPYING para información sobre
los términos de la licencia del manual. El manual tiene más o menos
590 páginas y varias mejoras con relación a la versión anterior.
Asegúrate de leer el capítulo "Gallery" que contiene muchas imágenes
bonitas y trucos de como crearlas. La "Gallery" es un buen ejemplo de
lo que puede ser hecho con GIMP. Todas las imágenes en el manual
fueron hechas exclusivamente con GIMP. La versión HTML es apropiada
para un manual online, en cuanto las versiones PS y PDF lo son para
impresión, o para tener un manual online con una mayor calidad. El
código fuente FM es útil solamente para los interesados en contribuir
con el Proyecto de Documentación Gráfica. Las contribuciones para el
Manual del Usuario del GIMP serán liberadas de acuerdo con la licencia
contenida en el archivo COPYING. A pesar de la versión HTML del manual
ser conveniente para usarse como un manual online no tiene la misma
calidad de los formatos PDF y PostScript. Mejoras se harán, en el
futuro, en la versión HTML. Esta versión ha tenido restricciones de
tiempo. Para obtener otros formatos de este manual visita
ftp://manual.gimp.org/pub/manual/ .

%description -l pl.UTF-8
Pakiet gimp-manual zawiera podręcznik użytkownika (GUM) programu GIMP
(GNU Image Manipulation Program) w formacie HTML. Należy zwrócić uwagę
na fakt, że HTML-owa wersja podręcznika nie jest tak dobrej jakości
jak inne wersje, które można ściągnąć z oficjalnej strony GUM:
<http://manual.gimp.org/pub/manual/>. Na internetowej stronie GUM
można zaopatrzyć się w postscriptową i pdf-ową wersję podręcznika, jak
również uzyskać źródła dla FrameMakera. Kod źródłowy FrameMakera jest
dla tych, którzy chcieliby mieć swój udział w Projekcie Dokumentacji
Graficznej. Dodatki do podręcznika są przyjmowane na zasadach licencji
podręcznika, które można znaleźć w pliku COPYING. GUM jest kompletnym
podręcznikiem GIMP-a. Obecna wersja podręcznika zawiera ulepszenia w
stosunku do poprzednich wersji. Należy zapoznać się z nowym rozdziałem
"Galeria", który prezentuje przyzwoity przegląd możliwości GIMP-a.
Galeria zawiera interesujące obrazki i zawiera wskazówki mówiące o
tym, jak samemu stworzyć podobne dzieła przy pomocy GIMP-a. Aby
dowiedzieć się więcej o GUM-ie, należy odwiedzić stronę WWW GUM-a:
<http://manual.gimp.org/>.

%description -l pt_BR.UTF-8
Esta é a versão 1.0.0 do Manual do Usuário do GIMP (GUM). É a primeira
versão estável do manual, produto de quase um ano de trabalho. Está
disponível em HTML, PS, PDF e código fonte FM (FrameMaker). Por favor
leia o arquivo COPYING para informações sobre os termos de licença do
manual.

O manual tem mais ou menos 590 páginas e várias melhorias em relação à
versão anterior. Certifique-se de ler o capítulo "Gallery" que contém
muitas imagens bonitas e dicas de como criá-las. A "Gallery" é um bom
exemplo do que pode ser feito com o GIMP. Todas as imagens no manual
foram feitas exclusivamente com o GIMP.

A versão HTML é apropriada para um manual online, enquanto as versões
PS e PDF são apropriadas para impressão ou para ter um manual online
com maior qualidade. O código fonte FM é útil somente para os
interessados em contribuir com o Projeto de Documentação Gráfica. As
contribuições para o Manual do Usuário do GIMP serão liberadas de
acordo com a licença contida no arquivo COPYING.

Apesar da versão HTML do manual ser conveniente para ser usada como um
manual on-line, não tem a mesma qualidade dos formatos PDF e
PostScript.

Para obter outros formatos deste manual visite
ftp://manual.gimp.org/pub/manual/ .

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
