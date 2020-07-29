from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from self import self
from django.db.models import Sum
from .models import users, CustomUser, Teacher, marks, Store, addres, resources, Document, guide
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from .forms import CustomUserCreationForm, DocumentForm


def add(request):
    return render(request, 'reg.html')


def saveteacher(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    dept = request.POST.get('dept')
    email = request.POST.get('email')
    mobile = request.POST.get('mobile')
    username = request.POST.get('username')
    password = request.POST.get('password')
    o = guide(fname=fname, lname=lname, department=dept, email=email, mobile=mobile, username=username,
              password=password)
    o.save()
    print('teachers reg saved')
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)


def nextuser(request):
    title2 = request.POST.get('title1')
    request.session['title2'] = title2
    fname2 = request.POST.get('fname1')
    lname2 = request.POST.get('lname1')
    no2 = request.POST.get('no1')
    email2 = request.POST.get('email1')
    domain2 = request.POST.get('domain1')
    request.session['domain2'] = domain2
    print(domain2)
    aca2 = request.POST.get('aca1')
    request.session['aca'] = aca2
    print(aca2)
    dept2 = request.POST.get('dept1')
    div2 = request.POST.get('div1')
    role2 = request.POST.get('role1')
    email3 = request.POST.get('email2')
    no3 = request.POST.get('no2')

    o_ref = users(title1=title2, fname1=fname2, lname1=lname2, no1=no2, email1=email2, dept1=dept2, div1=div2,
                  role1=role2,
                  email2=email3, no2=no3, domains=domain2, aca=aca2)
    o_ref.save()
    print('saved')
    ID = users.objects.filter(title1=title2)
    for i in ID:
        getdomain = i.domains
        print(getdomain)
        getaca = i.aca
        print(getaca)
        getdiv = i.div1
        print(getdiv)
        getdept = i.dept1
        print(getdept)
        savedid = getdomain + "" + getaca + "" + getdept + "" + getdiv
        request.session['savedid'] = savedid
        print(savedid)
    save = request.session['savedid']
    ss = users.objects.filter(domains=domain2).count()
    print(ss)
    mainid = savedid + "" + str(ss)
    request.session['mainid'] = mainid
    print(mainid)

    users.objects.filter(title1=title2).update(domainID=mainid)
    print('updated')

    name3 = users.objects.filter(fname1=fname2)
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)


def addnew(request):
    return render(request, 'addnew.html')


def saveaddnew(request):
    title2 = request.session['title2']
    domain3 = request.session['domain2']
    mainid3 = request.session['mainid']
    aca3 = request.session['aca']

    # id2 = request.POST.get('id1')
    fname2 = request.POST.get('fname1')
    lname2 = request.POST.get('lname1')
    no2 = request.POST.get('no1')
    email2 = request.POST.get('email1')

    dept2 = request.POST.get('dept1')
    div2 = request.POST.get('div1')
    role2 = request.POST.get('role1')

    o_ref = users(title1=title2, fname1=fname2, lname1=lname2, no1=no2, email1=email2, dept1=dept2, div1=div2,
                  role1=role2,
                  domains=domain3, aca=aca3, domainID=mainid3)
    o_ref.save()
    send_mail('Helloo from Mini-Project reg. System',
              ' You have registered succesfully, for mini_project of academic year ' + aca3 + ' and Your project name is : ' + title2 + ' and Your PROJECT ID : ' + mainid3,
              'systemproject472@gmail.com',
              [email2],
              fail_silently=False)
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)


def fetch(request):
    username = request.session['users']
    kk = guide.objects.filter(username=username)
    data = users.objects.filter(role1='leader')
    print(data)
    ss = guide.objects.all()

    return render(request, 'grpfinal.html', {'data': data, 'username': username, 'ss': ss, 'kk': kk})


def fetch2(request):
    return render(request, 'msg.html')


