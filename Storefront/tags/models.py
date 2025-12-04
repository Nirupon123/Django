from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.
class taggedItemManager(models.Manager):
    def get_by_model(self,obj_type,obj_id):
        content_type=ContentType.objects.get_for_model(obj_type)
        return tagedItem.objects. \
        select_related('tag')\
        .filter( 
            content_type=content_type,
            object_id=obj_id)
    
class tag(models.Model):
    label=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.label

class tagedItem(models.Model):
    objects=taggedItemManager()
    tag=models.ForeignKey(tag,on_delete=models.CASCADE)
    content_type=models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id=models.PositiveIntegerField()
    content_object=GenericForeignKey()