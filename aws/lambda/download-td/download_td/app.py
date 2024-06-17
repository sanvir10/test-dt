import json
import logging
from util import Util

logger = logging.getLogger(__name__)

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    msg=""
    try:
        util = Util()
        util.download("https://drive.google.com/file/d/1aNAL2jravbMF3BS6GP4G1C-5ONrKHLWG/view?usp=sharing")
        util.uploadFileS3("demo-i")
        msg = "File downloaded to S3 Successfully"
    except Exception as e:
        msg = "Exception Downloding/Uploadding file"
        logger.error(f"msg: {e}")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": msg,
        }),
    }
