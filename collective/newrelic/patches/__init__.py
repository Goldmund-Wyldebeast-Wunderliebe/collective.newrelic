__import__('pkg_resources').declare_namespace(__name__)

import newrelic.agent

# This is one is required: it creates the 'webtransaction'
import zpublisher_publish

# Enable/disable as you like

import zpublisher_mapply

import transformchains

import zope_event

import catalog_tool

import talinterpreter

import Globals

try:
    if Globals.DevelopmentMode:
        newrelic.agent.initialize('newrelic.ini', 'development')
    else:
        newrelic.agent.initialize('newrelic.ini', 'staging')
except:
    pass
