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

if perforceServer is None:
   sys.exit(1)

iServer = ServerFactory().getOptionsServer(perforceServer['port'], None)
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

