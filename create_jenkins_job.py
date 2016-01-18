#!/usr/bin/env python
'''  '''


import os

from jenkinsapi.jenkins import Jenkins


# I enabled security... grab credentials from the environment:
JENKINS_USER = os.environ['JENKINS_USER']
JENKINS_PASSWORD = os.environ['JENKINS_PASSWORD']


def get_jenkins_instance():
    jenkins_web_interface_url = 'http://localhost:8080'
    return Jenkins(jenkins_web_interface_url, username=JENKINS_USER, password=JENKINS_PASSWORD)


# get an API client
jk = get_jenkins_instance()


# post a full list of jenkins jobs
print '\njenkins jobs listing:'
for job in jk.get_jobs():
    print '\tjob: {}'.format(job)
print


# create jobs via the raw HTTP API:
#       https://gist.github.com/stuart-warren/7786892