def fetchnext(request):
    title4 = request.POST.get('title3')
    name4 = request.POST.get('name3')
    item = users.objects.filter(title1=title4)
    for i in item:
        domainID = i.domainID
        tee = i.teacher1
        print(tee)
        request.session['domain'] = domainID
    urrr = users.objects.filter(teacher1=tee, role1='leader')
    for i in urrr:
        yname = i.teacher1
        print(yname)
    print(urrr)
    domain = request.session['domain']
    print(domain)
    gg = users.objects.filter(domainID=domain)
    o_ref = Teacher(Tname=title4, Ttopic=name4)
    o_ref.save()
    users.objects.filter(title1=title4).update(teacher1=name4)
    item = users.objects.filter(title1=title4)
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)


def fetchnext2(request):
    username = request.session['users']
    kk = guide.objects.filter(username=username)
    usr = request.session['username']
    data = users.objects.all()
    return render(request, 'showregdetails.html', {'data': data, 'usr': usr, 'kk': kk})


def fetchnext3(request):
    usr = request.session['users']
    kk = guide.objects.filter(username=usr)
    data = users.objects.filter(role1='leader')
    return render(request, 'showregdetails2.html', {'data': data, 'usr': usr, 'kk': kk})


def teacher(request):
    return render(request, 'teacherModule.html')


def treg(request):
    return render(request, 'guidereg.html')


def ss(request):
    username = request.POST.get('username')
    print(username)
    kk = users.objects.filter(teacher1=username, role1='leader')
    for i in kk:
        taketitle = i.title1
        print(taketitle)
        request.session['taketitle'] = taketitle

    taketitle = request.session['taketitle']

    request.session['username'] = username
    password = request.POST.get('password')

    user = guide.objects.filter(username=username, password=password)
    # if not request.user.is_authenticated:
    if user:
        Tdetails = guide.objects.filter(username=username)

        return render(request, 'teacherModule.html', {'Tdetails': Tdetails, 'taketitle': kk})
    else:
        return render(request, 'failedglogin.html', {'msg': 'Please enter correct username or password'})


def grp(request):
    username = request.session['username']
    kk = guide.objects.filter(email=username)
    print(username)
    lect = request.session['lect']
    print(lect)
    oo = users.objects.filter(title1=lect)
    return render(request, 'grpdetails.html', {'alldata': oo, 'kk': kk, 'lect': lect})


''' 
 alldata = users.objects.filter(teacher1=username, role1='leader')'''


def teamain(request):
    username = request.session['username']
    Tdetails = guide.objects.filter(username=username)
    lect = request.POST.get('gp')
    print(lect)
    request.session['lect'] = lect
    return render(request, 'teamain.html', {'Tdetails': Tdetails})


def nextgrp(request):
    username = request.session['username']
    kk = guide.objects.filter(email=username)
    alldata = users.objects.filter(teacher1=username)
    grpselect = request.POST.get('grp')
    rrs = users.objects.filter(title1=grpselect)
    for i in rrs:
        grpid = i.domainID
    rs = users.objects.filter(domainID=grpid)

    return render(request, 'grpdetails1.html',
                  {'rs': rs, 'username': username, 'alldata': alldata, 'select': grpselect, 'kk': kk})


def allocate(request):
    username = request.session['username']
    print(username)
    alldata = users.objects.filter(teacher1=username)
    return render(request, 'allocategrp.html', {'alldata': alldata})


def marks2(request):
    gp = request.POST.get('group')
    request.session['gpname'] = gp
    fetchgrp = users.objects.filter(title1=gp)

    return render(request, '', {'Item': fetchgrp})


def check(request):
    getname = request.POST.getlist('1')
    gpname = request.session['gpname']
    s = request.POST.get('2')
    saveintomarks = marks(name=gpname, count=getname, new=s)
    saveintomarks.save()
    filterdoc = marks.objects.filter(name=gpname)
    print(filterdoc)

    # op = marks.objects.filter(name=gpname).aggregate(to=Sum('count'))['to']
    # print(op)

    # return render(request, '', {'op': op})
    return render(request, '', {'op': filterdoc})


