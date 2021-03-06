from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile, Message
from feedpage.models import Notice
from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate as django_authenticate
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

from django.http import JsonResponse

# 비밀번호 변경
from django.contrib.auth.hashers import check_password

from django.core.paginator import Paginator 

# 회원가입
def signup(request):

    # POST 방식
    if request.method == "POST":
        print(request.POST)
        
        # form 값 저장
        user_id = request.POST['user_id'] # User, 아이디
        password = request.POST['password'] # User, 비밀번호
        confirm_password = request.POST['confirm_password'] # 비밀번호 확인
        name = request.POST['name'] # Profile, 이름
        nickname = request.POST['nickname'] # Profile, 닉네임
        email = request.POST['email'] # User, 이메일
        building_category = request.POST['building_category']  # Profile, 생활관
        building_dong = request.POST['building_dong'] # Profile, 동

        # 1차, 2차 비밀번호 일치여부 판단(js에서 1차 검증)
        if password == confirm_password:
            # 유저 생성            
            user = User.objects.create_user(
                username=user_id,
                password=password,
            )
            
            user.profile.name = name
            user.profile.nickname = nickname
            user.profile.email = email
            user.profile.building_category = building_category
            user.profile.building_dong = building_dong
            user.save()

        login_user = django_authenticate(username=user_id, password=password)
        django_login(request, login_user)
        return redirect('showmain')
        
    return render(request, 'accounts/signup.html')

# 아이디 중복 확인
def id_db_check(request):
    username = request.GET['user_id']

    try:
        # 아이디 중복 o (사용 불가능)
        user = User.objects.get(username=username)
    except:
        # 아이디 중복 x (사용 가능)
        user = None

    if user is None:
        db_check = "pass"
    else:
        db_check = "fail"

    context = {'db_check': db_check}

    return JsonResponse(context)

# 닉네임 중복 확인
def nk_db_check(request):
    nickname = request.GET['nickname']

    try:
        user = Profile.objects.get(nickname=nickname)
    except:
        user = None

    try:        
        if(request.user.profile == user):
            db_check = "pass1"
        else: 
            db_check = "fail1" 
            
    except:
        # 닉네임 중복 o (사용 불가능)
        if user is None:
            db_check = "pass"
        # 닉네임 중복 x (사용 가능)
        else:
            db_check = "fail"
    
    context = {'db_check': db_check}

    return JsonResponse(context)

