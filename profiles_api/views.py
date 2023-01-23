from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test api view"""

    def get(self,request,format=None):
        """Returns a list of APIView features"""

        an_apiview=[
        'hello',
        'welcome',
        'to',
        'Hyderabad'
        ]

        return Response({'an_apiview':an_apiview})
