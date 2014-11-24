#!/usr/bin/env python3

import urllib.request, urllib.error
from datetime import datetime, timedelta

_mapping = []

class PCFParser(object):
    def __init__(self):
        self._mapping = []

    def get_mapping(self):
        if self._mapping:
            return self._mapping
        content = None
        out = []
        url = "ftp://webpcode:webpcode@ftp2.itella.com/unzip/Itella_PCF_%s.dat"
        if int(datetime.now().strftime("%Y")) >= 2015:
            url = "ftp://webpcode:webpcode@ftp2.itella.com/unzip/PCF_%s.dat"
        t = datetime.now()
        for i in range(10):
            try:
                r = urllib.request.urlopen(url % t.strftime("%Y%m%d"))
            except urllib.error.URLError:
                t = t - timedelta(seconds=60*60*24)
                continue
            content = r.read()
            break
        if content:
            for line in content.splitlines():
                line = line.decode("iso-8859-1")
                x = {"ponotid": line[0:47].strip(),
                     "type": line[48:77].strip(),
                     "short": line[78:89].strip(),
                     "short_swe": line[90:102].strip(),
                     "region": line[116:145].strip(),
                     "region_swe": line[146:176].strip(),
                     "id": line[176:179].strip(),
                     "name": line[179:199].strip(),
                     "name_swe": line[199:219].strip(),
                     "random_id": line[219:].strip()
                     }
                out.append(x)
        self._mapping = out
        return self._mapping

if __name__ == '__main__':
    import json
    m = PCFParser().get_mapping()
    print(json.dumps(m))
