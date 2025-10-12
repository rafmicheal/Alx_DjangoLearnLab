from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.CharField(
        source='actor.username', read_only=True)
    target_repr = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ['id', 'actor', 'actor_username',
                  'verb', 'target_repr', 'unread', 'timestamp']
        read_only_fields = ['id', 'actor_username', 'timestamp', 'actor']

    def get_target_repr(self, obj):
        try:
            return str(obj.target)
        except Exception:
            return None
