from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    
    
    def save(self, *args, **kwargs):
        super().save( *args, **kwargs)

        # Check if the profile has an image associated with it
        if self.image and self.image.path:
            # Open the image and perform operations
            img = Image.open(self.image.path)

            # Example: resize if image height or width is larger than a given size
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)