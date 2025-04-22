
# AWS Bedrock Claude Model Inference (bedrock-cris)

```markdown
# AWS Bedrock Claude Model Inference

This Python script demonstrates how to interact with Amazon Bedrock to invoke Claude language models using the AWS SDK (boto3).

## Prerequisites

- AWS account with access to Amazon Bedrock
- Appropriate IAM permissions configured
- Python 3.x
- boto3 library installed

## Installation

1. Install the required Python package:
```bash
pip install boto3
```

2. Configure your AWS credentials using one of the following methods:
   - AWS CLI (`aws configure`)
   - Environment variables
   - IAM role (if running on AWS services)

## Configuration

Update the following variables in the script:
- `region`: Your AWS region (default is "us-east-1")
- `model_id`: The ARN of your Bedrock model or inference profile

## Usage

The script demonstrates:
1. Setting up a Bedrock runtime client
2. Preparing a request payload for Claude model
3. Invoking the model with a prompt
4. Handling the response and potential errors

## Code Structure

- Creates Bedrock runtime client
- Defines model ID and prompt
- Prepares request payload with specific Claude format
- Implements error handling for AWS ClientError and general exceptions
- Processes and extracts generated text from response

## Example

```python
prompt = "Explain the benefits of using custom inference profiles in AWS Bedrock."
```

## Response Handling

The script handles different response formats:
- Checks for "content" in response
- Falls back to "completion" if needed
- Falls back to "message.content" if needed
- Uses string representation as final fallback

## Error Handling

The script includes error handling for:
- AWS ClientError exceptions
- General exceptions

## Dependencies

- boto3
- json
- botocore.exceptions

## Security Note

Ensure proper IAM permissions and security best practices are followed when using AWS services.

## License

[Your license information here]
```
