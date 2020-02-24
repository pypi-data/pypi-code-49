from autosolveclient.autosolve import AutoSolve


def receiver_function(json_message):
    print("Task ID :: " + json_message['taskId'])
    print("Site Key :: " + json_message['siteKey'])
    print("Token :: " + json_message['token'])
    print("Created At :: " + json_message['createdAt'])
    print("Version :: " + json_message['version'])
    print("Action :: " + json_message['action'])


auto_solve = AutoSolve(
    access_token="30144-4a843021-bb26-4a13-b442-f7ce4824da14",
    api_key="2164d024-51a9-4401-a8f6-23a08e46d314",
    client_key="test",
    receiver_function=receiver_function,
    debug=True)

finished = auto_solve.initialized()
