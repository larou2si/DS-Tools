from PIL import Image
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(default='defaultprofile.jpg', upload_to='profile_pics')
    email_confirmed = models.BooleanField(default=False)

    # role = manager, supermanager, simpleUser, superadmin
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('dsuser:profile', args=[self.id])

    def pokes(self):
        return str(Poke.objects.filter(poked=self.user).count())

    def my_pokes(self):
        return User.objects.exclude(id=self.user.id).exclude(is_superuser=True).all()


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()
        # if instance.is_staff and not instance.is_superuser:


class InstallationResource(models.Model):
    title = models.CharField(max_length=255, blank=True, null=False)
    url = models.URLField()

    class Meta:
        db_table = 'installation_resource'


class Poke(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=False)
    poked = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=False, related_name="poked")
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    viewed = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'poke'