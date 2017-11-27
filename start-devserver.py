#!/usr/bin/env python
"""Starts the Flask app in debug mode.

Do not use in production.
"""
from k2app import k2app

if __name__ == "__main__":
    k2app.debug = True
    k2app.run(port=8042, host='0.0.0.0', processes=3)
