from rest_framework import serializers


class AddSessionSerializer(serializers.Serializer):
    item_id = serializers.IntegerField()
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField(required=False)
    duration = serializers.IntegerField(required=False)
    pages_read = serializers.IntegerField(required=False)
    watching_time = serializers.IntegerField(required=False)



