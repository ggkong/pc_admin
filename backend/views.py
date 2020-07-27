from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie

from . import models
from django.http import JsonResponse
# Create your views here.


def login(request):
	username = request.POST.get("username")
	password = request.POST.get("password")
	print(username)
	print(password)
	try:
		user = models.User.objects.get(username=username)
	except:
		date = {'flag': 'no', "msg" : "no to user"}
		return JsonResponse({'request':date})
	if password == user.password:
		date_msg = "登陆成功"
		date_flag = "yes"
		print("成功")
	else:
		date_msg = "密码输入错误"
		date_flag = "no"
	date = {'flag':date_flag,'msg': date_msg}

	return JsonResponse({'request': date})
