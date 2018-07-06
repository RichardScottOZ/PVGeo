__all__ = [
    'TranslateGridOrigin'
]

import vtk
from vtk.util import numpy_support as nps
import numpy as np
# Import Helpers:
from ..base import PVGeoAlgorithmBase
from .. import _helpers


#---- Translate Grid Origin ----#

class TranslateGridOrigin(PVGeoAlgorithmBase):
    """This filter will translate the origin of vtkImageData to any specified Corner of the data set assuming it is currently in the South West Bottom Corner (will not work if Corner was moved prior)."""
    def __init__(self, corner=1):
        PVGeoAlgorithmBase.__init__(self,
            nInputPorts=1, inputType='vtkImageData',
            nOutputPorts=1, outputType='vtkImageData')
        self.__corner = corner


    def _Translate(self, pdi, pdo):
        """
        TODO: Description
        """
        if pdo is None:
            pdo = vtk.vtkImageData()

        [nx, ny, nz] = pdi.GetDimensions()
        [sx, sy, sz] = pdi.GetSpacing()
        [ox, oy, oz] = pdi.GetOrigin()

        pdo.DeepCopy(pdi)

        xx,yy,zz = 0.0,0.0,0.0

        if self.__corner == 1:
            # South East Bottom
            xx = ox - (nx-1)*sx
            yy = oy
            zz = oz
        elif self.__corner == 2:
            # North West Bottom
            xx = ox
            yy = oy - (ny-1)*sy
            zz = oz
        elif self.__corner == 3:
            # North East Bottom
            xx = ox - (nx-1)*sx
            yy = oy - (ny-1)*sy
            zz = oz
        elif self.__corner == 4:
            # South West Top
            xx = ox
            yy = oy
            zz = oz - (nz-1)*sz
        elif self.__corner == 5:
            # South East Top
            xx = ox - (nx-1)*sx
            yy = oy
            zz = oz - (nz-1)*sz
        elif self.__corner == 6:
            # North West Top
            xx = ox
            yy = oy - (ny-1)*sy
            zz = oz - (nz-1)*sz
        elif self.__corner == 7:
            # North East Top
            xx = ox - (nx-1)*sx
            yy = oy - (ny-1)*sy
            zz = oz - (nz-1)*sz

        pdo.SetOrigin(xx, yy, zz)

        return pdo

    def RequestData(self, request, inInfo, outInfo):
        # Get input/output of Proxy
        pdi = self.GetInputData(inInfo, 0, 0)
        pdo = self.GetOutputData(outInfo, 0)
        # Perfrom task
        self._Translate(pdi, pdo)
        return 1


    #### Seters and Geters ####


    def SetCorner(self, corner):
        """an int to represent corner location
        <Entry value="1" text="South East Bottom"/>
        <Entry value="2" text="North West Bottom"/>
        <Entry value="3" text="North East Bottom"/>
        <Entry value="4" text="South West Top"/>
        <Entry value="5" text="South East Top"/>
        <Entry value="6" text="North West Top"/>
        <Entry value="7" text="North East Top"/>
        """
        if self.__corner != corner:
            self.__corner = corner
            self.Modified()
