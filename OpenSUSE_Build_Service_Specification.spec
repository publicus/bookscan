# Note: This specfile was created with the help of the tutorial at https://docs.fedoraproject.org/en-US/Fedora_Draft_Documentation/0.1/html/Packagers_Guide/sect-Packagers_Guide-Creating_a_Basic_Spec_File.html

Name:           bookscan
Version:        0.1
Release:        1%{?dist}
Summary:        A single-camera solution for book scanning.

#Group:          
License:        ISC
URL:            https://github.com/publicus/bookscan
Source0:        https://github.com/publicus/bookscan/archive/Adding_Page_Size_as_Command_Line_Argument.tar.gz
#BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  cmake
BuildRequires:  opencv
BuildRequires:  opencv-devel
BuildRequires:  libopencv2_4
BuildRequires:  cpp5
BuildRequires:  gcc5

Requires:       opencv

%description
This program takes images of books (each picture including a two-page spread), detects special glyphs pasted in the corners of the book, and de-keystones and thereby digitally flattens the pages. It then automatically separates the pages into separate, cropped image files.

%prep
%setup -q


%build
#%configure
#make %{?_smp_mflags}
cmake -DCMAKE_CXX_COMPILER=g++-5 .
make

#%check
#make check

#%install
#rm -rf $RPM_BUILD_ROOT
#make install DESTDIR=$RPM_BUILD_ROOT


#%clean
#rm -rf $RPM_BUILD_ROOT


%files
#%defattr(-,root,root,-)

%doc markers_for_book_scanner.pdf markers_for_book_scanner.ai test_input.jpg

%changelog
* 2017-02-10 Jacob Levernier <j@adunumdatum.org> 0.1-1
- Added Specfile

