# README.md

# Creating the Runtime
```
pip install --target package/python -r requirements.txt
cd package/python
zip -r9 ${OLDPWD}/function.zip .
cd -
zip -g function.zip lambda_function.py
```

# Submitting the Lambda
aws lambda update-function-code --function-name lambda-tracing-test --zip-file fileb://function.zip
```

# Invoking the Lambda function
```
aws lambda invoke --function-name lambda-tracing-test --invocation-type RequestResponse
```