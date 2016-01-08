#!/bin/bash

# Script to check orphan workflows in oozie

select app_name,a.status,b.status,count from WF_JOBS a, WF_ACTIONS b where a.id=b.external_id and b.status='RUNNING' and b.external_status='SUSPENDED';
