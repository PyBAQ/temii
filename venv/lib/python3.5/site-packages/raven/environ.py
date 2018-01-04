from __future__ import absolute_import
import sys


class Environ(object):
    """
    Singleton for environment and system properties.

    """

    @property
    def python_version(self):
        return sys.version_info

    @property
    def python_packages(self):
        raise NotImplementedError

    @property
    def git_sha(self):
        raise NotADirectoryError

    @property
    def platform(self):
        raise NotImplementedError
