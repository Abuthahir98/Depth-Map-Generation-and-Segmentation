# depthmap.py
from gradio_client import Client, handle_file

# Initialize the client with the endpoint
client = Client("depth-anything/Depth-Anything-V2")

# Use the client to predict the depth map
result = client.predict(
    image=handle_file('https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png'),
    api_name="/on_submit"
)

# Print the result
print(result)