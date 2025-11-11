
echo "Deploying Flask app..."
export FLASK_APP=app.py
az webapp up --resource-group $RG --sku F1 -n flaskwebapp123456
