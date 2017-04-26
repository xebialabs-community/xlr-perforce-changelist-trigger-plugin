#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import sys
from com.perforce.p4java.server import ServerFactory

if perforceServer is None:
   print "No server provided"
   sys.exit(1)

iServer = ServerFactory().getOptionsServer(perforceServer['url'], None)
iServer.setUserName(perforceServer['username'])
iServer.connect()

if perforceServer['password']:
   iServer.login(perforceServer['password'])


changelists = iServer.getChangelists(1, None, None, None , False, False, False, False)

changelistId = str(0)
for cl in changelists:
  changelistId = str(cl.id)
triggerState = changelistId
