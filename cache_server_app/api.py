from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework import request

from .serializers import CacheEntryOutputSerializer, FileOutputSerializer
from .serializers import CacheEntryInputSerializer, FileInputSerializer

from .models import Cache_entry, File
from .forms import CacheEntryForm, FileForm

class SubmissionDetails(mixins.RetrieveModelMixin,
                        mixins.CreateModelMixin,
                        generics.GenericAPIView,
                        ):
    """
        API for gettting or updating cached blast data
    """

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SubmissionOutputSerializer
        if self.request.method == 'POST':
            return SubmissionInputSerializer

    def get(self, request, *args, **kwargs):
        """
            Returns the current status of a job
        """
        return self.retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
            Update a PSI-BLAST result
        """
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
            Add a new uniprot ID and then add the pssm/chk
        """
