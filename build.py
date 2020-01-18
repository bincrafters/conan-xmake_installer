#!/usr/bin/env python

from bincrafters import build_template_installer


if __name__ == "__main__":

    builder = build_template_installer.get_builder()
    builder.add()
    builder.run()
