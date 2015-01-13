from __future__ import absolute_import

from logilab.common.configuration import OptionsManagerMixIn
from pylint.lint import PyLinter


class ProspectorLinter(PyLinter):  # pylint: disable=too-many-ancestors,too-many-public-methods

    def __init__(self, found_files, *args, **kwargs):
        self._files = found_files

        # set up the standard PyLint linter
        PyLinter.__init__(self, *args, **kwargs)

    def reset_options(self):
        # for example, we want to re-initialise the OptionsManagerMixin
        # to supress the config error warning
        # pylint: disable=non-parent-init-called
        OptionsManagerMixIn.__init__(self, usage=PyLinter.__doc__, quiet=True)

    def expand_files(self, modules):
        expanded = PyLinter.expand_files(self, modules)
        filtered = []
        for module in expanded:
            if self._files.check_module(module['path']):
                filtered.append(module)
        return filtered
