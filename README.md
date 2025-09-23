# AT-MassDataPull
Scripts/processes to collect data from multiple vendors

Included is a ".source [sample]" folder, this includes the needed .env file and distributions.txt referenced in the scripts. Rename this folder to just ".source" and edit the keys in the .env file to include any keys you are using

======== SYNOPSIS =========
       Automated collection script for managed portals.

======= DESCRIPTION =======
       Calls to various API endpoints and pulls information on devices, accounts, config,
       specs, etc. and consolidates it into a .csv file.

       Then, it prepares and sends an email through SMTP to any emails
       present in .\source\distribution.txt

========= AUTHOR =========
       Arrow Team | Brendon Mourao

========== NOTES ==========

