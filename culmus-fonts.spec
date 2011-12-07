%define fontname culmus
%define fontconf 65-%{fontname}

%define common_desc \
The culmus-fonts package contains fonts for the display of\
Hebrew from the Culmus project.


Name:           %{fontname}-fonts
Version:        0.103
Release:        7%{?dist}
Summary:        Fonts for Hebrew from Culmus project

Group:          User Interface/X
License:        GPLv2
URL:            http://culmus.sourceforge.net
Source0:        http://downloads.sourceforge.net/sourceforge/%{fontname}/%{fontname}-%{version}.tar.gz
Source1:        %{fontconf}-aharoni-clm.conf
Source2:        %{fontconf}-caladings-clm.conf
Source3:        %{fontconf}-david-clm.conf
Source4:        %{fontconf}-drugulin-clm.conf
Source5:        %{fontconf}-ellinia-clm.conf
Source6:        %{fontconf}-frank-ruehl-clm.conf
Source7:        %{fontconf}-miriam-clm.conf
Source8:        %{fontconf}-miriam-mono-clm.conf
Source9:        %{fontconf}-nachlieli-clm.conf
Source10:        http://downloads.sourceforge.net/sourceforge/%{fontname}/david-type1-%{version}.tar.gz
Obsoletes:      culmus-fonts < 0.102-1
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch:      noarch
BuildRequires:  fontpackages-devel

%description
%common_desc
Meta-package of Culmus fonts which installs various families of culmus project.

%package common
Summary:        Common files of culmus-fonts
Group:          User Interface/X
Requires:       fontpackages-filesystem
Obsoletes:      culmus-fonts < 0.102-1
%description common
%common_desc

This package consists of files used by other %{name} packages.


%package -n %{fontname}-fonts-compat
Summary:          Compatibility files of Culmus font families
Group:            User Interface/X
Provides:        culmus-fonts = %{version}-%{release}
Obsoletes:        %{fontname}-fonts-common < 0.102-5
Obsoletes:        %{fontname}-aharoni-clm-fonts < 0.102-5
Obsoletes:        %{fontname}-caladings-clm-fonts < 0.102-5
Obsoletes:        %{fontname}-david-clm-fonts < 0.102-5
Obsoletes:        %{fontname}-drugulin-clm-fonts < 0.102-5
Obsoletes:        %{fontname}-ellinia-clm-fonts < 0.102-5
Obsoletes:        %{fontname}-frank-ruehl-clm-fonts < 0.102-5
Obsoletes:        %{fontname}-miriam-clm-fonts < 0.102-5
Obsoletes:        %{fontname}-miriam-mono-clm-fonts < 0.102-5
Obsoletes:        %{fontname}-nachlieli-clm-fonts < 0.102-5
Obsoletes:        %{fontname}-yehuda-clm-fonts < 0.102-5
Obsoletes:        culmus-fonts < 0.103-5

Requires:         %{fontname}-fonts-common = %{version}-%{release}
Requires:         %{fontname}-aharoni-clm-fonts = %{version}-%{release}
Requires:         %{fontname}-caladings-clm-fonts = %{version}-%{release}
Requires:         %{fontname}-david-clm-fonts = %{version}-%{release}
Requires:         %{fontname}-drugulin-clm-fonts = %{version}-%{release}
Requires:         %{fontname}-ellinia-clm-fonts = %{version}-%{release}
Requires:         %{fontname}-frank-ruehl-clm-fonts = %{version}-%{release}
Requires:         %{fontname}-miriam-clm-fonts = %{version}-%{release}
Requires:         %{fontname}-miriam-mono-clm-fonts = %{version}-%{release}
Requires:         %{fontname}-nachlieli-clm-fonts = %{version}-%{release}
Requires:         %{fontname}-yehuda-clm-fonts = %{version}-%{release}

%description -n %{fontname}-fonts-compat
%common_desc
Meta-package for installing all font families of Culmus.
This package only exists to help transition culmus-fonts users to the new
package split. It will be removed after one distribution release cycle, please
do not reference it or depend on it in any way.


%files -n %{fontname}-fonts-compat


%package -n %{fontname}-aharoni-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-aharoni-clm-fonts
%common_desc

%_font_pkg -n aharoni-clm -f %{fontconf}-aharoni-clm.conf AharoniCLM-*.afm AharoniCLM-*.pfa

%package -n %{fontname}-caladings-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-caladings-clm-fonts
%common_desc

%_font_pkg -n caladings-clm -f %{fontconf}-caladings-clm.conf CaladingsCLM.afm CaladingsCLM.pfa

%package -n %{fontname}-david-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-david-clm-fonts
%common_desc

%_font_pkg -n david-clm -f %{fontconf}-david-clm.conf DavidCLM-*.ttf DavidCLM-*.afm DavidCLM-*.pfa

%package -n %{fontname}-drugulin-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-drugulin-clm-fonts
%common_desc

%_font_pkg -n drugulin-clm -f %{fontconf}-drugulin-clm.conf DrugulinCLM-*.afm DrugulinCLM-*.pfa

%package -n %{fontname}-ellinia-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-ellinia-clm-fonts
%common_desc

%_font_pkg -n ellinia-clm -f %{fontconf}-ellinia-clm.conf ElliniaCLM-*.afm ElliniaCLM-*.pfa

