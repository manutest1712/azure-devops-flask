
echo "Deploying Flask app..."
export FLASK_APP=app.py
az webapp up --resource-group AzureDevops --sku F1 -n flaskwebapp123456
