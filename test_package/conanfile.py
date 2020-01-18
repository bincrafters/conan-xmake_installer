from conans import ConanFile
import os


class TestPackageConan(ConanFile):

    def test(self):
        self.run("xmake lua versioninfo")
