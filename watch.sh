#!/usr/bin/env bash
when-changed templates/index.html posts/ build.py about.md  -c python build.py