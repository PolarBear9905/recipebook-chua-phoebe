import cloudinary.uploader
import cloudinary
from django.core.files.storage import Storage

class CloudinaryStorage(Storage):
    def deconstruct(self):
        return ('recipebook.storage.CloudinaryStorage', [], {})

    def _save(self, name, content):
        result = cloudinary.uploader.upload(
            content,
            public_id=name.split('.')[0],
            overwrite=True,
            resource_type='auto'
        )
        return result['secure_url']

    def url(self, name):
        return name

    def exists(self, name):
        return False