%define	oname	ultrasphinx

Summary:	Ruby on Rails configurator and client to the Sphinx fulltext search engine
Name:		rubygem-%{oname}
Version:	1.11
Release:	%mkrel 1
License:	MIT
Group:		Development/Ruby
URL:		http://%{oname}.rubyforge.org/
Source0:	http://gems.rubyforge.org/gems/%{oname}-%{version}.gem
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ruby-RubyGems
Requires:	rubygem-chronic
BuildArch:	noarch

%description
Ruby on Rails configurator and client to the Sphinx fulltext search engine.

%prep

%build

%install
rm -rf %{buildroot}
gem install --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}
sed -e 's#/usr/local/bin#%{_bindir}#g' -i %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/test/integration/app/public/dispatch.{rb,cgi}
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/gems/%{oname}-%{version}
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec

