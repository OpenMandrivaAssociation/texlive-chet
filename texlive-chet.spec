Name:		texlive-chet
Version:	45081
Release:	1
Summary:	LaTeX layout inspired by harvmac
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chet
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chet.r45081.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chet.doc.r45081.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
