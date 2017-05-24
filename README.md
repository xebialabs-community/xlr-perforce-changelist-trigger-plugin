## XL Release Perforce Changelist Trigger plugin ##

## CI status ##

[![Build Status][xlr-perforce-changelist-trigger-plugin-travis-image]][xlr-perforce-changelist-trigger-plugin-travis-url]
[![License: MIT][xlr-perforce-changelist-trigger-plugin-license-image]][xlr-perforce-changelist-trigger-plugin-license-url]
![Github All Releases][xlr-perforce-changelist-trigger-plugin-downloads-image]

[xlr-perforce-changelist-trigger-plugin-travis-image]: https://travis-ci.org/xebialabs-community/xlr-perforce-changelist-trigger-plugin.svg?branch=master
[xlr-perforce-changelist-trigger-plugin-travis-url]: https://travis-ci.org/xebialabs-community/xlr-perforce-changelist-trigger-plugin
[xlr-perforce-changelist-trigger-plugin-license-image]: https://img.shields.io/badge/License-MIT-yellow.svg
[xlr-perforce-changelist-trigger-plugin-license-url]: https://opensource.org/licenses/MIT
[xlr-perforce-changelist-trigger-plugin-downloads-image]: https://img.shields.io/github/downloads/xebialabs-community/xlr-perforce-changelist-trigger-plugin/total.svg


## Overview
- The plugin will repeatedly query a Perforce repository using the latest Java interface JAR file (p4java-2017.1.1508216-bundle.jar the time of development) for the latest changelist applied to the repo.  The polling interval is configurable.          
-  Whenever the plugin detects a change in value of the latest changelist id, it will trigger a release off a template in XL Release.  The changelist id is passed to the release as a variable.

## Change history

- 1.0.2 Original release
- 2.0.0 Rewrite, using Configuration instead of HTTPConnection

## Installation
- Unzip distribution file.
- Copy p4java-2017.1.1508216-bundle.jar to xl-release-server/lib.
- Copy xlr-perforce-changelist-trigger.jar to xl-release-server/plugins.
- Restart XL Release server.

## Configuration

#### Perforce server reference
- Define a reference to your Perforce server on the XL Release configuration panel.

![screenshot of perforce server confg](images/xlr-perforce-changelist-trigger-plugin-config-1.png)

#### Perforce trigger
- Then define a release trigger that references the server. Note that the changelist id is available as a trigger variable. 
- You can filter the changes that trigger the release by a workspace. Map the depot paths you want to watch in a new workspace,
  then configure the release trigger to use that workspace.

![screenshot of perforce trigger config](images/xlr-perforce-changelist-trigger-plugin-config-2.png)

![screenshot of perforce server config](images/xlr-perforce-changelist-trigger-plugin-config-3.png)


 


