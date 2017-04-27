#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import sys
from com.perforce.p4java.server import ServerFactory
from com.perforce.p4java.option.server import GetChangelistsOptions
from com.perforce.p4java.core import IChangelist

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

if workspace:
    opts.setClientName(workspace)

changelists = iServer.getChangelists(None, opts)

iServer.disconnect()

changelistId = str(0)
for cl in changelists:
  changelistId = str(cl.id)
  with open('/tmp/trigger.out', 'w+') as f:
      f.write("Latest change : {}\n".format(changelistId))

triggerState = changelistId

