#!/usr/bin/env python

"""
Utility script used to examine the python webbrowser module with different OSs.
"""

import os

os.environ['BROWSER'] = 'firefox'

# If we want to override the $BROWSER variable that the python webbrowser
# references, it needs to be done before the webbrowser module is imported
# for the first time.
TUIR_BROWSER, BROWSER = os.environ.get('TUIR_BROWSER'), os.environ.get('BROWSER')
if TUIR_BROWSER:
    os.environ['BROWSER'] = TUIR_BROWSER

print('TUIR_BROWSER=%s' % TUIR_BROWSER)
print('BROWSER=%s' % BROWSER)

import webbrowser

print('webbrowser._browsers:')
for key, val in webbrowser._browsers.items():
    print('  %s: %s' % (key, val))

print('webbrowser._tryorder:')
for name in webbrowser._tryorder:
    print('  %s' % name)

webbrowser.open_new_tab('https://www.python.org')
