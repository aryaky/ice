# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

import os, sys, traceback, time
import Ice, Test, TestAMDI


class TestActivationAMDI(Test.TestActivation):

    def activateServantLocator(self, activate, current=None):
        if(activate):
            current.adapter.addServantLocator(TestAMDI.ServantLocatorI(""), "")
            current.adapter.addServantLocator(TestAMDI.ServantLocatorI("category"), "category")
        else:
            current.adapter.removeServantLocator("")
            current.adapter.removeServantLocator("category")

