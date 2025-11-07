RG=AzureDevops
PLAN=plan-flask-demo
APP=flaskwebapp
PYTHON_VERSION=3.10

install:
	pip install --user -r requirements.txt
lint:
	echo "to be done"
test:
	echo "to be done"
create-plan:
	az appservice plan create --name $(PLAN) --resource-group $(RG) --sku B1 --is-linux

create-app:
	az webapp create --resource-group $(RG) --plan $(PLAN) --name $(APP) --runtime "PYTHON:$(PYTHON_VERSION)"
	az webapp config set --resource-group $(RG) --name $(APP) --startup-file "python app.py"
app-run:
	@echo "Checking if webapp exists..."
	@az webapp show --name helloflask --resource-group $(RG) >/dev/null 2>&1 && \
		echo "Deleting existing webapp helloflask..." && \
		az webapp delete --name flaskwebapp --resource-group $(RG) || \
		echo "No existing app found."

	@echo "Setting Flask startup file and deploying..."
	export FLASK_APP=app.py
	az webapp up --resource-group $(RG) --sku F1 -n flaskwebapp
