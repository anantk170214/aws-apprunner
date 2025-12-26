
# Health
curl -s http://localhost:8080/health

# Query by PK only
curl -s "http://localhost:8080/items?pk=USER#123"



CDK
AppRunner Stack is setup with NGINX initially. 

✅ How You Switch to Private ECR Later (No Surprises)
1️⃣ Change image config:

"imageIdentifier": f"{ecr_repo.repository_uri}:latest",
"imageRepositoryType": "ECR",
"imageConfiguration": {
    "port": "8080"
}


2️⃣ Add authenticationConfiguration back:

"authenticationConfiguration": {
    "accessRoleArn": service_role.role_arn
}

3️⃣ Deploy:
cdk deploy AppRunnerStack
