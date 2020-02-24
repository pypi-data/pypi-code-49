from vtg.client import UserClient

client = UserClient("https://trolltunga.distributedlearning.ai", 443, "")

client.authenticate("predict", "predict")

client.setup_encryption("", True)

client.set_collaboration_id(4)

client.set_task_image("harbor.distributedlearning.ai/models/breast-cancer-predict")

f = open("/home/palga/repositories/prediction_pipeline/input/model_input.csv")
input_ = f.read()

output = client.run_image(bytes(input_,"utf-8"))

print(output)
