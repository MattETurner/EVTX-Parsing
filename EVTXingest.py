'''
-----------------------------------------------------------------
| Changelog:
| v1.0 MT / initial version. evtx only for now. uses https://github.com/dgunter/evtxtoelk by Dragos Incident Response Team, this script initially uses this stream parser and recurses through the root folder. When a file is ingested without error, it will be removed from that folder.
|
'''

from evtxtoelk import EvtxToElk
import os
evtxrootdir  = '/logstash/evtx'


for subdir, dirs, files in os.walk(evtxrootdir):
    for file in files:
        fileingest = os.path.join(subdir, file)
        print(f"Ingesting {fileingest}...")
        try:
            EvtxToElk.evtx_to_elk(fileingest,"http://localhost:9200")
            if os.path.exists(fileingest):
                os.remove(fileingest)
                print(f"{fileingest} Removed")
            else:
                print(f"{fileingest} was not found")    
        except:
            print(f"{fileingest} had an error and was NOT ingested.")
            
print("all done!")