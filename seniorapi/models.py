from django.db import models


class number(models.Model):
    user_id   = models.AutoField(auto_created = True,primary_key = True)
    phone     = models.CharField(max_length=15, null=True)
    activated = models.BooleanField(null=True,default=False)
   
   
    def __str__(self):
        return '{}'.format(self.user_id)


class users(models.Model):
    firstname = models.CharField(max_length=30, null=True)
    secondname = models.CharField(max_length=30, null=True)
    fathername = models.CharField(max_length=30, null=True)
    dateofbirth = models.DateField(null=True,max_length=15)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    profilepic=models.ImageField(null=True, upload_to="images/" )
    cardpic=models.ImageField(null=True, upload_to="images/" )
    car = models.BooleanField(default=False)
    user_id = models.ForeignKey(number, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.first_name)



class car(models.Model):
    Vehicle_Type = models.CharField(max_length=30, null=True)
    car_number = models.CharField(max_length=30, null=True)
    user = models.ForeignKey(number, on_delete=models.CASCADE)

    def __str__(self):
        return "{} ".format(self.Vehicle_Type)


class Stream(models.Model):
    user = models.ForeignKey(number, on_delete=models.CASCADE)
    lat=models.DecimalField(max_digits = 25,decimal_places = 10 )
    lon=models.DecimalField(max_digits = 25,decimal_places = 10 )
    time =models.CharField(max_length=50)
    def __str__(self):
        return '{}'.format( self.lat)


class cluster(models.Model):
    lat=models.DecimalField(max_digits = 25,decimal_places = 10 )
    lon=models.DecimalField(max_digits = 25,decimal_places = 10 )

    def __str__(self):
        return '{}'.format(self.pk)

class cluster_ref(models.Model):
    cluster_id = models.ForeignKey(cluster, on_delete=models.CASCADE)
    start_lat  = models.DecimalField(max_digits = 25,decimal_places = 10 )
    start_lon  = models.DecimalField(max_digits = 25,decimal_places = 10 )
    end_lat    = models.DecimalField(max_digits = 25,decimal_places = 10 )
    end_lon    = models.DecimalField(max_digits = 25,decimal_places = 10 )

    def __str__(self):
        return '{}'.format(self.cluster_id)


class pat_ref(models.Model):
    time = models.DateField(null=True,max_length=30)
    startp_lat = models.DecimalField(max_digits = 25,decimal_places = 10 )
    startp_lon = models.DecimalField(max_digits = 25,decimal_places = 10 )
    endp_lat = models.DecimalField(max_digits = 25,decimal_places = 10 )
    endp_lon = models.DecimalField(max_digits = 25,decimal_places = 10 )
    user = models.ForeignKey(number,on_delete=models.CASCADE)
    cluster = models.IntegerField(null=False,default=0)

    def __str__(self):
        return '{}'.format(self.pk)


class patterns(models.Model):
    lat = models.DecimalField(max_digits = 25,decimal_places = 10 )
    lon = models.DecimalField(max_digits = 25,decimal_places = 10 )

    def __str__(self):
        return '{}'.format(self.pk)

class traj_ref(models.Model):

    time = models.DateField(null=True,max_length=30)
    user = models.ForeignKey(number,on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.pk)


class trajectories(models.Model):
    traj_id = models.ForeignKey(traj_ref, on_delete=models.CASCADE)
    lat = models.DecimalField(max_digits = 25,decimal_places = 10 )
    lon = models.DecimalField(max_digits = 25,decimal_places = 10 )

    def __str__(self):
        return '{}'.format(self.pk)
