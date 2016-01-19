# python-jenkins-nosetests-bootstrap
teaching myself to set up and configure Jenkins for testing python projects, then automating that process


Purpose
-------

* have you ever had to work with folks who commit code without seeing if it compiles it first?
* has someone ever changed a major code API in code you are responsible for without consulting you?
* do you ever anticipate yourself coding in a blaze of glory one night when intexicated?
  * or when having a brilliant idea just before bed?

*I long for the warm and comforting embrace of a robust CICD setup...*
But one that matches my propensity for creating a lot of repos and
seeing which ideas prove fruitful only after letting the code blossom.
My CIDI setup should be:

* super fast to configure and deploy
* simple to understand and maintain
* works on OSX & RHEL
* totally open source, portable, and available to me in secure environments
* strong preference for restricting dependence to strong and active OSS projects


getting started
---------------

Let's find some tutorials and RTFMs to see what's available in python's
open CIDI world:

* the [awesome alex conrad on python testing in Jenkins](http://www.alexconrad.org/2011/10/jenkins-and-python.html?m=1) - thank you sir!
* [some dude at a 2015 Jenkins conference](https://www.cloudbees.com/jenkins/juc-2015/presentations/JUC-2015-Europe-Orchestrating-Your-Bhattacharya.pdf) - neat
* a [Jenkins python directory page](https://wiki.jenkins-ci.org/display/JENKINS/Python+Projects) - partially matches my own reasearch, a good sign
  * this one needs a second look, good links
* [buildbot looks interesting](http://docs.buildbot.net/current/tutorial/firstrun.html)...


install jenkins & install python's plugins
---------------------------------------------

```
$ brew install jenkins
$ open http://localhost:8080/
```

* install the `git` an d`python` plugins for Jenkins by running:

```
$ ./jenkins_api_install_git_and_python_plugins.py
```

Create a Jenkins job and start testing
---------------------------------------

* here's a [super simple project designed for testing demos](https://github.com/devinshields/testable_python_project)

* ??? how to create the config_xml string ???
  * [found out here](https://www.sghill.net/how-do-i-backup-jenkins-jobs.html)


### progress with the API client has slowed down. let's change tack:

* [setup tutorial for humans](http://www.alexconrad.org/2011/10/jenkins-and-python.html?m=1)


Backup and restore a Jenkins Job Configuration
-----------------------------------------------

* https://www.sghill.net/how-do-i-backup-jenkins-jobs.html


-------------------------------------------



redo everything: from scratch, and using only the Jenkins API
-------------------------------------------------------------

a git repo of python and one job_config.xml file should do it:

* create python script that queryies for all Jobs
  * forearch, extract and store a Job pickle, or `job_config.xml` file

* delete the existing Jenkins server
  * purge everything - configs, plugins, everything

* create a vanilla Jenkins server from scratch (w/homebrew?)

* install all plugins

* restore all Jenkins Jobs

* trigger one build for each job

