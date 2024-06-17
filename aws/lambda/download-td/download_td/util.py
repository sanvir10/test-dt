import boto3
import logging
import requests

logger = logging.getLogger(__name__)

class Util:
    def __init__(self):
        self.gsFilename=""
        
    def download(self, url):
        self.validateUrl(url)
        self.downloadGSFile(url)
        
    def validateUrl(self, url):
        url_lower = url.lower()

        # TODO
        # Add a service to validate if Google GS URL Is correct or incorrect

        # For now we only have basic validations
        mandatoryTokens = {"drive.google.com"}   # Here we can add more tokens to review        
        urlTokens = url_lower.split("/")

        if not url.strip():
            raise ValueError(f"Invalid URL(Empty URL)")

        if len(urlTokens) != 7: 
            # ['https:', '', 'docs.google.com', 'document', 'd', 'file ID', 'edit?usp=drive_link']
            raise ValueError(f"Invalid URL(Incorrect structure)")

        if "drive.google.com" not in urlTokens:
            raise ValueError(f"Invalid URL, this must contains: drive.google.com")
            
    def downloadGSFile(self, publicUrl):        
        try:
            # URL Tokens
            tokens = publicUrl.split("/")
            logger.info(f"tokens: {tokens}")
            # Get the file identifier
            file_id = tokens[-2] 

            # Construct the download URL using the file identifier
            download_url = f"https://drive.google.com/uc?export=download&id={file_id}"

            # Download the file
            response = requests.get(download_url, allow_redirects=True)
            # logger.info(f"R-> : {response}")

            # Check for successful download
            if response.status_code == 200:
              # Get filename from response headers (might not always be reliable)
              self.gsFilename = response.headers.get("Content-Disposition").split("filename=")[1].strip('"')
              
              # Save the downloaded content to a local file
              with open(f"/tmp/{self.gsFilename}", "wb") as f:
                f.write(response.content)
              logger.info(f"File downloaded: {self.gsFilename}")
            else:
              logger.info(f"Download failed with status code: {response.status_code}")
        except Exception as e:
            logger.error(f"Error in downloadGSFile:{self.__class__.__name__}")
            raise 
        
    def uploadFileS3(self, bucketName):    
        try:
            s3= boto3.client('s3')
            if not self.gsFilename:
                raise ValueError("filename must be non Empty")

            s3.upload_file(f"/tmp/{self.gsFilename}", bucketName, self.gsFilename)
            logger.info(f"File uploaded")
        except Exception as e:
            logger.error(f"Error in uploadFileS3:{self.__class__.__name__}")
            raise