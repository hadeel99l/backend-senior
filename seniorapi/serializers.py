from rest_framework import serializers
from .models import number, users, car, Stream, cluster, cluster_ref, pat_ref, patterns, traj_ref, trajectories


class numberSerializer(serializers.ModelSerializer):

    class Meta:
        model = number
        fields = '__all__'


class usersSerializer(serializers.ModelSerializer):

    class Meta:
        model = users
        fields = '__all__'

class carSerializer(serializers.ModelSerializer):

    class Meta:
        model = car
        fields = '__all__'

class StreamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stream
        fields = '__all__'


class clusterSerializer(serializers.ModelSerializer):

    class Meta:
        model = cluster
        fields = '__all__'


class cluster_refSerializer(serializers.ModelSerializer):

    class Meta:
        model = cluster_ref
        fields = '__all__'


class pat_ref_Serializer(serializers.ModelSerializer):

    class Meta:
        model = pat_ref
        fields = '__all__'

class patternsSerializer(serializers.ModelSerializer):

    class Meta:
        model = patterns
        fields = '__all__'

class traj_refSerializer(serializers.ModelSerializer):

    class Meta:
        model = traj_ref
        fields = '__all__'


class trajectoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = trajectories
        fields = '__all__'
