# PPWGEN: a simple web-based AWS application written in Python using Flask 
# Generates a simple 15-digit password that contains at least 3 lowercase letters, at least 3 uppercase letters, at least 3 numbers, and one or two dashes (-) when a button is pushed.

import random
import string
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
  password = generate_password()
  return render_template("index.html", password=password)

def generate_password():
  """Generates a 15-digit password that contains at least 3 lowercase letters, at least 3 uppercase letters, at least 3 numbers, and one or two dashes (-)."""
  password = ""
  for i in range(15):
    char = random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + "-")
    if char.islower():
      password += char
    elif char.isupper():
      password += char
    elif char.isdigit():
      password += char
    else:
      if len(password) < 13:
        password += char
  return password

if __name__ == "__main__":
  app.run(debug=True)

# This code first imports the random and string modules. The random module is used to generate random numbers and characters, while the string module is used to get a list of all lowercase letters, uppercase letters, and digits.
# Next, the Flask module is imported. Flask is a microframework that makes it easy to create web applications in Python.
# The app variable is then created and initialized with the Flask object.
# The index() function is then defined. This function is the main function of the application. It generates a random password and then renders the index.html template with the password as a parameter.
# The generate_password() function is then defined. This function generates a random password that contains at least 3 lowercase letters, at least 3 uppercase letters, at least 3 numbers, and one or two dashes (-).
#The if __name__ == "__main__": block then starts the application.
# To run the application, you can save the code as password_generator.py and then run the following command in the command line:
# python password_generator.py

# 1. Create an AWS Lambda function.
# 2. Upload the app.py file to the Lambda function.
# 3. Configure the Lambda function to run when a HTTP request is received.
# 4. Create an API Gateway endpoint for the Lambda function.
# 5. Test the API Gateway endpoint.

# Here are the detailed steps:
# Go to the AWS Lambda console.
# Click the "Create function" button.
# Select the "Python 3.8" runtime.
# Give the function a name, such as "password_generator".
# Select the "Author from scratch" option.
# Paste the code from the password_generator.py file into the function code editor.
# Click the "Save" button.
# Go to the "Configuration" tab for the Lambda function.
# In the "Trigger" section, select the "HTTP" trigger.
# In the "Method" section, select "POST".
# Click the "Save" button.
# Go to the API Gateway console.
# Click the "Create API" button.
# Select the "REST API" option.
# Give the API a name, such as "password_generator_api".
# Click the "Create" button.
# In the "Actions" menu, select "Create Resource".
# Give the resource a name, such as "/password".
# Click the "Create" button.
# In the "Actions" menu, select "Enable CORS".
# In the "CORS" section, select the "Enable CORS for all origins" option.
# Click the "Save" button.
# In the "Method" section, select the "POST" method.
# In the "Integration" section, select the "Lambda" integration.
# In the "Lambda Function" field, select the "password_generator" function.
# Click the "Save" button.
# Test the API Gateway endpoint by sending a POST request to the following URL:
# https://<API_ID>.execute-api.us-east-1.amazonaws.com/password
# The response body will contain the generated password.





# Here are the steps on how to run the application in AWS:

# Create an AWS Lambda function.
# Upload the password_generator.py file to the Lambda function.
# Configure the Lambda function to run when a HTTP request is received.
# Create an API Gateway endpoint for the Lambda function.
# Test the API Gateway endpoint.
# Here are the detailed steps:

# Go to the AWS Lambda console.

# Click the "Create function" button.

# Select the "Python 3.8" runtime.

# Give the function a name, such as "password_generator".

# Select the "Author from scratch" option.

# Paste the code from the password_generator.py file into the function code editor.

# Click the "Save" button.

# Go to the "Configuration" tab for the Lambda function.

# In the "Trigger" section, select the "HTTP" trigger.

# In the "Method" section, select "POST".

# Click the "Save" button.

# Go to the API Gateway console.

# Click the "Create API" button.

# Select the "REST API" option.

# Give the API a name, such as "password_generator_api".

# Click the "Create" button.

# In the "Actions" menu, select "Create Resource".

# Give the resource a name, such as "/password".

# Click the "Create" button.

# In the "Actions" menu, select "Enable CORS".

# In the "CORS" section, select the "Enable CORS for all origins" option.

# Click the "Save" button.

# In the "Method" section, select the "POST" method.

# In the "Integration" section, select the "Lambda" integration.

# In the "Lambda Function" field, select the "password_generator" function.

# Click the "Save" button.

# Test the API Gateway endpoint by sending a POST request to the following URL:

# Code snippet
# https://<API_ID>.execute-api.us-east-1.amazonaws.com/password
# Use code with caution. Learn more
# The response body will contain the generated password.