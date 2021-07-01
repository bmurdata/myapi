# myapi
This repository holds code current API projects. Once complete, they will be moved over to new repos, branches, or removed altogether.  
My LinkedIn: https://www.linkedin.com/in/brianmurphy94/

## Current Project: NYC Gov Jobs API-Mongo Edition

### Objectives
* Create an API interface for my NYC Goverment Job Scraper, using MongoDB Atlas and Azure.  
* Create Frontend using Flask or C# to display API.

Link to scraper Repo: https://github.com/bmurdata/NYCGovJobSearch  
Link to full Flask Implementation: https://github.com/bmurdata/GovJobSearch_Web

## Progress
* API Functional- returns results from MongoDB as JSON objects to browser.
* Security- Function key level. 
* Frontend intergration in progress.

## Endpoints
https://nycgovjobs.azurewebsites.net/api/byJobCode
https://nycgovjobs.azurewebsites.net/api/jobPost
https://nycgovjobs.azurewebsites.net/api/jobMeta

All three take parameters jnum, where jnum is the jobID. If none is given, all results in collections are returned.
## What I have
GCP Ubuntu virtual machine running Python Flask and Python Selenium to display and update scrape data. MySQL as a database, and cron jobs to run updates twice daily.

**Why change?** Cost- GCP virtual machine is expensive compared to Azure, and I have certifications in Azure.

Python Flask API/Frontend can be replicated using consumption services due to low demand. Scraping updates can be run from local Pi and pushed twice daily.

SQL Server is also expensive as an alternative to MySQL, as well as requiring boot up time to run. MongoDB Atlas Free M0 Cluster is functional, and should the need arise can be ported to Azure CosmosDB free tier.
