from django.db import models

# Create your models here.
class LandingRecord(models.Model):
    landingReceiptNum = models.CharField(max_length=50, db_column='LandingReceiptNum')
    landingDate = models.DateField(db_column="LandingDate")
    fisherId = models.CharField(max_length=50, db_column='FisherID')
    fisherName = models.CharField(max_length=255, null=True, blank=True, default=None, db_column='FisherName')
    fisherAbv = models.CharField(max_length=4, null=True, blank=True, default=None, db_column='FisherAbv')
    vesselID = models.IntegerField(null=True, blank=True, default=None, db_column="VesselID")
    fGVesselName = models.CharField(max_length=255, null=True, blank=True, default=None, db_column='FGVesselName')
    vesselAbv = models.CharField(max_length=4, null=True, blank=True, default=None, db_column='VesselAbv')
    statePermitNumber = models.CharField(max_length=20, null=True, blank=True, default=None, db_column='StatePermitNumber')
    gFPermitNum = models.CharField(max_length=50, null=True, blank=True, default=None, db_column='GFPermitNum')
    portID = models.IntegerField(db_column='PortID')
    portName = models.CharField(max_length=255, null=True, blank=True, default=None, db_column='PortName')
    cDFWBlockID = models.IntegerField(null=True, blank=True, default=None, db_column='CDFWBlockID')
    blockName = models.CharField(max_length=255, null=True, blank=True, default=None, db_column='BlockName')
    businessID = models.IntegerField(null=True, blank=True, default=None, db_column='BusinessID')
    fishBusinessName = models.CharField(null=True, blank=True, default=None, max_length=255, db_column='FishBusinessName')
    businessAbv = models.CharField(null=True, blank=True, default=None, max_length=4, db_column='BusinessAbv')
    plantID = models.IntegerField(null=True, blank=True, default=None, db_column='PlantID')
    primaryGearID = models.IntegerField(null=True, blank=True, default=None, db_column='PrimaryGearID')
    primaryGearName = models.CharField(max_length=255, null=True, blank=True, default=None, db_column='PrimaryGearName')
    speciesID = models.IntegerField(null=True, blank=True, default=None, db_column='SpeciesID')
    speciesName = models.CharField(max_length=255, null=True, blank=True, default=None, db_column='SpeciesName')
    quantity = models.IntegerField(null=True, blank=True, default=None, db_column='Quantity')
    pounds = models.IntegerField(null=True, blank=True, default=None, db_column='Pounds')
    unitPrice = models.FloatField(null=True, blank=True, default=None, db_column='UnitPrice')
    totalPrice = models.FloatField(null=True, blank=True, default=None, db_column='TotalPrice')
    gearID = models.IntegerField(null=True, blank=True, default=None, db_column='GearID')
    gearName = models.CharField(max_length=255, null=True, blank=True, default=None, db_column='GearName')
    depthName = models.CharField(max_length=255, null=True, blank=True, default=None, db_column='DepthName')
    gradeName = models.CharField(max_length=255, null=True, blank=True, default=None, db_column='GradeName')
    fishConditionID = models.IntegerField(null=True, blank=True, default=None, db_column='FishConditionID')
    fishConditionName = models.CharField(null=True, blank=True, default=None, max_length=255, db_column='FishConditionName')
    useID = models.IntegerField(null=True, blank=True, default=None, db_column='UseID')
    useName = models.CharField(max_length=255, null=True, blank=True, default=None, db_column='UseName')

    @classmethod
    def create(cls, row):
        if 'id' in row.keys():
            instance_id = row['id']
        else:
            instance_id = ''
        for key in row.keys():
            if row[key] == '*':
                row[key] = None
        return cls(
            id = instance_id,
            landingReceiptNum = row['LandingReceiptNum'],
            landingDate = row['LandingDate'],
            fisherId = row['FisherID'],
            fisherName = row['FisherName'],
            fisherAbv = row['FisherAbv'],
            vesselID = row['VesselID'],
            fGVesselName = row['FGVesselName'],
            vesselAbv = row['VesselAbv'],
            statePermitNumber = row['StatePermitNumber'],
            gFPermitNum = row['GFPermitNum'],
            portID = row['PortID'],
            portName = row['PortName'],
            cDFWBlockID = row['CDFWBlockID'],
            blockName = row['BlockName'],
            businessID = row['BusinessID'],
            fishBusinessName = row['FishBusinessName'],
            businessAbv = row['BusinessAbv'],
            plantID = row['PlantID'],
            primaryGearID = row['PrimaryGearID'],
            primaryGearName = row['PrimaryGearName'],
            speciesID = row['SpeciesID'],
            speciesName = row['SpeciesName'],
            quantity = row['Quantity'],
            pounds = row['Pounds'],
            unitPrice = row['UnitPrice'],
            totalPrice = row['TotalPrice'],
            gearID = row['GearID'],
            gearName = row['GearName'],
            depthName = row['DepthName'],
            gradeName = row['GradeName'],
            fishConditionID = row['FishConditionID'],
            fishConditionName = row['FishConditionName'],
            useID = row['UseID'],
            useName = row['UseName'],
        )