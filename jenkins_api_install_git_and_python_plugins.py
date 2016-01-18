#!/usr/bin/env python
'''
https://www.cloudbees.com/jenkins/juc-2015/presentations/JUC-2015-Europe-Orchestrating-Your-Bhattacharya.pdf
'''



from jenkinsapi.jenkins import Jenkins


def get_jenkins_instance():
    jenkins_web_interface_url = 'http://localhost:8080'
    return Jenkins(jenkins_web_interface_url)



# first thing: create a new Jenkins Job by poking things at the jenkins_web_interface_url


# create an api client
jk = get_jenkins_instance()


# get a list of job titles?
print '\njk: {}'.format(jk)
print '\tjk.keys(): {}\n'.format(jk.keys())


# post a full list of jenkins jobs
print 'jenkins jobs listing:'
for job in jk.get_jobs():
    print '\tjob: {}'.format(job)


# look at some jenkins internals - and install the git & python nosetest plugins while we're at it
#      https://python-jenkins.readthedocs.org/en/latest/api.html#jenkins.Jenkins.get_version


# inspect my installed jenkins, and dump the properties on my API client
print '\njk.version: {}'.format(jk.version)
for prop in dir(jk):
    print '\t\t', prop


# working with plugins
#       https://python-jenkins.readthedocs.org/en/latest/examples.html#example-4-working-with-jenkins-plugins
#
# dir(jk) showed 6 plugin related functions:
#       * get_plugins
#       * get_plugins_url
#       * has_plugin
#       * install_plugin
#       * install_plugins
#


# dump the installed plugins list
print 'installed plugins:'
print '\njk.get_plugins(): {}\n'.format(jk.get_plugins())



# try installing the git and python plugins via the API
install_git_plugin_response = jk.install_plugin('git@2.4.1')
print '\ninstall_git_plugin_response: {}\n'.format(install_git_plugin_response)

install_python_plugin_response = jk.install_plugin('python@1.3')
print '\ninstall_python_plugin_response: {}\n'.format(install_python_plugin_response)



# it worked! takes a while for Jenkins to download and install those buggers...
print 'installed plugins:'
print '\njk.get_plugins(): {}\n'.format(jk.get_plugins())



# you can safely power-cycle the Jenkins server:
#       http://stackoverflow.com/questions/8072700/how-to-restart-jenkins-manually



