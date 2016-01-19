#!/usr/bin/env python
'''
'''


import os

from jenkinsapi.jenkins import Jenkins


# configs
jenkins_web_interface_url = 'http://localhost:8080'

JENKINS_USER = os.environ['JENKINS_USER']
JENKINS_PASSWORD = os.environ['JENKINS_PASSWORD']


def get_jenkins_instance():
    return Jenkins(jenkins_web_interface_url, username=JENKINS_USER, password=JENKINS_PASSWORD)


def dump_all_jobs():
    jk = get_jenkins_instance()

    # post a full list of jenkins jobs
    for job in jk.get_jobs():
        print job


def main():
    dump_all_jobs()


if __name__ == '__main__':
    main()

