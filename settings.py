from registries.structure import RegistrySchema


SETTINGS = {
    'SQLALCHEMY_DATABASE_URI': 'postgresql://lod:qbdhnLs4@127.0.0.1:5433/test-lod-2_db',
    'SQLALCHEMY_TRACK_MODIFICATIONS': True,
    'RESOURCE_METHODS': ['GET', 'POST', 'DELETE'],
    'ITEM_METHODS': ['GET', 'PATCH', 'DELETE'],
    'DOMAIN': {
        'registry': RegistrySchema._eve_schema['registry'],
    },
    'ID_FIELD': 'id',
    'ITEM_LOOKUP_FIELD': 'id'
}
