# -*- coding: utf-8 -*-
#------------------------------------------------------------------------
#
#      /$$$$$$  /$$
#     /$$__  $$| $$
#    | $$  \__/| $$  /$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$
#    | $$      | $$ /$$__  $$ |____  $$| $$__  $$ /$$__  $$ /$$__  $$
#    | $$      | $$| $$$$$$$$  /$$$$$$$| $$  \ $$| $$$$$$$$| $$  \__/
#    | $$    $$| $$| $$_____/ /$$__  $$| $$  | $$| $$_____/| $$
#    |  $$$$$$/| $$|  $$$$$$$|  $$$$$$$| $$  | $$|  $$$$$$$| $$
#     \______/ |__/ \_______/ \_______/|__/  |__/ \_______/|__/
#
#     cleaner.py
#     This is the main python file for sending a request to the
#     server for cleaning unused files.
#
#   Poster   http://pypi.python.org/pypi/poster/
#
#------------------------------------------------------------------------


# Imports
#------------------------------------------------------------------------
import config, poster, socket, urllib2


# Functions
#------------------------------------------------------------------------
def clean():
    try:
        opener = poster.streaminghttp.register_openers()
        params = { 'u': config.CLEAN_U, 'p': config.CLEAN_P }
        datagen, headers = poster.encode.multipart_encode(params)
        response = opener.open( urllib2.Request( config.CLEAN_URL, datagen, headers ), timeout=config.CLEAN_TIMEOUT )
        #response.read()
    except socket.timeout:
        print "Timed out. Trying again..."
        clean()
    except:
        print "There was an error. Shutting down..."


# Main
#------------------------------------------------------------------------
if __name__=="__main__":
    try:
        print "Cleaning unused files"
        clean()
        print "Cleaning complete"

    except:
        print ""
        print "To use: python clean.py"
        print ""