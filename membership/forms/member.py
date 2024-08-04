
from django import forms
from membership.models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['user', 'join_date', 'status', ]

class MemberUpdateForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['user', 'status', ]
