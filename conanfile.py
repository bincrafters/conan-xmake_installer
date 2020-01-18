from conans import ConanFile, tools
import os


class XmakeInstallerConan(ConanFile):
    name = "xmake_installer"
    version = "2.2.3"
    description = "Installer for the xmake build system"
    topics = ("conan", "xmake", "tboox", "installer", "build_system")
    url = "https://github.com/bincrafters/conan-xmake_installer"
    homepage = "https://github.com/tboox/xmake"
    license = "MIT"
    settings = "os_build"
    _source_subfolder = "source_subfolder"

    # TODO: Implement build-from-source on all platforms to replace binary download
    # def source(self):
        # checksum = "c73d34805ab26d214f22fee74bf033942f91ce43bfc028663ffb910ad22c2c5d"
        # tools.get(f"{self.homepage}/archive/v{self.version}.tar.gz", sha256=checksum)
        # extracted_dir = "xmake-" + self.version
        # os.rename(extracted_dir, self._source_subfolder)      

    def build(self):
            if self.settings.os_build == "Windows":
                tools.download("https://github.com/tboox/xmake/releases/download/v2.2.3/xmake-v2.2.3.exe", "xmake.exe")
            else:
                # need simple instructions on build from source with standard build tools

    def package(self):
        self.copy(pattern="LICENSE.md", dst="licenses", src=self._source_subfolder)
        if self.settings.os_build == "Windows":
            self.copy(pattern="xmake.exe", dst="bin", src="core/build", keep_path=False)
        else:
            self.copy(pattern="*xmake", dst="bin", keep_path=False)

    def package_info(self):
        self.env_info.PATH.append(os.path.join(self.package_folder, "bin"))
