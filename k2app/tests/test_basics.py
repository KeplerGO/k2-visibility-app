import os
import pandas as pd

from .. import PACKAGEDIR
from ..k2app import _is_k2_observing


def test_pixels():
    """Is the visibility function self-consistent with the data?"""
    pixel_db_fn = os.path.join(PACKAGEDIR, 'data',
                               'k2-c16-pixel-coordinates.feather')
    pixels = pd.read_feather(pixel_db_fn)
    for idx in range(len(pixels))[::20000]:
        ra = pixels.iloc[idx].ra
        dec = pixels.iloc[idx].dec
        assert _is_k2_observing(ra=ra, dec=dec)
        assert _is_k2_observing(ra=ra+2/3600., dec=dec-2/3600.)
        assert not _is_k2_observing(ra=ra+20., dec=dec-20)
