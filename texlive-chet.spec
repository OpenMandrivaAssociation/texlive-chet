# revision 24864
# category Package
# catalog-ctan /macros/latex/contrib/chet
# catalog-date 2011-12-18 14:52:40 +0100
# catalog-license lppl1.3
# catalog-version 1.4
Name:		texlive-chet
Version:	1.4
Release:	2
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
%doc %{_texmfdistdir}/doc/latex/chet/chetmacros.txt

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.4-2
+ Revision: 750155
- Rebuild to reduce used resources

* Mon Dec 26 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.4-1
+ Revision: 745166
- texlive-chet

* Thu Nov 10 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.3-2
+ Revision: 729637
- texlive-chet

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.3-1
+ Revision: 718052
- texlive-chet
- texlive-chet
- texlive-chet
- texlive-chet
- texlive-chet

