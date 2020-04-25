from rest_framework import serializers

from .models import Category, Specialist


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def create(self, validated_data):
        category = Category.objects.create(**validated_data)
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class SpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = ['id', 'title', 'age', 'gender', 'city', 'likes', 'comments', 'front_image', 'first_image',
                  'second_image', 'third_image', 'category']
