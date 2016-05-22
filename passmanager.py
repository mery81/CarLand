#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""CarLand Final Project"""

import hashlib
import picklecache


def getEncPassword(user, raw_password):
    import random
    salt = get_hexdigest('sha1', str(random.random()),
                         str(random.random()))[:5]
    hsh = get_hexdigest('sha1', salt, raw_password)
    password = '%s$%s$%s' % ('sha1', salt, hsh)
    return salt, password


def validPassword(user, raw_password, cache):
    """Returns a boolean of whether the raw_password was correct. Handles
    encryption formats behind the scenes."""
    enc = cache[user]
    salt = enc[0]
    enc_psswrd = enc[1]
    flypsswd = '%s$%s$%s' % ('sha1', salt, get_hexdigest('sha1',
                                                         salt, raw_password))
    #print("stored pass = {0} calc pass = {1}".format(enc_psswrd, flypsswd))
    return flypsswd == enc_psswrd


def get_hexdigest(algo, salt, raw_password):
    return hashlib.sha1(salt + raw_password).hexdigest()
