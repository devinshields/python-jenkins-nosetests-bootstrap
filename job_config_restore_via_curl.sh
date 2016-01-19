#!/bin/bash
#
#   backup and restore on the raw API:
#           https://www.sghill.net/how-do-i-backup-jenkins-jobs.html
#
#
#   post xml data with curl:
#           http://stackoverflow.com/questions/3007253/send-post-xml-file-using-curl-command-line
#
#   fixing lack of newline chars in posted xml:
#          https://benkiew.wordpress.com/2012/01/12/automating-hudsonjenkins-via-rest-and-curl-a-very-small-cookbook/
#


# ------------ #

# PARAMETER: for a given Jenkins Job...
JOB_BACKUP_NAME='casual-experiment-python-project'

# CONFIGS:
BACKUP_FILE_EXTENSION='.xml'
JOB_CONFIG_BACKUPS_DIR='./z_job_config_backups'

# THE BACKUP FILE
JOB_BACKUP_FILE_PATH="$JOB_CONFIG_BACKUPS_DIR/$JOB_BACKUP_NAME$BACKUP_FILE_EXTENSION"

# ------------ #


# logging
echo -e "\n\nJOB_BACKUP_FILE_PATH: $JOB_BACKUP_FILE_PATH\nJOB_BACKUP_NAME: $JOB_BACKUP_NAME\n\n"



# NOTE:     from what I've seen so far, a Jenkins Job with the right name MUST ALREADY EXIST
#           for Job restoration to work.


# execute the restore
curl -X POST -H "Content-Type: text/xml" --data-binary "@$JOB_BACKUP_FILE_PATH" "http://localhost:8080/job/$JOB_BACKUP_NAME/config.xml"



