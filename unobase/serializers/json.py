"""
Serialize data to/from JSON
"""
from django.utils import simplejson
from python import Serializer as PythonSerializer
from django.core.serializers.json import Deserializer as JSONDeserializer, \
    DjangoJSONEncoder

class Serializer(PythonSerializer):
    """
    Convert a queryset to JSON.
    """
    def end_serialization(self, qs):
        """Output a JSON encoded queryset."""

        if not qs:
            simplejson.dump(self.objects[0], self.stream, cls=DjangoJSONEncoder,
                **self.options)
        else:
            simplejson.dump(self.objects, self.stream, cls=DjangoJSONEncoder,
                **self.options)

    def getvalue(self):
        """
        Return the fully serialized queryset (or None if the output stream
        is not seekable).
        """

        if callable(getattr(self.stream, 'getvalue', None)):
            return self.stream.getvalue()

Deserializer = JSONDeserializer
