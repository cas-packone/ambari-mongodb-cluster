#coding=utf-8
import sys, os, pwd, grp, signal, time,logging
from time import sleep
import resource_management
from subprocess import call
from resource_management import *

class MMSServer(Script):

    def install(self,env):
        import params

        try:
            Execute('echo "MMS Server Istall beging" ')
            Execute('yes | yum install mongodb-mms')
            sleep(5)
            self.configure(env)
        except Exception, e:
            print Exception, ":", e
            Execute('echo "MMS Server Install error" ')



    def configure(self,env):
        import params
        env.set_params(params)

        mms_configdir = params.mms_configdir
        mms_conf_prop_path = mms_configdir + '/conf-mms.properties'
        File(mms_conf_prop_path,
             content=Template("conf-mms.properties.j2"),
             )

        mms_conf = mms_configdir + '/mms.conf'
        File(mms_conf, content=Template("mms.conf.j2"))

    def start(self,env):
        self.configure(env)
        Execute(" service mongodb-mms start")

    def stop(self,env):
        Execute(" service mongodb-mms stop")

    def restart(self, env):
       self.stop(env)
       self.configure()
       self.start(env)

    def status(self,env):
        #Execute(" service mongodb-mms status")
        pid_file = "/opt/mongodb/mms/tmp/mms-0.pid"
        check_process_status(pid_file)



if __name__ == "__main__":
    MMSServer().execute()