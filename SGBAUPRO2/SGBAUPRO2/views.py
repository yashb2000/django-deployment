from django.shortcuts import render,redirect
from .models import memberOperations
from .models import memberOperations
# from urllib import request as rq
from django.http import JsonResponse


def home(request):
    dic={}
    return render(request,"index.html",dic)


def allmember(request):
 
    obj = memberOperations()
    faculty_names = obj.get_all_faculties()  
    return render(request, "getallmember.html", {'faculties': faculty_names})


def filter_members(request):
   
    if request.method == "GET" and "faculty" in request.GET:
        faculty = request.GET["faculty"]
        obj = memberOperations()
        filtered_data = obj.get_members_by_faculty(faculty)
        return JsonResponse({'memberdata': filtered_data})
    return JsonResponse({'error': 'Invalid request'}, status=400)


def searchmember(request):
    if request.method == 'POST':
        dic = {}
        try:      
            member_id = request.POST.get("MemberID")
            if not member_id:
                dic['error'] = "Please provide a Member ID."
                return render(request, "Searchmember.html", dic)

            obj = memberOperations()
            member_data = obj.searchonMemberID(member_id)

            if not member_data:
                dic['error'] = "No member found with the provided Member ID."
                return render(request, "Searchmember.html", dic)

            return redirect('displaymember', member_id=member_data['MemberID'])

        except Exception as e:
            print(f"Error in searching data: {e}")
            dic['error'] = "There was an error processing your request."
            return render(request, "Searchmember.html", dic)
    else:
        return render(request, "Searchmember.html")



def displaymember(request, member_id):
    obj = memberOperations()
    member_data = obj.searchonMemberID(member_id)
    
    if not member_data:
        return render(request, "Displaymember.html", {'error': "Member not found."})

    signature_path = member_data.get('SIGNATURE', 'images/hod_signature.png')  

    member_data['SIGNATURE'] = signature_path

    return render(request, "Displaymember.html", member_data)





def newMember(request):
    return render(request, "NewMember.html")

def addMember(request):
    msg = None
    if request.method == "POST":
        try:
            mid = request.POST.get("MemberId")
            certnm = request.POST.get("CERTNAME")
            meetname = request.POST.get("MEETINGNAME")
            meetdate = request.POST.get("MEETINGDATE")
            mobno = request.POST.get("MOBILENO")
            emailid = request.POST.get("EMAILID")
            catg = request.POST.get("CATEGORY")

            obj = memberOperations()
            msg = obj.addMember(mid, certnm, meetname, meetdate, mobno, emailid, catg)
        
        except Exception as e:
            msg = "Error in insert: " + str(e)  
        dic = {'status': msg}  
        return render(request, "Newmemberstatus.html", dic)




def delmember(request):
    return render(request,"DeleteMember.html")

def delete(request):
    dic={}
    if request.method=="POST":
        try:
            mid=request.POST.get("MemberId")
            obj=memberOperations()
            msg=obj.deleteMember(mid)
            dic={'status':msg}
        except Exception as e:
            print("Error in delete:",e)
            dic={'status':"Error in delete:"+str(e)}
    return render(request,"Deletestatus.html",dic)

























    
# def print_view(request):
#     context = {
      
#     }
#     return render(request, 'print_template.html', context)
