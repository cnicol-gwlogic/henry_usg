import numpy as np

from flopy.pakbase import Package
from flopy.utils import Util2d, Util3d


class ModflowDdf(Package):
    """
    Density-Driven Flow package class for MODFLOW-USG
    """

    def __init__(
        self,
        model,
        rhofresh=1000.0,
        rhostd=1025.0,
        cstd=1.0,
        ithickav=0,
        imph=0,
        isharp=0,
        extension="ddf",
        unitnumber=None,
    ):
        # set default unit number of one is not specified
        if unitnumber is None:
            unitnumber = ModflowDdf._defaultunit()

        # call base package constructor
        super().__init__(model, extension, self._ftype(), unitnumber)

        self.rhofresh = rhofresh
        self.rhostd = rhostd
        self.cstd = cstd
        self.ithickav = ithickav
        self.imph = imph
        self.isharp = isharp

        self.parent.add_package(self)
        return

    def write_file(self):
        """
        Write the package file.

        Returns
        -------
        None

        """
        # Open file for writing
        f_ddf = open(self.fn_path, "w")
        # Item 1: RHOFRESH, RHOSTD, CSTD, ITHICKAV, IMPH
        f_ddf.write(
            f"{self.rhofresh} {self.rhostd} {self.cstd} {self.ithickav} {self.imph} {self.isharp}\n"
            )

        return

    @staticmethod
    def _ftype():
        return "DDF"

    @staticmethod
    def _defaultunit():
        return 36
