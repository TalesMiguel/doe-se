from djgeojson.fields import PointField
from djgeojson.serializers import Serializer as GeoJSONSerializer
from ..models import Acoes

def serialize():
    resposta = GeoJSONSerializer().serialize(Acoes.objects.all(), use_natural_keys=True, with_modelname=False)
    return resposta