#!/usr/bin/env python
'''
https://www.cloudbees.com/jenkins/juc-2015/presentations/JUC-2015-Europe-Orchestrating-Your-Bhattacharya.pdf


working with plugins
      https://python-jenkins.readthedocs.org/en/latest/examples.html#example-4-working-with-jenkins-plugins

dir(jk) showed 6 plugin related functions:
      * get_plugins
      * get_plugins_url
      * has_plugin
      * install_plugin
      * install_plugins


you can safely power-cycle the Jenkins server:
      http://stackoverflow.com/questions/8072700/how-to-restart-jenkins-manually      
'''


import os

from jenkinsapi.jenkins import Jenkins


# configs
JENKINS_USER = os.environ['JENKINS_USER']
JENKINS_PASSWORD = os.environ['JENKINS_PASSWORD']


def get_jenkins_instance():
    jenkins_web_interface_url = 'http://localhost:8080'
    return Jenkins(jenkins_web_interface_url, username=JENKINS_USER, password=JENKINS_PASSWORD)


def dump_jenkins_jobs():
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


def dump_plugin_info():
    # dump the installed plugins list
    print 'installed plugins:'
    print '\njk.get_plugins(): {}\n'.format(jk.get_plugins())


def install_python_cicd_plugins():
    # get an api client
    jk = get_jenkins_instance()

    # plugin requirements
    CICD_plugins = ['git@2.4.1', 'python@1.3', 'cobertura@1.9.7', 'violations@0.7.11']

    for plugin in CICD_plugins:
        response = jk.install_plugin(plugin)
        print 'plugin: {}, response: {}'.format(plugin, response)

install_python_cicd_plugins()

