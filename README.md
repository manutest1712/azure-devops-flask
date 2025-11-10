# Overview

This project provides a cloud-hosted Flask web application that predicts housing prices using a trained machine-learning model.  
Users can send property details to the `/predict` API and instantly receive price predictions in JSON format.  
Automation is built in: a Makefile simplifies setup, testing, and deployment.
Continuous Integration runs through GitHub Actions, which installs dependencies, runs pylint for code analysis and pytest to execute unit test cases on every push to the main branch.
Azure Pipelines provides continuous delivery by packaging the application and deploying it directly to an Azure Web App.  
The result is a reliable, scalable, and automated solution that supports rapid development and real-time model inference.

## Project Plan

[Trello board for the Housing Trend Project Planner](https://trello.com/invite/b/690f05db22262841d76ee7eb/ATTIae68ef4c002ae520093e7c908e38d715DBC9BB5E/fask-housing-trend-weekly-plan)

[Project Plan In Excel](https://docs.google.com/spreadsheets/d/1QsJpxNEZldNpzWKBwi_6Fmf42sGRiEYL/edit?usp=sharing&ouid=109875377807326084890&rtpof=true&sd=true)
  https://docs.google.com/spreadsheets/d/1QsJpxNEZldNpzWKBwi_6Fmf42sGRiEYL/edit?usp=sharing&ouid=109875377807326084890&rtpof=true&sd=true

## Instructions

<TODO:  
* Architectural Diagram (Shows how key parts of the system work)>

<TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

* Project running on Azure App Service

* Project cloned into Azure Cloud Shell

* Passing tests that are displayed after running the `make all` command from the `Makefile`

* Output of a test run

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application

> 

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

<TODO: Add link Screencast on YouTube>





# Flask Hello World

Minimal Flask application that returns "Hello, World!" at `/` and a JSON healthcheck at `/health`.


## Requirements
- Python 3.8+ (3.12 works fine)
- make


## Quick start (Unix/macOS)

# clone the repo
git clone <your-repo-url>
cd azure-devops-flask


# Install necessary dependencies
make install


# run the app (development)
make run

# open http://127.0.0.1:5000 in your browser


![alt text](docs/images/Azure_Cloud_Shell_Make_All_Pass.png?raw=true)

