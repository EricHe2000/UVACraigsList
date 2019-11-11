from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings

class PublicMediaStorage(S3Boto3Storage):
	location = 'media'
	default_acl = 'public-read'
	file_overwrite = False

# class PrefixedStorage(storages.backends.s3boto.S3BotoStorage):
# 	def __init__(self, *args, **kwargs):
# 		from django.conf import settings
# 		kwargs['location'] = settings.ASSETS_PREFIX
# 		return super(PrefixedStorage, self).__init__(*args, **kwargs)