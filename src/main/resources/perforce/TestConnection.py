#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

# include P4API
# extract parameters
# connect to server
# run p4.info

import sys
from com.perforce.p4java.server import ServerFactory

if configuration is None:
   sys.exit(1)

iServer = ServerFactory().getOptionsServer(configuration['port'], None)
iServer.setUserName(configuration['username'])
iServer.connect()

if configuration['password']:
    iServer.login(configuration['password'])

serverInfo = iServer.getServerInfo()

iServer.disconnect()
