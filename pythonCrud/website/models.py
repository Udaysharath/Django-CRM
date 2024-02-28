from django.db import models

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    first_name =models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=15)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
    
    def get_record_json(self):
        record_json = self
        record_json['id'] = self.id
        record_json['created_at'] = self.created_at
        record_json['first_name'] = self.first_name
        record_json['last_name'] = self.last_name
        record_json['email'] = self.email
        record_json['phone'] = self.phone
        record_json['address'] = self.address
        record_json['city'] = self.city
        record_json['state'] = self.state
        record_json['zipcode'] = self.zipcode
        record_json['image'] = self.image
        
        return record_json
    
    
