from django.db import models

class Client(models.Model):
    id = models.CharField(max_length=50, primary_key=True) 
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField()

    class Meta:
        db_table = 'clients'
        managed = False 

class AccMaster(models.Model):
    code = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=250)
    super_code = models.CharField(max_length=5, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=60, blank=True, null=True)
    phone2 = models.CharField(max_length=60, blank=True, null=True)
    client_id = models.CharField(max_length=50)

    class Meta:
        db_table = 'acc_master'
        managed = False  # This tells Django not to try to create the table


class ManualCustomer(models.Model):
    id = models.AutoField(primary_key=True)
    client_id = models.CharField(max_length=50)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        db_table = 'acc_master_manual'
        managed = False
        unique_together = ('client_id', 'name') 



class AccProduct(models.Model):
    code = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    product = models.CharField(max_length=30, blank=True, null=True)
    brand = models.CharField(max_length=30, blank=True, null=True)
    unit = models.CharField(max_length=10, blank=True, null=True)
    taxcode = models.CharField(max_length=5, blank=True, null=True)
    defect = models.CharField(max_length=50, blank=True, null=True)
    company = models.CharField(max_length=30, blank=True, null=True)
    client_id = models.CharField(max_length=50)

    class Meta:
        db_table = 'acc_product'
        managed = False


class AccProductBatch(models.Model):
    productcode = models.CharField(max_length=30, primary_key=True)
    cost = models.DecimalField(
        max_digits=12, decimal_places=3, blank=True, null=True)
    salesprice = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True)
    bmrp = models.DecimalField(
        max_digits=12, decimal_places=3, blank=True, null=True)
    barcode = models.CharField(max_length=35, blank=True, null=True)
    secondprice = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True)
    thirdprice = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True)
    client_id = models.CharField(max_length=50)

    class Meta:
        db_table = 'acc_productbatch'
        managed = False


class AccUsers(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    pass_field = models.CharField(
        max_length=100, db_column='pass')
    role = models.CharField(max_length=30, blank=True, null=True)
    client_id = models.CharField(max_length=50)

    class Meta:
        db_table = 'acc_users'
        managed = False
