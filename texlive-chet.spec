# revision 24864
# category Package
# catalog-ctan /macros/latex/contrib/chet
# catalog-date 2011-12-18 14:52:40 +0100
# catalog-license lppl1.3
# catalog-version 1.4
Name:		texlive-chet
Version:	1.4
Release:	1
Summary:	LaTeX class inspired by harvmac
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

%pre
    %{_sbindir}/texlive.post

%post
    %{_sbindir}/texlive.post

%preun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

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
%doc %{_texmfdistdir}/doc/latex/chet/chetmacros.txt
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
