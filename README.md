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

## Instructions

### Architecture Diagram

  ![Architecture](docs/images/Architecture.png?raw=true)

### Clone Project in Azur Cloud Shell (SSH) — Step-by-step Guide

#### 1. Open Azure Cloud Shell (Bash)
  1. Open https://shell.azure.com/ in your browser (or open Cloud Shell from the Azure Portal via the top-right Cloud Shell icon).
  2. Make sure Bash is selected (not PowerShell).

#### 2. Generate an SSH keypair
Run the following command in Azure Cloud Shell:

```bash
ssh-keygen -t rsa
```
- When prompted for file in which to save the key, press Enter to accept the default (usually `/home/<username>/.ssh/id_rsa`).
- When prompted for a passphrase, press Enter to use no passphrase.

#### 3. Copy the public key
Print the public key so you can copy it to GitHub:

```bash
cat ~/.ssh/id_rsa.pub
```

Copy the entire output (one long line starting with `ssh-rsa`).

#### 4. Add the SSH public key to GitHub

1. Open GitHub in your browser and sign in: https://github.com/
2. Click your profile picture (top-right) → **Settings**.
3. In the left-hand menu click **SSH and GPG keys**.
4. Click **New SSH key** (or **Add SSH key**).
5. In **Title** enter a friendly name like `Azure Cloud Shell - <date>`.
6. Paste the contents of `~/.ssh/id_rsa.pub` into the **Key** field.
7. Click **Add SSH key**. You may be asked to confirm your GitHub password or 2FA if enabled.


#### 5. Clone the repository (SSH)
Now clone the repository using the SSH URL: git@github.com:manutest1712/azure-devops-flask.git

```bash
git clone git@github.com:manutest1712/azure-devops-flask.git
```

This will create a new directory `azure-devops-flask` in your Cloud Shell home directory. Change into the directory and list files:

```bash
cd azure-devops-flask
dir
```
#### Screenshot
![alt text](docs/images/Azure_Cloud_Shell_Project_Clone.png?raw=true)

### Exute the unit tests from cloud shell

```bash
make all
```

#### Screenshot
![alt text](docs/images/Azure_Cloud_Shell_Make_All_Pass.png?raw=true)

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

