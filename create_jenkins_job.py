#!/usr/bin/env python
'''

create Jobs with the API:

    https://gist.github.com/stuart-warren/7786892

'''


import os

from jenkinsapi.jenkins import Jenkins


# configs
JENKINS_USER = os.environ['JENKINS_USER']
JENKINS_PASSWORD = os.environ['JENKINS_PASSWORD']


def get_jenkins_instance():
    jenkins_web_interface_url = 'http://localhost:8080'
    return Jenkins(jenkins_web_interface_url, username=JENKINS_USER, password=JENKINS_PASSWORD)


def dump_all_jobs():
    # get API client
    jk = get_jenkins_instance()

    # post a full list of jenkins jobs
    print '\njenkins jobs listing:'
    for job in jk.get_jobs():
        print '\tjob: {}'.format(job)
    print


def main():
    dump_all_jobs()

if __name__ == '__main__':
    main()