def bulk(request):
    name1 = request.POST.get('mod1')
    m1 = request.POST.get('smod1')

    p1 = request.POST.get('prio1')

    s1 = request.POST.get('status1')
    tea = request.session['teacher']
    ti = request.session['name']
    o = Store(mod=name1, smod=m1, priority=p1, status=s1, teacher=tea, title=ti)
    o.save()
    print('saved')
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)


def table(request):
    name = request.session['name']
    ss = Store.objects.filter(title=name)
    return render(request, 'table.html', {'tabledata': ss})


def updatetable(request):
    u = request.POST.get('mod')
    u1 = request.POST.get('smod')
    u2 = request.POST.get('prio')
    u3 = request.POST.get('status')
    print(u, u1, u2)
    Store.objects.filter(smod=u1).update(priority=u2, status=u3)

    return render(request, 'kupdated.html')


def up(request):
    smod = request.POST.get('smod2')
    prio2 = request.POST.get('prio1')
    status2 = request.POST.get('status1')
    Store.objects.filter(smod=smod).update(priority=prio2, status=status2)
    print('updated')
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)


def deletetable(request):
    u = request.POST.get('dname')
    a = 'NULL'
    if u != 'NULL':
        Store.objects.filter(smod=u).delete()
    else:
        Store.objects.filter(smod=a).update(name='Alert!!..Enter name')
    return render(request, 'oupdated.html')


def submodule(request):
    c = request.POST.get('s')
    print(c)
    return render(request, 'bulk.html', {'count': c})


def tracking(request):
    username = request.session['username']
    lect = request.session['lect']
    kk = guide.objects.filter(username=username)
    '''
        ss = users.objects.filter(teacher1=username)
        for i in ss:
            title = i.title1
            print(title)
            request.session['title'] = title
        title = request.session['title']
        store = Store.objects.filter(title=title)
        alldata = users.objects.filter(teacher1=username, role1='leader')'''
    nn = Store.objects.filter(title=lect)
    return render(request, 'track.html', {'kk': kk, 'lect': lect, 'nn': nn})


def loguser(request):
    return render(request, 'userloginpage.html')


''' for user login'''
from django.contrib import messages
from django.contrib import messages
from django.contrib import messages

from django.template import loader


def loggedin(request):
    if request.method == 'POST':
        username = request.POST.get('username1')
        request.session['usr'] = username
        password = request.POST.get('password1')
        fetchusername = users.objects.filter(email2=username, no2=password)

        for i in fetchusername:
            uname = i.fname1
            lname = i.lname1
            if i.email2 == username:
                return render(request, 'logcomplete.html', {'use': username, 'uname': uname, 'lname': lname})
        else:
            return render(request, 'failedulogin.html', {'msg': 'Please enter correct username or password'})


def forgot1(request):
    return render(request, 'uverification.html')


def forgot2(request):
    return render(request, 'uverification.html')


def verify1(request):
    getemail = request.POST.get('email1')
    request.session['setemail'] = getemail
    getno = request.POST.get('mobile1')

    vv = users.objects.filter(email1=getemail, no1=getno)
    if vv:
        return render(request, 'newpassword.html')
    else:
        return render(request, 'verifailed.html', {'msg': 'Entered email or mobile-number is not registered'})


def verify2(request):
    getemail = request.POST.get('email1')
    request.session['setemail'] = getemail
    getno = request.POST.get('mobile1')

    vv = guide.objects.filter(username=getemail, password=getno)
    if vv:
        return render(request, 'newpassword.html')
    else:
        return render(request, 'verifailed.html', {'msg': 'Entered email or mobile-number is not registered'})


def verifailed(request):
    return HttpResponseRedirect('/forgot1')


