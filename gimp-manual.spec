Name:		gimp-manual
Version:	1.0.0
Release:	5
Summary:	The HTML version of the GIMP User Manual (GUM).
Group:		Documentation
Copyright:	OpenContent
Source:		ftp://manual.gimp.org/pub/manual/GimpUserManual-1.0.0-html.tar.bz2
BuildRoot:	/tmp/%{name}-%{version}-root
BuildArch:	noarch

%description
The gimp-manual package contains the GIMP (GNU Image Manipulation Program)
User Manual (GUM) in HTML format. Please note that the HTML version of
the GUM is not as good a quality as the other versions, which can be
obtained from the GUM website at http://manual.gimp.org/pub/manual. On
the GUM website, The manual is provided in HTML (for viewing the GUM
online), in PostScript(TM) and PDF formats (for printing) as well as
in FM (FrameMaker) source code. The FrameMaker source code is provided for
people who would like to contribute to the Graphic Documentation Project.
Submissions to the GUM are covered by the manual's license agreement and
terms, included in the file COPYING.

The GUM is a complete guide for using the GIMP. This version of the GUM
includes improvements over previous versions. Be sure to check out the
new Gallery chapter, which provides a good overview of what the GIMP can
do. The Gallery displays cool images and give you hints on how to create
them with the GIMP.

For more information about the GUM, check the GUM website at
http://manual.gimp.org/.

%prep
%setup -q -n GimpUserManaul_v1.0.0

%build
echo Done

%install
rm -rf $RPM_BUILD_ROOT
echo Done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *
