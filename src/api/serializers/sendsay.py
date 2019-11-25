from rest_framework import serializers

_ios_group_id = 'pl9585'
_android_group_id = 'pl52957'

OS_CHOICES = (
    (_ios_group_id, 'IOS'),
    (_android_group_id, 'Android')
)


class SendsaySetMemberSerializer(serializers.Serializer):
    email = serializers.EmailField()
    os = serializers.CharField()