def newpass1(request):
    newpass11 = request.POST.get('pass1')
    print(newpass11)
    newpass22 = request.POST.get('pass2')
    print(newpass22)
    getmail = request.session['setemail']
    print(getmail)
    if newpass11 == newpass22:
        guide.objects.filter(username=getmail).update(password=newpass22)
        users.objects.filter(email2=getmail).update(no2=newpass22)
        print('updated')
        return render(request, 'showmsg1.html', {'msg': 'Your new password is ' + newpass22})
    else:
        return render(request, 'showmsg.html', {'msg': 'password are not matched..please enter again'})


def login1(request):
    return HttpResponseRedirect('/userloginpage.html')


def login2(request):
    return HttpResponseRedirect('/guidelogin.html')


def tr(request):
    return HttpResponseRedirect('/userloginpage.html')


def trg(request):
    return HttpResponseRedirect('/guidelogin.html')


def tra(request):
    return HttpResponseRedirect('/adminlogin.html')


def dele(request):
    delet = request.POST.get('sdel')
    print(delet)
    Store.objects.filter(smod=delet).delete()
    delet = request.POST.get('del')
    print(delet)
    Store.objects.filter(mod=delet).delete()
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)


def check1(request):
    username = request.session['usr']
    print(username)
    trackdata1 = users.objects.filter(email1=username)
    for i in trackdata1:
        name = i.title1
        teacher = i.teacher1
        domain = i.domainID
        print('name is =' + name + 'teacher is =' + teacher)
        request.session['name'] = name
        request.session['teacher'] = teacher
        request.session['domain'] = domain
    domain = request.session['domain']
    domain2 = request.session['teacher']
    members = users.objects.filter(domainID=domain)
    tea = guide.objects.filter(email=domain2)
    jj = Store.objects.filter(title=name)
    return render(request, 'bulk.html', {'trackdata': trackdata1, 'jj': jj, 'members': members, 'tea': tea})


def done(request):
    username = request.session['usr']
    print(username)
    tra = users.objects.filter(email1=username, role1='leader')
    for i in tra:
        teacher = i.teacher1
        tii = i.title1
        request.session['teacher'] = teacher
    domain2 = request.session['teacher']
    kk = guide.objects.filter(email=domain2)
    for i in kk:
        getemail = i.email
        de = i.degree
        f = i.fname
        l = i.lname
        send_mail('Hello,' + de + '' + f + '' + l + '',
                  'Your Project group ' + tii + ' recently made a updations ...Please check it out.',
                  'systemproject472@gmail.com',
                  [getemail],
                  fail_silently=False)

    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)


def mainpage(request):
    return render(request, 'mainpage.html')


def tlogin(request):
    return render(request, 'tlogin.html')


def adminlogin(request):
    return render(request, 'adminlogin.html')


''' admin login '''


def adminlogged(request):
    usrname = request.POST.get('usr')
    request.session['users'] = usrname
    passi = request.POST.get('pass')
    usr = request.session['users']
    kk = guide.objects.filter(username=usr)
    logged = guide.objects.filter(username=usrname, password=passi)
    for i in logged:
        username = i.username
        password = i.password
        if username == usrname and password == passi:
            return render(request, 'msg.html', {'usrname': usrname, 'kk': kk})
    else:
        return render(request, 'failedalogin.html', {'msg': 'Please enter correct username or password'})


def updatetracker(request):
    return render(request, 'logcomplete.html')


def senddata(request):
    username = request.session['usr']
    print(username)
    klkl = users.objects.filter(email1=username)
    for i in klkl:
        name = i.domainID
        proname = i.title1
        j = i.fname1
        k = i.lname1
        request.session['proname'] = proname
        request.session['name'] = name
    name = request.session['name']
    proname = request.session['proname']
    ff = users.objects.filter(domainID=name)
    return render(request, 'senddata.html', {'ff': ff, 'username': username, 'proname': proname, 'j': j, 'k': k})


