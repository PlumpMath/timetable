from json import JSONEncoder
from objs import *
from settings import *

def _default(self, obj):
    if isinstance(obj,gene):
        return { "genePairs": obj.genePairs, "geneScore": obj.geneScore }
    elif isinstance(obj,person):
        return { "name": obj.name, "classes": obj.classes }
    elif isinstance(obj,subject):
        return { "id": obj.id, "name": obj.name, "len": obj.len, "room": obj.room, "timeConstraints": obj.timeConstraints}
    elif isinstance(obj,room):
        return { "id": obj.id, "name": obj.name}
    return getattr(obj.__class__, "to_json", _default.default)(obj)

_default.default = JSONEncoder().default  # Save unmodified default.
JSONEncoder.default = _default # replacement