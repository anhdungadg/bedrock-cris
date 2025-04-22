import boto3
import json
from botocore.exceptions import ClientError

# Set up the AWS Bedrock runtime client
# This assumes you have the appropriate IAM role configured
region = "us-east-1"  # Change to your AWS region
bedrock_runtime = boto3.client("bedrock-runtime", region_name=region)

# Define your inference profile ARN (CRIS-enabled model)
model_id = 'arn:aws:bedrock:us-east-1:123456789012:inference-profile/eu.anthropic-claude-3-5'

# Define your prompt
prompt = "Explain the benefits of using custom inference profiles in AWS Bedrock."

# Prepare request payload for Claude model
# This format is specific to Anthropic Claude models
request_payload = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 1000,
    "messages": [
        {
            "role": "user",
            "content": prompt
        }
    ]
}

try:
    # Invoke the model using the CRIS-enabled inference profile
    response = bedrock_runtime.invoke_model(
        modelId=model_id,
        body=json.dumps(request_payload),
        contentType="application/json",
        accept="application/json"
    )
    
    # Process the response
    response_body = json.loads(response["body"].read())
    
    # Extract the generated text based on Claude model response format
    if "content" in response_body:
        generated_text = response_body["content"]
    elif "completion" in response_body:
        generated_text = response_body["completion"]
    elif "message" in response_body:
        generated_text = response_body["message"]["content"]
    else:
        generated_text = str(response_body)  # Fallback
        
    print("Generated Text:\n", generated_text)
    
except ClientError as e:
    print(f"ClientError: {e.response['Error']['Message']}")
except Exception as e:
    print(f"An error occurred: {e}")