%package -n %{fontname}-frank-ruehl-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-frank-ruehl-clm-fonts
%common_desc

%_font_pkg -n frank-ruehl-clm -f %{fontconf}-frank-ruehl-clm.conf FrankRuehlCLM-*.afm FrankRuehlCLM-*.pfa

%package -n %{fontname}-miriam-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-miriam-clm-fonts
%common_desc

%_font_pkg -n miriam-clm -f %{fontconf}-miriam-clm.conf MiriamCLM-*.afm MiriamCLM-*.pfa

%package -n %{fontname}-miriam-mono-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-miriam-mono-clm-fonts
%common_desc

%_font_pkg -n miriam-mono-clm -f %{fontconf}-miriam-mono-clm.conf MiriamMonoCLM-*.afm MiriamMonoCLM-*.pfa

%package -n %{fontname}-nachlieli-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-nachlieli-clm-fonts
%common_desc

%_font_pkg -n nachlieli-clm -f %{fontconf}-nachlieli-clm.conf NachlieliCLM-*.afm NachlieliCLM-*.pfa

%package -n %{fontname}-yehuda-clm-fonts
Summary:        Fonts for Hebrew from Culmus project
Group:          User Interface/X
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-yehuda-clm-fonts
%common_desc

%_font_pkg -n yehuda-clm YehudaCLM-*.afm YehudaCLM-*.pfa

%prep
%setup -q -n %{fontname}-%{version}
%setup -c -q -a 10
mv %{fontname}-%{version}/* .
mv david-%{version}/* .

%build

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}
install -m 0644 -p *.afm %{buildroot}%{_fontdir}
install -m 0644 -p *.pfa %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-aharoni-clm.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-caladings-clm.conf
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-david-clm.conf
install -m 0644 -p %{SOURCE4} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-drugulin-clm.conf
install -m 0644 -p %{SOURCE5} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-ellinia-clm.conf
install -m 0644 -p %{SOURCE6} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-frank-ruehl-clm.conf
install -m 0644 -p %{SOURCE7} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-miriam-clm.conf
install -m 0644 -p %{SOURCE8} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-miriam-mono-clm.conf
install -m 0644 -p %{SOURCE9} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-nachlieli-clm.conf

for fconf in %{fontconf}-aharoni-clm.conf \
             %{fontconf}-caladings-clm.conf \
             %{fontconf}-david-clm.conf \
             %{fontconf}-drugulin-clm.conf \
             %{fontconf}-ellinia-clm.conf \
             %{fontconf}-frank-ruehl-clm.conf \
             %{fontconf}-miriam-clm.conf \
             %{fontconf}-miriam-mono-clm.conf \
             %{fontconf}-nachlieli-clm.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done


%clean
rm -fr %{buildroot}


%files common
%defattr(0644,root,root,0755)
%doc CHANGES GNU-GPL LICENSE LICENSE-BITSTREAM 

%dir %{_fontdir}


%changelog
* Tue May 04 2010 Pravin Satpute <psatpute@redhat.com> - 0.103-7 
- Resolves: bug 586834

* Wed Jan 20 2010 Pravin Satpute <psatpute@redhat.com> - 0.103-6
- updated .conf file priorities
- Resolves: bug 565386

* Wed Jan 20 2010 Pravin Satpute <psatpute@redhat.com> - 0.103-5
- Resolves: bug 556776

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.103-4.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.103-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 10 2009 Pravin Satpute <psatpute@redhat.com> - 0.103-3
- added DavidCLM afm and pfa
- bug 509694

* Wed Jul 08 2009 Pravin Satpute <psatpute@redhat.com> - 0.103-1
- upstream new release 0.103

* Tue Apr 14 2009 Rahul Bhalerao <rbhalera@redhat.com> - 0.102-6.fc11
- Rebuild for bug #491957.

* Thu Mar 19 2009 Rahul Bhalerao <rbhalera@redhat.com> - 0.102-5.fc11
- Corrected Obsoletes for compat.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.102-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 16 2009 Rahul Bhalerao <rbhalera@redhat.com> - 0.102-3.fc11
- Modified -compat.

* Mon Feb 09 2009 Rahul Bhalerao <rbhalera@redhat.com> - 0.102-2.fc11
- Created -compat for subpackage for smooth upgrade.

* Wed Feb 04 2009 Rahul Bhalerao <rbhalera@redhat.com> - 0.102-1.fc11
- Updated version.
- Following new font packaging guidelines.

* Wed Jul 23 2008 Rahul Bhalerao <rbhalera@redhat.com> - 0.101-5.fc10
- Obsoleted dead package fonts-hebrew

* Mon Oct 15 2007 Rahul Bhalerao <rbhalera@redhat.com> - 0.101-4.fc8
- License change

* Thu Oct 11 2007 Rahul Bhalerao <rbhalera@redhat.com> - 0.101-3.fc8
- Updated according to the review

* Thu Oct 04 2007 Rahul Bhalerao <rbhalera@redhat.com> - 0.101-2.fc8
- Using common spec template for font packages

* Thu Oct 04 2007 Rahul Bhalerao <rbhalera@redhat.com> - 0.101-1.fc8
- Font directory and package name corrected and updated the version

* Thu Oct 04 2007 Rahul Bhalerao <rbhalera@redhat.com> - 0.100-1.fc8
- Split package from fonts-hebrew to reflect upstream project name
