#!/bin/bash
#
#   https://www.sghill.net/how-do-i-backup-jenkins-jobs.html
#


# ------------ #


# PARAMETER: for a given Jenkins Job...
JOB_IN_JENKINS='RunNosetTestsJob'


# CONFIGS:
JOB_CONFIG_BACKUPS_DIR='./z_job_config_backups'


# OUTPUTS:
OUTPUT_FILE="$JOB_CONFIG_BACKUPS_DIR/$JOB_IN_JENKINS.xml"


# ------------ #



# make the dir if it doesn't exist
mkdir -p $JOB_CONFIG_BACKUPS_DIR



# request this job's config from Jenkins
echo -e "backing up Job: $JOB_IN_JENKINS"
curl -s "http://localhost:8080/job/$JOB_IN_JENKINS/config.xml" > $OUTPUT_FILE




