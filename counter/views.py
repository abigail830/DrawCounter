from django.shortcuts import render

from django.http import HttpResponse
from .models import Member, Counter
from django.template import loader


def health(request):
    return HttpResponse("I am Health!")


def index(request):
    summary=[]
    full_list = Member.objects.all()
    for member_info in full_list:
        member_detail = {
            "id" : member_info.id,
            "member_name":  member_info.member_name,
            "remark": member_info.remark,
            "count": Counter.objects.all().values().filter(member=member_info).latest('last_update_date')}
        summary.append(member_detail)

    template = loader.get_template('counter/members.html')
    context = {
        'summary': summary,
    }
    return HttpResponse(template.render(context, request))


def detail(request, id):

    member = Member.objects.get(pk=id)

    template = loader.get_template('counter/detail.html')
    context = {
            'name': member.member_name,
            'join_date': member.join_date,
            'remark': member.remark,
            'history': Counter.objects.filter(member=member),
    }

    return HttpResponse(template.render(context, request))