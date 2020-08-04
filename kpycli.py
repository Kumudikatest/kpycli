import boto3
cognito_idp = boto3.client("cognito-idp")
import requests

def handler(event, context):
    try:
        res = requests.get(
            "https://paper-api.alpaca.markets/v2/account",
            params={},
            headers={"Accept":"application/json"}
        )
        # your code goes here
    except BaseException as e:
        # error handling goes here
        raise(e)
        try:
            data = cognito_idp.list_users(
                UserPoolId="us-east-1_HdYJb7Znp",
                Limit=10
            )
        except BaseException as e:
            print(e)
            raise(e)
    
    return {"message": "Successfully executed"}
