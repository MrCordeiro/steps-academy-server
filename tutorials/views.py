from rest_framework import viewsets
from .models import Tutorial
from .serializers import TutorialSerializer

# Create your views here.
class TutorialViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    Additionally we also provide an extra `highlight` action.
    """
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer

