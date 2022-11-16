Name:		texlive-tikz-kalender
Version:	52890
Release:	1
Summary:	A LaTeX based calendar using TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tikz-kalender
License:	cc-by-sa-1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-kalender.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-kalender.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
For usage see the example files tikz-kalender-example1.tex,
tikz-kalender-example2.tex, and *.events. The Code is inspired
by this document and is subject to the >>Creative Commons
attribution license (CC-BY-SA)<<. The class tikz-kalender
requires the package TikZ and the TikZ libraries calc and
calendar.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tikz-kalender
%doc %{_texmfdistdir}/doc/latex/tikz-kalender

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
