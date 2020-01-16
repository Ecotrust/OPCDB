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
    portID = models.IntegerField(null=True, blank=True, default=None, db_column='PortID')
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

class CpfvRecord(models.Model):
    logMonth = models.IntegerField(db_column='LogMonth')
    logDat = models.IntegerField(db_column='LogDay')
    logYear = models.IntegerField(db_column='LogYear')
    logDate = models.DateField(db_column="LogDate")
    dateReceived = models.DateField(null=True, blank=True, default=None, db_column="DateReceived")
    noActivityMonth = models.CharField(max_length=20,blank=True, null=True, default=None, db_column="NoActivityMonth")
    serialNumber = models.CharField(max_length=50, db_column='SerialNumber')
    vesselID = models.IntegerField(null=True, blank=True, default=None, db_column="VesselID")
    portCode = models.IntegerField(null=True, blank=True, default=None, db_column='PortCode')
    targetSpeciesLingcod = models.CharField(max_length=20,blank=True, null=True, default=None, db_column="TargetSpeciesLingcod")
    targetSpeciesOther = models.CharField(max_length=20,blank=True, null=True, default=None, db_column="TargetSpeciesOther")
    targetSpeciesRockfishes = models.CharField(max_length=20,blank=True, null=True, default=None, db_column="TargetSpeciesRockfishes")
    targetSpeciesSalmon = models.CharField(max_length=20,blank=True, null=True, default=None, db_column="TargetSpeciesSalmon")
    targetSpeciesSharks = models.CharField(max_length=20,blank=True, null=True, default=None, db_column="TargetSpeciesSharks")
    targetSpeciesStripedBass = models.CharField(max_length=20,blank=True, null=True, default=None, db_column="TargetSpeciesStripedBass")
    targetSpeciesSturgeon = models.CharField(max_length=20,blank=True, null=True, default=None, db_column="TargetSpeciesSturgeon")
    targetSpeciesTuna = models.CharField(max_length=20,blank=True, null=True, default=None, db_column="TargetSpeciesTuna")
    targetSpeciesPotluck = models.CharField(max_length=20,blank=True, null=True, default=None, db_column="TargetSpeciesPotluck")
    targetSpeciesMiscCoastal = models.CharField(max_length=20,blank=True, null=True, default=None, db_column="TargetSpeciesMiscCoastal")
    targetSpeciesMiscOffshore = models.CharField(max_length=20,blank=True, null=True, default=None, db_column="TargetSpeciesMiscOffshore")
    targetSpeciesMiscBay = models.CharField(max_length=20,blank=True, null=True, default=None, db_column="TargetSpeciesMiscBay")
    dateSubmitted = models.DateField(null=True, blank=True, default=None, db_column="DateSubmitted")
    fishingMethodTrolling = models.CharField(max_length=20,blank=True, null=True, default=None, db_column="FishingMethodTrolling")
    fishingMethodMooching = models.CharField(max_length=20,blank=True, null=True, default=None, db_column="FishingMethodMooching")
    fishingMethodAnchored = models.CharField(max_length=20,blank=True, null=True, default=None, db_column="FishingMethodAnchored")
    fishingMethodDrifting = models.CharField(max_length=20,blank=True, null=True, default=None, db_column="FishingMethodDrifting")
    fishingMethodDiving = models.CharField(max_length=20,blank=True, null=True, default=None, db_column="FishingMethodDiving")
    fishingMethodLightTackle = models.CharField(max_length=20,blank=True, null=True, default=None, db_column="FishingMethodLightTackle")
    fishingMethodOther = models.CharField(max_length=20,blank=True, null=True, default=None, db_column="FishingMethodOther")
    baitUsedAnchoviesLive = models.CharField(max_length=20,blank=True, null=True, default=None, db_column="BaitUsedAnchoviesLive")
    baitUsedAnchoviesDead = models.CharField(max_length=20,blank=True, null=True, default=None, db_column="BaitUsedAnchoviesDead")
    baitUsedSardinesLive = models.CharField(max_length=20,blank=True, null=True, default=None, db_column="BaitUsedSardinesLive")
    baitUsedSardinesDead = models.CharField(max_length=20,blank=True, null=True, default=None, db_column="BaitUsedSardinesDead")
    baitUsedSquidLive = models.CharField(max_length=20,blank=True, null=True, default=None, db_column="BaitUsedSquidLive")
    baitUsedSquidDead = models.CharField(max_length=20,blank=True, null=True, default=None, db_column="BaitUsedSquidDead")
    baitUsedOtherLive = models.CharField(max_length=20,blank=True, null=True, default=None, db_column="BaitUsedOtherLive")
    baitUsedOtherDead = models.CharField(max_length=20,blank=True, null=True, default=None, db_column="BaitUsedOtherDead")
    tripType = models.CharField(max_length=100, blank=True, null=True, default=None, db_column="TripType")
    nonPaying = models.CharField(max_length=20,blank=True, null=True, default=None, db_column="NonPaying")
    birdInteraction = models.CharField(max_length=20,blank=True, null=True, default=None, db_column="BirdInteraction")
    descendingDevice = models.CharField(max_length=20,blank=True, null=True, default=None, db_column="DescendingDevice")
    block = models.IntegerField(blank=True, null=True, default=None, db_column='Block')
    departureTime = models.IntegerField(blank=True, null=True, default=None, db_column='DepartureTime')
    returnTime = models.IntegerField(blank=True, null=True, default=None, db_column='ReturnTime')
    hoursMinutesFished = models.CharField(max_length=100, blank=True, null=True, default=None, db_column="HoursMinutesFished")
    hoursFished = models.FloatField(blank=True, null=True, default=None, db_column='HoursFished')
    numberOfFishers = models.IntegerField(blank=True, null=True, default=None, db_column='NumberOfFishers')
    depth = models.IntegerField(blank=True, null=True, default=None, db_column='Depth')
    temperature = models.IntegerField(blank=True, null=True, default=None, db_column='Temperature')
    speciesCode = models.CharField(max_length=255, blank=True, null=True, default=None, db_column='SpeciesCode')
    species = models.CharField(max_length=255, blank=True, null=True, default=None, db_column="Species")
    numberKept = models.IntegerField(blank=True, null=True, default=None, db_column='NumberKept')
    numberReleased = models.IntegerField(blank=True, null=True, default=None, db_column='NumberReleased')
    numberLostToSeaLions = models.IntegerField(blank=True, null=True, default=None, db_column='NumberLostToSeaLions')
    numberOfCrewFished = models.IntegerField(blank=True, null=True, default=None, db_column='NumberOfCrewFished')
    operatorName = models.CharField(max_length=255, blank=True, null=True, default=None, db_column="OperatorName")
    submitByName = models.CharField(max_length=255, blank=True, null=True, default=None, db_column="SubmitByName")
    completeDate = models.DateField(blank=True, null=True, default=None, db_column="CompleteDate")
    numberOfFishCaughtByCrew = models.IntegerField(blank=True, null=True, default=None, db_column='NumberOfFishCaughtByCrew')

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
            logMonth = row['LogMonth'],
            logDat = row['LogDay'],
            logYear = row['LogYear'],
            logDate = row['LogDate'],
            dateReceived = row['DateReceived'],
            noActivityMonth = row['NoActivityMonth'],
            serialNumber = row['SerialNumber'],
            vesselID = row['VesselID'],
            portCode = row['PortCode'],
            targetSpeciesLingcod = row['TargetSpeciesLingcod'],
            targetSpeciesOther = row['TargetSpeciesOther'],
            targetSpeciesRockfishes = row['TargetSpeciesRockfishes'],
            targetSpeciesSalmon = row['TargetSpeciesSalmon'],
            targetSpeciesSharks = row['TargetSpeciesSharks'],
            targetSpeciesStripedBass = row['TargetSpeciesStripedBass'],
            targetSpeciesSturgeon = row['TargetSpeciesSturgeon'],
            targetSpeciesTuna = row['TargetSpeciesTuna'],
            targetSpeciesPotluck = row['TargetSpeciesPotluck'],
            targetSpeciesMiscCoastal = row['TargetSpeciesMiscCoastal'],
            targetSpeciesMiscOffshore = row['TargetSpeciesMiscOffshore'],
            targetSpeciesMiscBay = row['TargetSpeciesMiscBay'],
            dateSubmitted = row['DateSubmitted'],
            fishingMethodTrolling = row['FishingMethodTrolling'],
            fishingMethodMooching = row['FishingMethodMooching'],
            fishingMethodAnchored = row['FishingMethodAnchored'],
            fishingMethodDrifting = row['FishingMethodDrifting'],
            fishingMethodDiving = row['FishingMethodDiving'],
            fishingMethodLightTackle = row['FishingMethodLightTackle'],
            fishingMethodOther = row['FishingMethodOther'],
            baitUsedAnchoviesLive = row['BaitUsedAnchoviesLive'],
            baitUsedAnchoviesDead = row['BaitUsedAnchoviesDead'],
            baitUsedSardinesLive = row['BaitUsedSardinesLive'],
            baitUsedSardinesDead = row['BaitUsedSardinesDead'],
            baitUsedSquidLive = row['BaitUsedSquidLive'],
            baitUsedSquidDead = row['BaitUsedSquidDead'],
            baitUsedOtherLive = row['BaitUsedOtherLive'],
            baitUsedOtherDead = row['BaitUsedOtherDead'],
            tripType = row['TripType'],
            nonPaying = row['NonPaying'],
            birdInteraction = row['BirdInteraction'],
            descendingDevice = row['DescendingDevice'],
            block = row['Block'],
            departureTime = row['DepartureTime'],
            returnTime = row['ReturnTime'],
            hoursMinutesFished = row['HoursMinutesFished'],
            hoursFished = row['HoursFished'],
            numberOfFishers = row['NumberOfFishers'],
            depth = row['Depth'],
            temperature = row['Temperature'],
            speciesCode = row['SpeciesCode'],
            species = row['Species'],
            numberKept = row['NumberKept'],
            numberReleased = row['NumberReleased'],
            numberLostToSeaLions = row['NumberLostToSeaLions'],
            numberOfCrewFished = row['NumberOfCrewFished'],
            operatorName = row['OperatorName'],
            submitByName = row['SubmitByName'],
            completeDate = row['CompleteDate'],
            numberOfFishCaughtByCrew = row['NumberOfFishCaughtByCrew'],
        )

    def __str__(self):
        return("%s: %s - %s" % (self.serialNumber, self.species, self.logDate))


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

class InflationIndex(models.Model):
    year = models.IntegerField(primary_key=True)
    cpi = models.FloatField()
    # Having the below value pre-calculated is super handy, but goes against DB design standards
    inflFactor = models.FloatField(null=True, blank=True, default=None)
    # Adding this field makes the previous field more forgivable
    yearCalculated = models.IntegerField(default=2018)

    def __str__(self):
        return "%s: %s" % (self.year, self.cpi)
