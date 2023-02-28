from rest_framework import serializers
from .models import TypingTest,UserProfile

class TypingTestSerializer(serializers.ModelSerializer):
    userName = serializers.CharField(source='user.userName')
    class Meta : 
        model = TypingTest
        fields =  ('id','user','userName','time','wpm','accuracy','raw','dateTaken')

class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = UserProfile
        fields = ('userName','email','profilePhoto','rank')
        
'''
user = models.OneToOneField(User,on_delete=models.CASCADE)
    time = models.IntegerField()
    wpm = models.IntegerField()
    accuracy = models.IntegerField()
    raw = models.IntegerField()
    dateTaken

'''

'''
    userName = models.CharField(max_length=26)
    email = models.EmailField(max_length=254)
    profilePhoto = models.ImageField()
'''