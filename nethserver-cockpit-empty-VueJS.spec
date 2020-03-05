Name:           nethserver-cockpit-empty-VueJS
Version:        0.0.0
Release:        1%{?dist}
Summary:        Short description of NethServer Cockpit Empty for VueJS

License:        GPLv3
URL:            %{url_prefix}/%{name}
Source0:        %{name}-%{version}.tar.gz
# Execute prep-sources to create Source1
Source1:        %{name}.tar.gz
BuildArch:      noarch

BuildRequires:  nethserver-devtools
Requires:       nethserver-cockpit

%description
Very very very very very long description of NethServer Cockpit Empty

%prep
%setup

%build
%{makedocs}
perl createlinks
sed -i 's/_RELEASE_/%{version}/' %{name}.json

%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)

mkdir -p %{buildroot}/usr/share/cockpit/%{name}/
mkdir -p %{buildroot}/usr/share/cockpit/nethserver/applications/
mkdir -p %{buildroot}/usr/libexec/nethserver/api/%{name}/

tar xvf %{SOURCE1} -C %{buildroot}/usr/share/cockpit/%{name}/

cp -a %{name}.json %{buildroot}/usr/share/cockpit/nethserver/applications/
cp -a api/* %{buildroot}/usr/libexec/nethserver/api/%{name}/
chmod +x %{buildroot}/usr/libexec/nethserver/api/%{name}/*

%{genfilelist} %{buildroot} \
$RPM_BUILD_ROOT > e-smith-%{version}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f e-smith-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
%attr(0440,root,root) /etc/sudoers.d/50_nsapi_nethserver_cockpit_empty_VueJS

# Enable to create event link with createlinks
#%dir %{_nseventsdir}/%{name}-update

%changelog
