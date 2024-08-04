
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from membership.models import Member
import math
from core.utils import check_missing_fields
from .utils import detail_data, create_member, put_member
class MemberListCreateView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def get(self, request):
        members = Member.objects.all()
        page_index = int(request.GET.get('page_index', 1))
        page_size = int(request.GET.get('page_size', 10))
        offset = (page_index - 1) * page_size
        totalCount = members.count()
        response = {}
        for member in members[offset:offset + page_size]:
            response["data"] = prepate_list_data(member)
        
        response["pagination"] = {
            "page_size": page_size,
            "page_index": page_index,
            "total_count": totalCount,
            "total_pages": math.ceil(totalCount / page_size)
        }
        return JsonResponse(response)

    def post(self, request):
        data = request.data
        required_fields = ['user', 'client', 'join_date', 'status', 'phone_number', 'address', 'sex', 'age', 'email']
        missing_fields = check_missing_fields(data, required_fields)
        if missing_fields:
            return JsonResponse({'error': f'Missing fields: {", ".join(missing_fields)}'}, status=400)
        try:
            member = create_member(data)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        return JsonResponse({'success': True, 'message': 'Member created successfully'})

class MemberDetailView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def get(self, request, pk):
        member = get_object_or_404(Member, pk=pk)
        return JsonResponse({'success': True, 'data': detail_data(data)})

    def put(self, request, pk):
        member = get_object_or_404(Member, pk=pk)
        try:
            member = put_member(member, data)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        return JsonResponse({'success': True, 'message': 'Member is updated successfully'})

    def delete(self, request, pk):
        member = get_object_or_404(Member, pk=pk)
        try:
            member.soft_delete()
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
        return JsonResponse({'success': True, 'message': 'Member is deleted successfully'})
