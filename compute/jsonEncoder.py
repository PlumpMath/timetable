from json import JSONEncoder
from gene import gene

def _default(self, obj):
    if isinstance(obj,gene):
        return { "genePairs": obj.genePairs, "geneScore": obj.geneScore }
    return getattr(obj.__class__, "to_json", _default.default)(obj)

_default.default = JSONEncoder().default  # Save unmodified default.
JSONEncoder.default = _default # replacement