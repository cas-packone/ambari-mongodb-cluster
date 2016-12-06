#coding=utf-8
import sys, os, pwd, grp, signal, time,logging
from time import sleep
import resource_management
from subprocess import call
from resource_management import *

class MMSAgent(Script):
    mongo_packages = ['mongodb-mms-automation-agent-manager']
    def install(self,env):
        import params
        env.set_params(params)
        self.installMongo(env)


    def configure(self,env):
        import params
        env.set_params(params)
        File('/etc/mongodb-mms/automation-agent.config', content=Template("automation-agent.config.j2"))


    def start(self,env):
        self.configure(env)
        Execute(" service mongodb-mms-automation-agent start") # , ignore_failures=True

    def stop(self,env):
        Execute(" service mongodb-mms-automation-agent stop") # , ignore_failures=True

    def restart(self, env):
        self.configure(env)
        Execute(" service mongodb-mms-automation-agent restart") # , ignore_failures=True

    def status(self,env):
        Execute(" service mongodb-mms-automation-agent status") # ,ignore_failures=True



if __name__ == "__main__":
    MMSAgent().execute()