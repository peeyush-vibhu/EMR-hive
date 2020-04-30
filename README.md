## BIGDATA-EMR-JOB-CLUSTER-CICD

## General Info
BIGDATA-EMR-JOB-CLUSTER-CICD is used to deploy EMR Transient cluster with respect to Hive/Spark/ Sparkfleet. Users can pass the paramters from Ansible tower as per their needs and launch an EMR Job Cluster.As this is a transient cluster, Cluster will be terminated when the Job is finished. 

## Technologies
* Ansible
* Ansible Tower
* CICD
* CF Templates
* EMR
* Gitlab
* Jenkins
* Python
* s3

## Environments
* STAGING
* HIVE
* SPARK

## Need for CICD
There are various advantages of using CICD pipeline like ease of handling codes, Keeping track of changes(who and when the changes are performed), changing the versioning of the code as per the need etc.

## Setup
EMR is launched from Ansible Tower passing the customized paramters. 

## Generic overview of the flow of the pipeline
* Jenkinsfile( written in Groovy format):It is passed in Jenkins pipeline. It contains the flow of CICD pipeline (order of execution of the script).
* Site.yml: Various stages in Jenkins file calls site.yml file which corresponds to specific roles like prepare, validate,deploy and delete the CF template.
* Inventory: Defines the inventory for the script. Here we are using locally wrt branches.
* ansible.cfg: It holds the ansible configuration. Inventory will be checked locally here.
* .gitignore: use to exclude files with particular extension while running the code.
* groupvars: holds the common variable required in script.
* roles: Roles folder is for the execution of the specific task. This is called from site.yml file.
* cf_templates: It holds the code written in YAML format.Here we are using three independent code: Hive, Spark and Sparkfleet and providing it as a package to end-user to select the script as per their preference.

## Usage
This pipeline is use launch EMR Transient cluster wrt to Hive/Spark or Sparkfleet.

## Reference Documents link:
Please refer the below documents to understand how to launch an EMR job cluster from an ansible tower and to know more about parameters. 
https://pgone.sharepoint.com/:x:/r/sites/bigdataanalytics/_layouts/15/Doc.aspx?sourcedoc=%7B5BC25506-9CEE-4204-BE12-DF157F274E70%7D&file=EMR_Job_Cluster_Parameters_Mastersheet.xlsx&action=default&mobileredirect=true 

https://pgone.sharepoint.com/:w:/r/sites/bigdataanalytics/_layouts/15/Doc.aspx?sourcedoc=%7B1353786B-FEFD-47A9-B445-AFC304780FFA%7D&file=EMR_Job_Cluster_Ansible_Tower_job_aid.docx&action=default&mobileredirect=true 
