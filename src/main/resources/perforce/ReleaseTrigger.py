#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import sys
from com.perforce.p4java.server import ServerFactory
from com.perforce.p4java.option.server import GetChangelistsOptions
from com.perforce.p4java.core import IChangelist
from com.perforce.p4java.core.file import FileSpecBuilder
from com.perforce.p4java import PropertyDefs
from java.lang import System

if perforceServer is None:
    print "No server provided"
    sys.exit(1)

props = System.getProperties()
props.put(PropertyDefs.PROG_NAME_KEY, "P4-XL_Release")
props.put(PropertyDefs.PROG_VERSION_KEY, "2.0.0")

iServer = ServerFactory().getOptionsServer(perforceServer['port'], props)
iServer.setUserName(perforceServer['username'])
iServer.connect()

if perforceServer['password']:
   iServer.login(perforceServer['password'])

opts = GetChangelistsOptions()
opts.setMaxMostRecent(1)
opts.setType(IChangelist.Type.SUBMITTED)

filespec = None
if workspace:
    client = iServer.getClient(workspace)
    iServer.setCurrentClient(client)
    filespec = FileSpecBuilder.makeFileSpecList("//"+workspace+"/...")

changelists = iServer.getChangelists(filespec, opts)

iServer.disconnect()

changelistId = str(0)
for cl in changelists:
  changelistId = str(cl.id)

triggerState = changelistId

