# revision 32384
# category Package
# catalog-ctan /macros/latex/contrib/chet
# catalog-date 2013-12-11 21:08:43 +0100
# catalog-license lppl1.3
# catalog-version 1.6
Name:		texlive-chet
Version:	1.6
Release:	2
Summary:	LaTeX layout inspired by harvmac
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chet
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chet.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chet.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is designed to streamline the work of typesetting,
and to provide the look and feel of harvmac for readers.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/chet/chetref.bst
%{_texmfdistdir}/tex/latex/chet/chet.sty
%doc %{_texmfdistdir}/doc/latex/chet/README
%doc %{_texmfdistdir}/doc/latex/chet/chetdoc.pdf
%doc %{_texmfdistdir}/doc/latex/chet/chetdoc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
