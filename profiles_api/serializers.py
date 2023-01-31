from rest_framework import serizlizers

class HelloSerializer(serializers.Serializer):
  """Serializes a name field for testing our APIView"""
  name = serizlizers.ChartField(max_length=10)
