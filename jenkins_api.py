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
print


#



