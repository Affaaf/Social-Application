from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import User
import requests
from datetime import date
import holidays
import geocoder

class SignupSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(write_only = True)
    
    def validate_email(self, value):
        try:
            validate_email(value)
        except ValidationError:
            raise serializers.ValidationError('Invalid email format.')
        return value

    class Meta:
        model = User
        fields = ['username', 'email', 'ip', 'holiday_info','password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
        }

    def create(self, validated_data):
        ip_address = requests.get('https://api64.ipify.org?format=json').json()
        ip= ip_address['ip']

        # Use geocoder to find the geolocation information
        g = geocoder.ip(ip)
        
        # # Extract relevant information from the geocoder result
        latitude = g.latlng[0]
        longitude = g.latlng[1]
        city = g.city
        country = g.country

        # # Print the geolocation information
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
        print(f"City:=================== {city}")
        print(f"Country:================ {country}")
        
        signup_date = date.today()
        
          

        # Get the holidays for the specified country
        holiday_list = holidays.CountryHoliday(country, years=signup_date.year)

        # Check if the specified date is a holiday
        if signup_date in holiday_list:
            holidays_today = holiday_list.get(signup_date)
            print(f"Holiday: {holidays_today[0]}")
            holiday=holidays_today[0]
        else:
            print("No holiday today.")
            holiday="there is no holiday today"
            
      
        holiday = str(holiday)
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            ip = ip,
            holiday_info = holiday
            )
        
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'password must match'})
        user.set_password(password)
        user.save()
        return user




