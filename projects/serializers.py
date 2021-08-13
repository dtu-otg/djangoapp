from rest_framework import serializers,status
from .models import Project
from user.models import Profile,User


class SpecialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('image',)


class CreateProjectSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required = True)
    image = serializers.ImageField(required=False)


    class Meta:
        model = Project
        fields = ('owner','id','name','description','image','discord')
        
class GetProjectSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    owner_pic = serializers.SerializerMethodField()
    
    def get_owner_pic(self,obj):
        here = SpecialSerializer(Profile.objects.get(owner = User.objects.get(username = obj.owner.username)))
        return here.data['image']
    def get_owner(self,obj):
        username = obj.owner.username
        return username

    class Meta:
        model = Project
        fields = ('id','owner','name','description','discord','image','owner_pic')