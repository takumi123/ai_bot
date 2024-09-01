import json

def lambda_handler(event, context):
    # リクエストボディからメッセージを取得
    message = event.get('message', 'Hello from Lambda!')
    
    # レスポンスを作成
    response = {
        'statusCode': 200,
        'body': json.dumps({'message': f'Echo: {message}'})
    }
    
    return response