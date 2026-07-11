%global tl_name tikz-kalender
%global tl_revision 77915

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.6b
Release:	%{tl_revision}.1
Summary:	A LaTeX based calendar using TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-kalender
License:	cc-by-sa-1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-kalender.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-kalender.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
For usage see the example files tikz-kalender-example1.tex, tikz-
kalender-example2.tex, tikz-kalender-example3.tex, and *.events. The
Code is inspired by this document and is subject to the >>Creative
Commons attribution license (CC-BY-SA)<<. The class tikz-kalender
requires the package TikZ and the TikZ libraries calc and calendar.

