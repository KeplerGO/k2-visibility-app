# K2 Visibility API

***A web api to check the visibility of targets in K2 Campaign 16.***

## Example usage

The url:

    http://api.keplerscience.org/is-k2-observing?ra=129.9885&dec=14.6993&campaign=16

returns 'yes' because this position in the sky is being observed by a telemetered pixel in K2 Campaign 16.

In contrast, the url:

    http://api.keplerscience.org/is-k2-observing?ra=142.2121&dec=18.7463&campaign=16

returns 'no' because this position in the sky is not being observed.

Note: ra and dec must be in decimal degrees.
