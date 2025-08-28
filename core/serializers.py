from rest_framework import serializers
<<<<<<< HEAD
from django.contrib.auth.models import User
from .models import Patient, Doctor, PatientDoctorMapping

# This serializer handles user registration.
=======
from .models import Patient, Doctor, PatientDoctorMapping

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'age', 'address', 'created_by']
        read_only_fields = ['id', 'created_by']


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialization']
        read_only_fields = ['id']


class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.name', read_only=True)
    doctor_name = serializers.CharField(source='doctor.name', read_only=True)

    class Meta:
        model = PatientDoctorMapping
        fields = ['id', 'patient', 'doctor', 'patient_name', 'doctor_name']
        read_only_fields = ['id', 'patient_name', 'doctor_name']


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class MappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctorMapping
        fields = '__all__'

from django.contrib.auth.models import User

>>>>>>> 2ebc91cff0c72749620f5e69ff666b2a1d9577ad
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
<<<<<<< HEAD
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        # Creates a new user using Django's helper function.
=======
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
>>>>>>> 2ebc91cff0c72749620f5e69ff666b2a1d9577ad
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user
<<<<<<< HEAD

# This serializer handles the Doctor model.
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        # Includes all fields from the Doctor model.
        fields = '__all__'

# This serializer handles the Patient model.
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        # Includes all fields from the Patient model.
        fields = '__all__'
        # Ensures 'created_by' is set by the server, not the client.
        read_only_fields = ('created_by',)

# This serializer handles the mapping between Patients and Doctors.
class MappingSerializer(serializers.ModelSerializer):
    # These fields provide human-readable names in the API response.
    patient_name = serializers.CharField(source='patient.name', read_only=True)
    doctor_name = serializers.CharField(source='doctor.name', read_only=True)

    class Meta:
        model = PatientDoctorMapping
        # Includes the IDs for creating the mapping and the names for reading it.
        fields = ('id', 'patient', 'doctor', 'patient_name', 'doctor_name')
        read_only_fields = ('patient_name', 'doctor_name')

=======
>>>>>>> 2ebc91cff0c72749620f5e69ff666b2a1d9577ad
