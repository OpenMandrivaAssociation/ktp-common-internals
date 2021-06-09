Summary:	Internals for the KDE Telepathy IM suite
Name:		ktp-common-internals
Version:	21.04.2
Release:	1
Epoch:		1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Designer)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	cmake(Qt5Script)
BuildRequires:	cmake(Qt5ScriptTools)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(KF5Bookmarks)
BuildRequires:	cmake(KF5Codecs)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5People)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5TextEditor)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KAccounts)
BuildRequires:	cmake(AccountsQt5)
BuildRequires:	cmake(SignOnQt5)
BuildRequires:	cmake(TelepathyQt5)
BuildRequires:	cmake(TelepathyQt5Service)
BuildRequires:	cmake(TelepathyLoggerQt)
BuildRequires:	doxygen cmake(Doxygen)
BuildRequires:	pkgconfig(shared-mime-info)
BuildRequires:	pkgconfig(mission-control-plugins)
BuildRequires:	pkgconfig(libotr)
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(libaccounts-glib)
BuildRequires:	telepathy-accounts-signon
Requires:	telepathy-accounts-signon

%description
Internals for the KDE Telepathy IM suite

%define devname %{mklibname -d KTpCommonInternals}

%libpackage KTpCommonInternals 9
%{_libdir}/libKTpCommonInternals.so.%{version}
%libpackage KTpLogger 9
%{_libdir}/libKTpLogger.so.%{version}
%libpackage KTpModels 9
%{_libdir}/libKTpModels.so.%{version}
%libpackage KTpOTR 9
%{_libdir}/libKTpOTR.so.%{version}
%libpackage KTpWidgets 9
%{_libdir}/libKTpWidgets.so.%{version}

%package -n %{devname}
Summary: Development files for KTpCommonInternals
Group: Development/KDE and Qt
Requires: %{mklibname KTpCommonInternals 9} = %{EVRD}
Requires: %{mklibname KTpLogger 9} = %{EVRD}
Requires: %{mklibname KTpModels 9} = %{EVRD}
Requires: %{mklibname KTpOTR 9} = %{EVRD}
Requires: %{mklibname KTpWidgets 9} = %{EVRD}

%description -n %{devname}
Development files for KTpCommonInternals

%files -n %{devname}
%dir %{_includedir}/KTp
%{_includedir}/KTp/Logger
%{_includedir}/KTp/Models
%{_includedir}/KTp/OTR
%{_includedir}/KTp/Widgets
%{_includedir}/KTp/*.h
%{_libdir}/cmake/KTp
%{_datadir}/katepart5/syntax/ktpdebugoutput.xml
%{_libdir}/*.so

%files -f all.lang
%{_bindir}/ktp-debugger
%{_libdir}/libexec/ktp-proxy
%{_libdir}/qt5/plugins/kaccounts/daemonplugins/kaccounts_ktp_plugin.so
%{_libdir}/qt5/plugins/kpeople/actions/ktp_kpeople_plugin.so
%{_libdir}/qt5/plugins/kpeople/datasource/im_persons_data_source_plugin.so
%{_libdir}/qt5/plugins/kpeople/widgets/imdetailswidgetplugin.so
%{_libdir}/qt5/plugins/kpeople/widgets/kpeople_chat_plugin.so
%{_libdir}/qt5/plugins/ktploggerplugin_tplogger.so
%{_libdir}/qt5/qml/org/kde/telepathy
%{_datadir}/config.kcfg/ktp-proxy-config.kcfg
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.KTp.Proxy.service
%{_datadir}/knotifications5/ktelepathy.notifyrc
%{_datadir}/kservicetypes5/ktp_logger_plugin.desktop
%{_datadir}/telepathy/clients/KTp.Proxy.client
%{_datadir}/icons/*/*/*/*
%{_datadir}/kservices5/ktploggerplugin_tplogger.desktop

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang ktp-common-internals
%find_lang ktp-debugger
cat *.lang >all.lang
