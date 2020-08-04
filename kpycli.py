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
    
    return {"message": "Successfully executed"}
