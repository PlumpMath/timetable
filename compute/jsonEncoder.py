from json import JSONEncoder
from gene import gene
from user import person
from sub import subject

def _default(self, obj):
    if isinstance(obj,gene):
        return { "genePairs": obj.genePairs, "geneScore": obj.geneScore }
    elif isinstance(obj,person):
        return { "name": obj.name, "classes": obj.classes }
    elif isinstance(obj,subject):
        return { "id": obj.id, "name": obj.name, "len": obj.len}
    return getattr(obj.__class__, "to_json", _default.default)(obj)

_default.default = JSONEncoder().default  # Save unmodified default.
JSONEncoder.default = _default # replacement