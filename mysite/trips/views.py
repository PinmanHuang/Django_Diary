from django.shortcuts import render
from datetime import datetime
from trips.models import Post
# Create your views here.

def hello_world(request):
	# output = """
	# 	<!DOCTYPE html>
	# 	<html>
	# 		<head>
	# 			<title>Hello</title>
	# 		</head>
		
	# 		<body>
	# 			Hello World! 
	# 			<em style="color:LightSeaGreen;">
	# 				{current_time}
	# 			</em>
	# 		</body>
	# 	</html>
	# """.format(current_time=datetime.now())
	#return HttpResponse(output)

	#render(請求, Template名稱, 回傳資料):讀進Template的內容
	#data:裡面可以帶入要傳送的所有資料
	data = {
		'current_time': datetime.now(),
		'my_name': 'Joyce'
	}
	return render(request, 'hello_world.html', data)
def home(request):
	post_list = Post.objects.all()
	return render(request, 'home.html', {'post_list':post_list})
def post_detail(request, id):
	post = Post.objects.get(id=id)
	return render(request, 'post.html', {'post':post})