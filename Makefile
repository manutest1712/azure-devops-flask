RG=AzureDevops
PLAN=plan-flask-demo
APP=my-flask-app-$(shell date +%s)
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
	az webapp up --name $(APP) --resource-group $(RG) --runtime "PYTHON:$(PYTHON_VERSION)"
