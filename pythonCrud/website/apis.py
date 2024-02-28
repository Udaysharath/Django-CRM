from rest_framework.response import Response
from rest_framework.views import APIView
from website.models import *


class RecordDataAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            for d in data:
                id = d.get('id')
                c = None
                if id:
                    c = Record.objects.get(id=id)
                    c.first_name = d['first_name']
                    c.last_name = d['last_name']
                    c.email = d['email']
                    c.phone = d['phone']
                    c.address = d['address']
                    c.city = d['city']
                    c.state = d['state']
                    c.zipcode = d['zipcode']
                    c.image = d['image']
                    c.save()
                else:
                    c = Record(**d)
                    c.save()
                Record.append(c.id)
            return Response({
                'success': True,
            })
        except Exception as ex:
            return Response({
                'success': False,
                'message': str(ex)
            }, request)