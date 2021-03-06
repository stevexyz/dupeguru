# Created By: Virgil Dupras
# Created On: 2006/03/03
# Copyright 2013 Hardcoded Software (http://www.hardcoded.net)
# 
# This software is licensed under the "BSD" License as described in the "LICENSE" file, 
# which should be included with this package. The terms are also available at 
# http://www.hardcoded.net/licenses/bsd_license

from core.scanner import Scanner as ScannerBase

class ScannerME(ScannerBase):
    @staticmethod
    def _key_func(dupe):
        return (-dupe.bitrate, -dupe.size)
    
