---
layout: post
title: json vs simplejson and Flask
---

We use [Flask](https://flask.palletsprojects.com/en/2.0.x/) as our Python web server framework. Recently, our CI tests started failing with a JSON encoding error. Turns out, one of Flask's dependencies, the [`itsdangerous`](https://itsdangerous.palletsprojects.com/en/2.0.x/) package got recently updated to version 2.0. In the new version, the package [drops support for Python 2](https://itsdangerous.palletsprojects.com/en/2.0.x/changes/#version-2-0-0). For compatibility reasons, `itsdangerous` was using the `simplejson` package for serializing/deserializing JSON data.

After dropping Python 2 support, the new version uses the built-in Python `json` package instead. Importantly, Flask uses `simplejson` as well if it's installed, and falls back to `json` if not. With the new version of `itsdangerous` doing without `simplejson`, Flask will just use the built-in package. 

`simplejson` and `json` have an important difference - `json` doesn't support encoding the `Decimal` type by default (nor `bytes` for example). This is what caused our builds to fail and the rather trivial solution is to add these encoders manually. The confusing part is Flask using `simplejson` simply if it's installed, and `json` otherwise. Discussed [here](https://github.com/pallets/itsdangerous/issues/146) as well.
