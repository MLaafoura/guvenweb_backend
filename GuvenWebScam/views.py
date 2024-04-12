from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ScamReport
from .serializers import ScamReportSerializer


@api_view(['GET'])
def get_all_scams(request):
    scamReport = ScamReport.objects.all()
    serializer = ScamReportSerializer(scamReport, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_scamreport_by_id(request, scam_id):
    try:
        scam_report = ScamReport.objects.get(id=scam_id)
    except ScamReport.DoesNotExist: 
        return Response({"Error": "Scam Report Not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ScamReportSerializer(scam_report)
    
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_scam_report(request):
    if request.method == 'POST':
        serializer = ScamReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_scam_report(request, scam_id):
    try:
        scam = ScamReport.objects.get(id=scam_id)
    except ScamReport.DoesNotExist:
        return Response({"Error":"Scam Report Not Found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = ScamReportSerializer(scam, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_scam_report(request, scam_id):
    try:
        scam = ScamReport.objects.get(id=scam_id)
    except ScamReport.DoesNotExist:
        return Response({"Error":"Scam Report Not Found"}, status=status.HTTP_404_NOT_FOUND)

    scam.delete()
    return Response({"Message":"Scam report deleted successfully"}, status=status.HTTP_204_NO_CONTENT)




        
        
