Name:		wattsup
Version:	0.1
Release:	%mkrel 1
License:	GPLv2
Group:		Monitoring
Summary:	Program for controlling the Watts Up? Pro Device
Source:		LinuxUtility.zip

%description
Program for controlling the Watts Up? Pro Device.

%prep
%setup -q -c
%{__rm} -f wattsup.bin

%build
%__cc %optflags -o wattsup wattsup.c

%clean
%{__rm} -Rf %{buildroot}

%install
%{__rm} -Rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__cp} -p wattsup %{buildroot}%{_bindir}

%files
%defattr(-,root,root)
%doc utility.txt readme.txt
%{_bindir}/%{name}

