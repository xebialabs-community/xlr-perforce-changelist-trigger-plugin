#
# Copyright 2017 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
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