def all(request):
    username = request.session['usr']
    print(username)
    dd = users.objects.filter(email1=username, role1='leader')
    for i in dd:
        tname = i.teacher1
        request.session['tname'] = tname
        print(tname)
    tname = request.session['tname']
    if tname != 'True':
        oo = guide.objects.filter(email=tname)
        for i in oo:
            fname = i.fname
            request.session['fname'] = fname
            fname = request.session['fname']
            jj = guide.objects.filter(fname=fname)
            return render(request, 'all.html', {'jj': jj, 'dd': dd})
    else:
        print('username is True')
        msg = 'SORRY, Teacher is not allocated for your project group'

    return render(request, 'all.html', {'msg': msg})


def manageresources(request):
    usr = request.session['users']
    kk = guide.objects.filter(username=usr)

    ff = addres.objects.all()

    return render(request, 'manager.html', {'ff': ff, 'kk': kk})


def addr(request):
    addr = request.POST.get('addr')
    nor = request.POST.get('nor')
    a = addres(type1=addr, nor=nor)
    a.save()
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)


def mm(request):
    ff = addres.objects.all()
    username = request.session['usr']
    kk = users.objects.filter(email1=username)
    for i in kk:
        kname = i.title1
        ll = i.fname1
        fff = i.lname1
        request.session['kname'] = kname
    n = range(1, 10)
    name = request.session['name']
    mml = resources.objects.filter(gname=name)
    return render(request, 'res.html', {'aa': username, 'ff': ff, 'kk': kk, 'n': n, 'mml': mml, 'll': ll, 'fff': fff})


def mmm(request):
    res = request.POST.get('res')
    qua = request.POST.get('qua')
    name = request.POST.get('sss')
    request.session['name'] = name
    print(res)
    print(qua)
    addd = resources(restype=res, resqua=qua, gname=name)
    addd.save()
    nn = resources.objects.filter(restype=res).aggregate(sum=Sum('resqua'))['sum']
    print('val')
    print(nn)
    ll = addres.objects.filter(type1=res)
    for i in ll:
        real = i.nor
    print(real)
    substract = real - nn
    addres.objects.filter(type1=res).update(nor=substract)
    print('sub=')
    print(substract)
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)


def low(request):
    uu = resources.objects.all()
    nn = resources.objects.filter(restype='dd').aggregate(Sum('resqua'))
    print(nn)
    return render(request, 'low.html', {'uu': uu})


def returned(request):
    op = resources.objects.filter(resqua=0)
    return render(request, 'returned.html', {'op': op})


def returnall(request):
    kname = request.session['kname']
    resources.objects.filter(gname=kname).update(resqua=0)
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)


def sendmail(request):
    username = request.session['usr']
    send_mail('Helloo from Mini Project manage system',
              'You have not submitted the issued resources...Please submit it.',
              'systemproject472@gmail.com',
              [username],
              fail_silently=False)
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)


def model_form_upload(request):
    usr = request.session['usr']
    jj = users.objects.filter(email1=usr)
    for i in jj:
        name = i.fname1
        lname = i.lname1

    print(usr)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            print('saved')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form, 'usr': usr, 'fname': name, 'lname': lname
    })


def xx(request):
    return render(request, 'ss.html')


def docs(request):
    username = request.session['username']
    lect = request.session['lect']
    kk = guide.objects.filter(email=username)

    usa = users.objects.filter(title1=lect, role1='leader')
    for i in usa:
        eee = i.email1
        request.session['eee'] = eee
    eee = request.session['eee']
    print(eee)
    dd = Document.objects.filter(username=eee)
    if usa:
        for i in usa:
            email = i.email1
            print(email)
            mm = Document.objects.filter(username=email)
            print('in docs')
            return render(request, 'docs.html', {'mm': mm, 'username': username, 'kk': kk})
    else:
        ss = "no documents uploaded"
        return render(request, 'docs.html', {'ss': ss, 'username': username, 'dd': dd})
