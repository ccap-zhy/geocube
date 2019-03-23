# -*- coding: utf-8 -*-
"""
This contains exceptions for GeoCube.
"""


class GeoCubeError(RuntimeError):
    """Base GeoCube exception class."""


class VectorDataError(GeoCubeError):
    """This is for errors in the vector data passed into GeoCube."""


class RioXarrayError(RuntimeError):
    """This is the base exception for errors in the rioxarray extension."""


class NoDataInBounds(RioXarrayError):
    """This is for when there are no data in the bounds for clipping a raster."""


class OneDimensionalRaster(RioXarrayError):
    """This is an error when you have a 1 dimensional raster."""


class SingleVariableDataset(RioXarrayError):
    """This is for when you have a dataset with a single variable."""
