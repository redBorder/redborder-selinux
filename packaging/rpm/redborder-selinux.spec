Name: redborder-selinux
Version: %{__version}
Release: %{__release}%{?dist}
BuildArch: noarch
Summary: redborder selinux

Requires: policycoreutils-python-utils libselinux-utils
BuildRequires: policycoreutils-python-utils libselinux-utils

License: AGPL 3.0
URL: https://github.com/redBorder/redborder-selinux
Source0: %{name}-%{version}.tar.gz

%description
%{summary}

%prep
%setup -qn %{name}-%{version}

%build
mkdir -p build
/usr/bin/checkmodule -M -m -o build/redborder-manager.mod resources/selinux-policies/redborder-manager.te
/usr/bin/semodule_package -o build/redborder-manager.pp -m build/redborder-manager.mod
/usr/bin/checkmodule -M -m -o build/redborder-ips.mod resources/selinux-policies/redborder-ips.te
/usr/bin/semodule_package -o build/redborder-ips.pp -m build/redborder-ips.mod
/usr/bin/checkmodule -M -m -o build/redborder-proxy.mod resources/selinux-policies/redborder-proxy.te
/usr/bin/semodule_package -o build/redborder-proxy.pp -m build/redborder-proxy.mod

%install
mkdir -p %{buildroot}/etc/selinux
install -D -m 0644 build/redborder-manager.pp %{buildroot}/etc/selinux/
install -D -m 0644 build/redborder-ips.pp %{buildroot}/etc/selinux/
install -D -m 0644 build/redborder-proxy.pp %{buildroot}/etc/selinux/

%pre

%post
case "$1" in
  1)
    # This is an initial install.
    :
  ;;
  2)
    # This is an upgrade.
    semodule -l | grep redborder-manager &>/dev/null
    if [ $? -eq 0 ]; then
      semodule -r redborder-manager
    fi
    getenforce | grep -v Disabled && rpm -qa | grep redborder-manager &>/dev/null
    if [ $? -ne 0 ]; then
      semodule -i /etc/selinux/redborder-manager.pp
    fi 
    
    semodule -l | grep redborder-ips &>/dev/null
    if [ $? -eq 0 ]; then
      semodule -r redborder-ips
    fi
    getenforce | grep -v Disabled && rpm -qa | grep redborder-ips &>/dev/null
    if [ $? -eq 0 ]; then
      semodule -i /etc/selinux/redborder-ips.pp
    fi 

    semodule -l | grep redborder-proxy &>/dev/null
    if [ $? -eq 0 ]; then
      semodule -r redborder-proxy
    fi
    getenforce | grep -v Disabled && rpm -qa | grep redborder-proxy &>/dev/null
    if [ $? -eq 0 ]; then
      semodule -i /etc/selinux/redborder-proxy.pp
    fi 
  ;;
esac

%files
%defattr(0644,root,root)
/etc/selinux/redborder-manager.pp
/etc/selinux/redborder-ips.pp
/etc/selinux/redborder-proxy.pp

%doc

%changelog
* Wed Oct 30 2024 David Vanhoucke <dvanhoucke@redborder.com> - 0.0.2-1
- adding proxy
* Fri Mar 22 2024 David Vanhoucke <dvanhoucke@redborder.com> - 0.0.1-1
- first spec version