# 로그인 기능
def login(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        password = request.POST['password']

        # 로그인
        user = auth.authenticate(request, username=user_id, password=password)

        # 성공
        if user is not None:
            auth.login(request, user)
            return redirect('showmain')

        # 실패
        else:
            if user_id == "" or password == "":
                error = "아이디와 비밀번호를 모두 입력해주세요."
            else:
                error = "아이디와 비밀번호를 확인해주세요."
        
        return render(request, 'accounts/login.html', {'error': error})

    else:
        return render(request, 'accounts/login.html')

# 로그아웃 기능
def logout(request):
    auth.logout(request)
    return redirect('showmain')


# 개인정보 변경하기
@login_required
def userEdit(request, id): 

    # 개인정보 변경하기 url 접근할 때
    if request.method == 'GET': 
        return render(request, 'accounts/user_edit.html', {'id': id})

    # 개인정보 변경하기 버튼을 클릭할 때
    elif request.method == 'POST': 
        current_user = request.user
        current_password = request.POST['origin_password']

        # 현재 비밀번호와 입력한 비밀번호가 일치할 때
        if check_password(current_password, current_user.password): 
            User.objects.filter(username=request.user.username).update(
                email=request.POST['email'],
            )            
            Profile.objects.filter(user=request.user).update(
                name=request.POST['name'],
                nickname=request.POST['nickname'],
                building_category=request.POST['building_category'],
                building_dong=request.POST['building_dong'],
            )

            return redirect('userinfo', id=id)

        # 현재 비밀번호와 입력한 비밀번호가 일치하지 않을 때
        else:
            return redirect('useredit', id=id)

# 비밀번호 변경하기
@login_required
def passwordEdit(request, id):
    if request.method == 'GET':
        return render(request, 'accounts/pw_edit.html', {'id': id})

    elif request.method == 'POST':    
        current_user = request.user
        current_password = request.POST['origin_password']

        # 1) 기존 비밀번호와 입력한 비밀번호의 비교
        if check_password(current_password, current_user.password): 
            new_password = request.POST['new_password']
            password_confirm = request.POST['password_confirm']

            # 2) 새로운 비밀번호와 확인까지 일치할 때 비밀번호 변경완료
            if new_password == password_confirm:
                current_user.set_password(new_password)
                current_user.save()                
                update_session_auth_hash(request, current_user)  # 변경된 비밀번호로 로그인 시켜주기
                return redirect('userinfo', id=id)
        return redirect('passwordedit', id=id)

def pwCheck(request):
    if request.method == 'POST':
        current_user = request.user
        current_password = request.POST['origin_password']

        if check_password(current_password, current_user.password):
            return JsonResponse({'pwcheck': 'true'})
        else:
            return JsonResponse({'pwcheck': 'false'})
    elif request.method == 'GET':
        return redirect('showmain')

def userInfo(request, id):

    return render(request, 'accounts/user_info.html', {'id': id})

def userNotice(request, id):
    notices = Notice.objects.filter(user_to = request.user.id).order_by('-created_at')
    count = notices.filter(checked = False).count()

    paginator = Paginator(notices, 7)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    page_numbers_range = 10
    max_index = len(paginator.page_range)
    current_page = int(page) if page else 1
    start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
    end_index = start_index + page_numbers_range
    
    if end_index >= max_index:
        end_index = max_index

    paginator_range = paginator.page_range[start_index:end_index]

    return render(request, 'accounts/user_notice.html', {'id': id, 'notices':notices, 'count':count,
                        'posts': posts, 'paginator_range': paginator_range })


def id_overlap_check(request):
    username = request.GET['username']
    try:
        # 중복 검사 실패
        user = User.objects.get(username=username)
    except:
        # 중복 검사 성공
        user = None
    if user is None:
        overlap_check = "pass"
    else:
        overlap_check = "fail"

    context = {'overlap_check': overlap_check}

    return JsonResponse(context)

def messageBox(request, id):
    num = User.objects.latest('id').id
    lastmessages = list()

    for i in range(1, num+1):
        if ( i != id):
            if Message.objects.filter(user_to_id = i, user_from_id = id).count() > 0 and Message.objects.filter(user_to_id = id, user_from_id = i).count() > 0:
                if Message.objects.filter(user_to_id = i, user_from_id = id).order_by('-created_at')[0].created_at < Message.objects.filter(user_to_id = id, user_from_id = i).order_by('-created_at')[0].created_at:
                    lastmessages.append(Message.objects.filter(user_to_id = id, user_from_id = i).order_by('-created_at')[0])
                else:
                    lastmessages.append(Message.objects.filter(user_to_id = i, user_from_id = id).order_by('-created_at')[0])
            elif Message.objects.filter(user_to_id = i, user_from_id = id).count() > 0 and Message.objects.filter(user_to_id = id, user_from_id = i).count() == 0:
                lastmessages.append(Message.objects.filter(user_to_id = i, user_from_id = id).order_by('-created_at')[0])
            elif Message.objects.filter(user_to_id = i, user_from_id = id).count() == 0 and Message.objects.filter(user_to_id = id, user_from_id = i).count() > 0:
                lastmessages.append(Message.objects.filter(user_to_id = id, user_from_id = i).order_by('-created_at')[0])

        

    return render(request, 'accounts/messagebox.html', {'id':id, 'lastmessages': lastmessages })

def chatRoom(request, id1, id2):
    messages = list()
    num = User.objects.latest('id').id
    lastmessages = list()
    friend = User.objects.get(id = id2).profile.nickname

    notices = Notice.objects.filter(user_to = request.user, feed = None)
    for notice in notices:
        notice.checked = True
        notice.save()

    for i in range(1, num+1):
        if Message.objects.filter(user_to_id = i, user_from_id = id1).count() > 0 and Message.objects.filter(user_to_id = id1, user_from_id = i).count() > 0:
            if Message.objects.filter(user_to_id = i, user_from_id = id1).order_by('-created_at')[0].created_at < Message.objects.filter(user_to_id = id1, user_from_id = i).order_by('-created_at')[0].created_at:
                lastmessages.append(Message.objects.filter(user_to_id = id1, user_from_id = i).order_by('-created_at')[0])
            else:
                lastmessages.append(Message.objects.filter(user_to_id = i, user_from_id = id1).order_by('-created_at')[0])
        elif Message.objects.filter(user_to_id = i, user_from_id = id1).count() > 0 and Message.objects.filter(user_to_id = id1, user_from_id = i).count() == 0:
            lastmessages.append(Message.objects.filter(user_to_id = i, user_from_id = id1).order_by('-created_at')[0])
        elif Message.objects.filter(user_to_id = i, user_from_id = id1).count() == 0 and Message.objects.filter(user_to_id = id1, user_from_id = i).count() > 0:
            lastmessages.append(Message.objects.filter(user_to_id = id1, user_from_id = i).order_by('-created_at')[0])
    
    for message in Message.objects.filter(user_to_id = id2, user_from_id = id1):
        messages.append(message)
    for message in Message.objects.filter(user_to_id = id1, user_from_id = id2):
        messages.append(message)

    return render(request, 'accounts/chatroom.html', {'chat_from': id1, 'chat_to':id2, 'lastmessages':lastmessages, 'messages': messages, 'friend' :friend })

def sendMessage(request, id1, id2):
    content = request.POST['content']
    Message.objects.create(user_to_id = id2, user_from_id = id1, content =content)
    Notice.objects.create(user_to_id = id2, user_from_id = id1, type_info1='쪽지')
    return redirect('chatroom', id1=id1, id2=id2)

