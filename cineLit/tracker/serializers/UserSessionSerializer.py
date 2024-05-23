from rest_framework import serializers


class ItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    type = serializers.ChoiceField(choices=['film', 'book'])


class AddSessionSerializer(serializers.Serializer):
    item = ItemSerializer()
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField(required=False)
    duration = serializers.IntegerField(required=False)
    pages_read = serializers.IntegerField(required=False)
    watching_time = serializers.IntegerField(required=False)



