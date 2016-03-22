import json
import logging
from uuid import uuid4

from django.db import models
from django.contrib.postgres.fields import ArrayField

import googlemaps

import conf

class BaseModel(models.Model):
    uuid = models.UUIDField(db_index=True, default=uuid4, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Address(models.Model):
    address_l1 = models.CharField(max_length=46)
    address_l2 = models.CharField(max_length=46, null=True, blank=True)
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=5)
    coordinates = ArrayField(
        models.CharField(max_length=12, blank=True),
        size=2,
        null=True,
        blank=True,
        editable=False)
    raw_coordinate_data = models.CharField(null=True, blank=True, max_length=4096)

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return self.address_l1

    def get_coordinates(self):
        gmaps = googlemaps.Client(key=conf.get('GOOGLE_GEOCODING_API_KEY'))
        if self.address_l2 is not None and self.address_l2 != '':
            address = '{} {}, {} {} {}'.format(
                    self.address_l1,
                    self.address_l2,
                    self.city,
                    self.state,
                    self.zip_code
                )
        else:
            address = '{}, {} {} {}'.format(
                    self.address_l1,
                    self.city,
                    self.state,
                    self.zip_code
                )
        geocode_results = gmaps.geocode(address)
        if len(geocode_results) == 0:
            logging.error('no response for your address: {}'.format(address))
            return

        location = geocode_results[0]['geometry']['location']
        latitude = float(location['lat'])
        longitute = float(location['lng'])

        self.raw_coordinate_data = json.dumps(geocode_results)
        self.coordinates = (latitude, longitute)
        self.save()
        return geocode_results, location


class Pantry(BaseModel):
    name = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    facebook = models.URLField(max_length=254, null=True, blank=True)
    twitter = models.CharField(max_length=140, null=True, blank=True)
    instagram = models.CharField(max_length=140, null=True, blank=True)
    address = models.OneToOneField('pantry.Address', related_name='pantry', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Pantries"
