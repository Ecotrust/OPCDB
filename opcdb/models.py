from django.db import models

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

    def __str__(self):
        return("%s: %s - %s" % (self.landingReceiptNum, self.speciesName, self.landingDate))

class PortGroupLookup(models.Model):
    projectShortCode = models.CharField(max_length=255, db_column="Project short code")
    portName = models.CharField(max_length=100, db_column="Port name")
    lat = models.FloatField(db_column="Lat")
    lon = models.FloatField(db_column="Long")
    portGroup = models.CharField(max_length=100, db_column="Port group")
    californiaRegion= models.CharField(max_length=100, db_column="California Region")
    portCode = models.IntegerField(db_column="Port code")

    def __str__(self):
        return self.portName

class SpeciesGroupLookup(models.Model):
    projectShortCode = models.CharField(max_length=255, db_column="Project short code")
    speciesCode = models.IntegerField(db_column="Species Code")
    speciesName= models.CharField(max_length=255, db_column="Species Name")
    commercialSpeciesGroup = models.CharField(max_length=255, db_column="Commercial Species Group")
    gearCode = models.IntegerField(db_column="Gear Code")
    gearDescription = models.CharField(max_length=255, db_column="Gear Description")
    gearGroup = models.CharField(max_length=255, db_column="Gear Group")
    commeciarlDataViewer = models.CharField(max_length=4, db_column="Commercial Data Viewer")
    cPFVSpeciesGroup = models.CharField(max_length=255, db_column="CPFV Species Group")
    cPFVDataViews = models.CharField(max_length=4, db_column="CPFV Data Viewer")

    def __str__(self):
        return "%s - %s" % (self.speciesName, self.gearDescription)






# SELECT
#     [1992].Landing_Year,
#     TblPrtGrpLkup_update1.Mlpa_stdy_reg,
#     TblPrtGrpLkup_update1.Port_group,
#     TblSpsGrps_update1.COMM_Sps,
#     TblGearLkup_update1.Gear_grp,
#     [1992].Condition_Group,
#     Sum([1992].Pounds) AS SumOfPounds,
#     Sum([1992].Value_Inflation) AS SumOfValue_Inflation,
#     Avg([1992].Price_Inflation) AS AvgOfPrice_Inflation,
#     TblSpsGrps_update1.Comm_NC
# FROM
#     (
#         (1992 INNER JOIN TblSpsGrps_update1 ON [1992].Species_Code = TblSpsGrps_update1.SPECIES_CODE)
#         INNER JOIN TblGearLkup_update1 ON [1992].Gear_Code = TblGearLkup_update1.[Gear Code]
#     ) INNER JOIN TblPrtGrpLkup_update1 ON [1992].Port_Code = TblPrtGrpLkup_update1.Portcode
# GROUP BY
#     [1992].Landing_Year,
#     TblPrtGrpLkup_update1.Mlpa_stdy_reg,
#     TblPrtGrpLkup_update1.Port_group,
#     TblSpsGrps_update1.COMM_Sps,
#     TblGearLkup_update1.Gear_grp,
#     [1992].Condition_Group,
#     TblSpsGrps_update1.Comm_NC
# HAVING
#     (
#         ((TblPrtGrpLkup_update1.Mlpa_stdy_reg)="NCSR")
#     );
