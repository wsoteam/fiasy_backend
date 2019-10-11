from elasticsearch_dsl import analyzer

from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from products.models import Product, Category, Brand, MeasurementUnit


@registry.register_document
class ProductDocument(Document):
    name = fields.StringField(
        fields={
            'raw': fields.StringField(analyzer='keyword'),
            'suggest': fields.CompletionField(),
        }
    )
    name_en = fields.StringField(
        fields={
            'raw': fields.StringField(analyzer='keyword'),
            'suggest': fields.CompletionField(),
        }
    )
    name_de = fields.StringField(
        fields={
            'raw': fields.StringField(analyzer='keyword'),
            'suggest': fields.CompletionField(),
        }
    )
    name_pt = fields.StringField(
        fields={
            'raw': fields.StringField(analyzer='keyword'),
            'suggest': fields.CompletionField(),
        }
    )
    name_es = fields.StringField(
        fields={
            'raw': fields.StringField(analyzer='keyword'),
            'suggest': fields.CompletionField(),
        }
    )
    category = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'name': fields.TextField()
    })
    brand = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        # 'name': fields.TextField()
        'name': fields.StringField(analyzer='keyword')
    })
    measurement_units = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'name': fields.TextField(),
        'amount': fields.FloatField()
    })

    def get_instances_from_related(self, related_instance):
        pass

    class Index:
        # Name of the Elasticsearch index
        name = 'products'
        # See Elasticsearch Indices API reference for available settings
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
            'max_result_window': 200000
        }

    class Django:
        model = Product  # The model associated with this Document

        # The fields of the model indexed in Elasticsearch
        fields = [
            # 'name',
            'id',
            'full_info',
            'portion',
            'is_liquid',
            'kilojoules',
            'calories',
            'proteins',
            'carbohydrates',
            'sugar',
            'fats',
            'saturated_fats',
            'monounsaturated_fats',
            'polyunsaturated_fats',
            'cholesterol',
            'cellulose',
            'sodium',
            'pottasium',
        ]
        related_models = [
            Category,
            Brand,
            MeasurementUnit
        ]
