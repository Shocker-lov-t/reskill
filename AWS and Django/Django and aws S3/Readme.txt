//S3 Policy//

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AddPerm",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::s3-bucket/*"
        }
    ]
}






===============================================================================

//Settings.py//



import boto3
from storages.backends.s3boto3 import S3Boto3Storage


INSTALLED_APPS = [

    'storages'
]


AWS_ACCESS_KEY_ID =
AWS_SECRET_ACCESS_KEY = 
AWS_STORAGE_BUCKET_NAME = 
AWS_S3_REGION_NAME='ap-south-1'

AWS_QUERYSTRING_AUTH = False


# Set the static files storage backend to S3
STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

# Set the URL for static files
STATIC_URL = f"https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/static/"

AWS_LOCATION = 'media'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Set the URL for media files
MEDIA_URL = f"https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/{AWS_LOCATION}/"

STATIC_ROOT = "https://s3.amazonaws.com/my-static-bucket/"
MEDIA_ROOT = "https://s3.amazonaws.com/my-media-bucket/"




===============================================================================


//urls.py//

from ec2django import settings
from django.conf.urls.static import static

static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

===============================================================================
