"""Simple webservice which tells a user whether K2 is observing a point in the sky.

Example usage
-------------
The url:
    /is-k2-observing?ra=129.9885&dec=14.6993&campaign=16
Will return 'yes' or 'no'.
"""
import os
import numpy as np
import pandas as pd

import flask
from flask import Flask, request

from . import PACKAGEDIR


k2app = Flask('k2app', static_url_path='')


def _is_k2_observing(ra, dec, campaign=16, match_radius=4/3600.):
    pixel_db_fn = os.path.join(PACKAGEDIR, 'data',
                               'k2-c{}-pixel-coordinates.feather'.format(campaign))
    try:
        pixels = pd.read_feather(pixel_db_fn)
    except IOError:
        raise NotImplementedError("This service does not support Campaign {} at this time.".format(campaign))
    dist = np.hypot((ra - pixels.ra) * np.cos(np.radians(dec)),
                    dec - pixels.dec)
    return (dist < match_radius).any()


@k2app.route('/')
def root():
    return k2app.send_static_file('index.html')


@k2app.route('/demo')
def demo():
    return flask.redirect("is-k2-observing?ra=129.9885&dec=14.6993")


@k2app.route('/is-k2-observing')
def is_k2_observing():
    campaign = request.args.get('campaign', default=17, type=int)
    ra = request.args.get('ra', default=None, type=float)
    dec = request.args.get('dec', default=None, type=float)
    if ra is None or dec is None:
        response = "ra and dec are required and must be floats"
    else:
        try:
            if _is_k2_observing(ra=ra, dec=dec, campaign=campaign):
                response = "yes"
            else:
                response = "no"
        except NotImplementedError as e:
            return str(e)
    return flask.Response(response, mimetype='text/plain')
