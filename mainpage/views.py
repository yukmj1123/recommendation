

from django.shortcuts import render
from .models import Jeju, Busan, Seoul,Ulsan ,Gangwon, Gyeongbuk,  Gyeonggi,Gyeongnam ,Gwangju,Incheon,Chungbuk,Chungnam,Jeonbuk,Jeonnam,Daegu,Daejeon,Sejong

def mainpage(request):
    return render(request, 'mainpage.html')

def new(request):
    return render(request, 'new.html')
    
def third(request):
    return render(request, 'third.html')


def SearchFuncOk(request):
    query = request.GET.get('query')
    if query=='제주도':
        data=Jeju.objects.all().order_by('total')[:3]
        return render(request,'mainpage.html',{'data': data})

    elif query=='서울특별시':
        data=Seoul.objects.all().order_by('total')[:3]
        return render(request,'mainpage.html',{'data': data})

    elif query=='세종특별자치시':
        data=Sejong.objects.all().order_by('total')[:3]
        return render(request,'mainpage.html',{'data': data})

    elif query=='부산광역시':
        data=Busan.objects.all().order_by('total')[:3]
        return render(request,'mainpage.html',{'data': data})
    
    elif query=='대전광역시':
        data=Daejeon.objects.all().order_by('total')[:3]
        return render(request,'mainpage.html',{'data': data})

    elif query=='대구광역시':
        data=Daegu.objects.all().order_by('total')[:3]
        return render(request,'mainpage.html',{'data': data})  

    
    elif query=='인천광역시':
        data=Incheon.objects.all().order_by('total')[:3]
        return render(request,'mainpage.html',{'data': data})  
    
    elif query=='울산광역시':
        data=Ulsan.objects.all().order_by('total')[:3]
        return render(request,'mainpage.html',{'data': data})

    elif query=='광주광역시':
        data=Gwangju.objects.all().order_by('total')[:3]
        return render(request,'mainpage.html',{'data': data})
    
    elif query=='경기도':
        data=Gyeonggi.objects.all().order_by('total')[:3]
        return render(request,'mainpage.html',{'data': data})
    
    elif query=='강원도':
        data=Gangwon.objects.all().order_by('total')[:3]
        return render(request,'mainpage.html',{'data': data})
    
    elif query=='경상남도':
        data=Gyeongnam.objects.all().order_by('total')[:3]
        return render(request,'mainpage.html',{'data': data})

    elif query=='경상북도':
        data=Gyeongbuk.objects.all().order_by('total')[:3]
        return render(request,'mainpage.html',{'data': data})
    
    elif query=='충청북도':
        data=Chungbuk.objects.all().order_by('total')[:3]
        return render(request,'mainpage.html',{'data': data})

    elif query=='충청남도':
        data=Chungnam.objects.all().order_by('total')[:3]
        return render(request,'mainpage.html',{'data': data}) 

    elif query=='전라북도':
        data=Jeonbuk.objects.all().order_by('total')[:3]
        return render(request,'mainpage.html',{'data': data})

    elif query=='전라남도':
        data=Jeonnam.objects.all().order_by('total')[:3]
        return render(request,'mainpage.html',{'data': data}) 
    


def index(request):
	return render(request, 'third.html')




def review(request):
    return render(request, 'review.html')



