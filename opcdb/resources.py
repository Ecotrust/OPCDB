from import_export import resources
from .models import LandingRecord

class LandingRecordResource(resources.ModelResource):

    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        if 'id' not in dataset.headers:
            dataset.insert_col(0, col=["",]*dataset.height, header="id")
    #
    # def get_instance(self, instance_loader, row):
    #     return False

    def init_instance(self, row=None):
        try:
            instance = LandingRecord.create(row)
            return instance
        except Exception as e:
            import ipdb; ipdb.set_trace()
            print(e)

        raise NotImplementedError()

    # def get_instance(self, instance_loader, row):
    #     """
    #     If all 'import_id_fields' are present in the dataset, calls
    #     the :doc:`InstanceLoader <api_instance_loaders>`. Otherwise,
    #     returns `None`.
    #     """
    #     for field_name in self.get_import_id_fields():
    #         if field_name not in row:
    #             return
    #     # return instance_loader.get_instance(row)
    #     try:
    #         params = {}
    #         for key in instance_loader.resource.get_import_id_fields():
    #             field = instance_loader.resource.fields[key]
    #             params[field.attribute] = field.clean(row)
    #         if params:
    #             return instance_loader.get_queryset().get(**params)
    #         else:
    #             return None
    #     except instance_loader.resource._meta.model.DoesNotExist:
    #         return None
    #

    class Meta:
        model = LandingRecord
        # import_id_fields = ('landingReceiptNum', 'landingDate', 'fisherId', 'vesselID', 'portID', 'businessID', 'speciesID', 'gearID', 'fishConditionID', 'useID')
