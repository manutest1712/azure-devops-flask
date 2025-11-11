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

### Execute the Unit Tests from Cloud Shell
You can run the unit test cases directly from Azure Cloud Shell using:

```bash
make all
```

#### Screenshot
Below is an example of a successful test run:

![alt text](docs/images/Azure_Cloud_Shell_Make_All_Pass.png?raw=true)

### Run the Application from Azure Cloud Shell

#### 1. Deploy and Run the Web Application
You can deploy and start the Flask application directly from Azure Cloud Shell using:

```bash
make app-run
```
This command deploys the application to Azure App Service using the name flaskwebapp123456
If an app with the same name already exists, it will automatically be deleted before redeployment
After deployment, you will see a URL similar to:

  https://flaskwebapp123456.azurewebsites.net

Open this link in your browser to view the running Flask application.

#### 2. View the Application in Azure Portal
To verify deployment or manage the web app:

1. Log in to https://portal.azure.com
2. Search for **App Services** in the search bar
3. Click **App Services**
4. Locate the application named **flaskwebapp123456**
5. Click the name to open the app dashboard
6. Click Browse to open the URL directly from the portal

##### Screenshot
Below is an example of a successful deployment output in cloudshell:

![alt text](docs/images/Azure_Cloud_Shell_App_Deployment.png?raw=true)

#### 3. Test the Prediction API Using POST
To test the /predict endpoint, run:
```bash
make web-app-run-post
```
This executes the script:

```bash
#!/usr/bin/env bash
curl -d '{
   "CHAS":{"0":0},
   "RM":{"0":6.575},
   "TAX":{"0":296.0},
   "PTRATIO":{"0":15.3},
   "B":{"0":396.9},
   "LSTAT":{"0":4.98}
}' \
-H "Content-Type: application/json" \
-X POST https://flaskwebapp123456.azurewebsites.net/predict
```

Sample output:
```bash
{"prediction":[20.35373177134412]}
```

##### Screenshot
Below is an example of a successful post command output in cloudshell:

![alt text](docs/images/Azure_Cloud_Shell_App_Post.png?raw=true)

#### 3. Check the log files

##### From cloud shell
Run the following command to stream logs from your deployed Flask application:

```bash
az webapp log tail --resource-group AzureDevops --name flaskwebapp123456
```
This displays real-time application output such as prints, logging statements, and errors.

##### Using Azure Portal – Log Stream

1. Log in to the **Azure Portal**
2. Go to **App Services**
3. Select your Flask application
4. On the left menu → Click **Log Stream**

This shows live application logs directly inside the Azure Portal.

##### Screenshot
Below is an example showing application logs after executing a POST request (visible both in Cloud Shell and Log Stream):
![alt text](docs/images/Azure_Cloud_Shell_App_Run.png?raw=true)

## CI CD Badges and Pipeline Status

### GitHub Actions – CI Build Workflow
This repository includes a GitHub Actions workflow that builds and validates the application on every commit or pull request.

##### Screenshots
List of CI pipeline runs
![alt text](docs/images/Github_Badge_List.png?raw=true)

Example of a successful CI pipeline execution
![alt text](docs/images/Github_Actions_Badge.png?raw=true)

### Azure Pipelines – Build & Deployment Workflow
Azure DevOps pipeline handles continuous deployment by packaging the app and publishing to Azure Web App.

##### Screenshot
List of CD pipeline executions
![alt text](docs/images/Azure_Pipeline_Badge_List.png?raw=true)

### Application Deployment History
Azure Web App keeps a full deployment history showing when each deployment happened and whether it was successful.

##### Screenshot
Deployment history from Azure Web App Activity Log
![alt text](docs/images/Azure_App_Activity_Log.png?raw=true)

## Enhancements

### 1. Working GitHub Actions YAML

A corrected workflow is required because current dependency versions cause build failures.
The updated YAML should:
  1. Create virtual environment
  2. Install compatible packages
  3. Run tests with pytest


### 2. Working Azure DevOps Pipeline YAML

The existing pipeline deploys successfully, but the app does not start on Azure Web App due to package and startup issues.
The revised YAML must:

1. Install compatible dependencies
2. Deploy to Linux Web App
3. Install packagaes and start the app with Gunicorn 
  startUpCommand: 'pip install -r requirements.txt && gunicorn --bind 0.0.0.0:8000 app:app'

## Demo 
A full walkthrough of the project — including application deployment, CI and CD pipelines — is available on YouTube.

[![Watch the demo](https://img.youtube.com/vi/-CAc0OwIkv4/0.jpg)](https://www.youtube.com/watch?v=-CAc0OwIkv4)


