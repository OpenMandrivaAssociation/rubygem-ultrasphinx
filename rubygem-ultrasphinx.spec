%define	oname	ultrasphinx

Summary:	Ruby on Rails configurator and client to the Sphinx fulltext search engine
Name:		rubygem-%{oname}
Version:	1.11
Release:	%mkrel 2
License:	Academic Free License (AFL) v. 3.0
Group:		Development/Ruby
URL:		http://%{oname}.rubyforge.org/
Source0:	http://gems.rubyforge.org/gems/%{oname}-%{version}.gem
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ruby-RubyGems
BuildArch:	noarch

%description
Ruby on Rails configurator and client to the Sphinx fulltext search engine.

%prep

%build

%install
rm -rf %{buildroot}
gem install -E -n %{buildroot}%{_bindir} --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}
rm -rf %{buildroot}%{ruby_gemdir}/{cache,gems/%{oname}-%{version}/ext}
find %{buildroot} -name \*.rb -o -name \*.cgi |xargs sed -e 's#/usr/local/bin/ruby#/usr/bin/env ruby#g' -i

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/gems/%{oname}-%{version}
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
