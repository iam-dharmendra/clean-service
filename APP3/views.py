from math import e
from django import http
from django.contrib import messages
from django.shortcuts import redirect, render,get_object_or_404
from django.http import HttpResponse
from django.utils.functional import empty


from .models import mycart, user,clean,type,orders

import smtplib
from email.message import EmailMessage
import random
import razorpay
import datetime
# Create your views here.


def home(self):
    if 'email' in self.session:

        if self.POST:
            v=self.POST['search']
            if v!='':
                try:
                    o=clean.objects.filter(title__contains=str(v).lower())
                    return(redirect('service',o[0].id))
                    
                except:
                    return(HttpResponse('nothing found'))   
            
        obj=user.objects.get(email=self.session['email'])
        t=type.objects.all()
        c=clean.objects.filter(Category=2)
        h=clean.objects.filter(Category=1)
        
        return(render(self,'home.html',{'ob':obj,'c':c,'h':h,'t':t}))
    return(redirect(login))    

def logout(self):
    if 'email' in self.session:
        del self.session['email']
        return(redirect(login))

def login(self):
    if self.POST:       
        e=self.POST['Lemail']
        p=self.POST['Lpassword']

        try:
            obj=user.objects.get(email=e)
            if obj.password==p:
                self.session['email']=e
                return(redirect(home))
            else:
                return(HttpResponse(' enter valid password')) 
        except:
            return(HttpResponse('you dont have account with this email'))

    return(render(self,'loginpage.html'))

def register(self):
    if self.POST:
        n=self.POST['Rname']
        e=self.POST['Remail']
        p=self.POST['Rpassword']
        cnfp=self.POST['Cnfpassword']

        c=user.objects.filter(email=e)
        
        if c:
            return(HttpResponse('this email already taken try another email'))
       
        elif p==cnfp:
            iv=user()
            iv.username=n
            iv.email=e
            iv.password=p
            iv.save()

            return(redirect(login))
        
        else:
            return(HttpResponse('both  password not match '))                    
    
    return(render(self,'registerpage.html'))    

def otp_genrate(self):
        str=''
        for i in range(4):
            g=random.choice(['0','1','2','3','4','5','6','7','8','9'])
            str+=g
        print(str)    
        return(str)

def forgotpassword(self):   

    if self.POST:
        e=self.POST['femail']
        # o=self.POST['fotp']

        try:
            obj=user.objects.get(email=e)
        except:
            return(HttpResponse('please enter registered email '))
        if e == obj.email:
            self.session['user1']=e
            global k
            k=otp_genrate(self)

            # for sending otp on email id
            
            msg=EmailMessage()

            msg.set_content(f'''
            for reset your password on cleaning services
            your otp is {k} 
            ''')  
            msg['subject']='reset password'
            msg['From']='drtest789@gmail.com'
            msg['TO']=e
            print(e)
             # send message via our oen smtp server

            server=smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login('drtest789@gmail.com','Dharm789@')
            server.send_message(msg) 
            server.quit()

            return(redirect('otp'))
    return(render(self,'forgotpassword.html'))

def otp(self):
    if 'user1' in self.session:
        if self.POST:
            o=self.POST['fotp']
            if o==k:
                    
                return(redirect('changepassword'))
            else:
                return(HttpResponse('wrong otp'))        
        return(render(self,'otp.html'))    

def changepassword(self):
    if 'user1' in self.session:
        if self.POST:
            p=self.POST['cpass']
            cnfp=self.POST['Cnfpass']
            
            if p == cnfp :
                obj=user.objects.get(email=self.session['user1'])
                obj.password=p
                obj.save()
                del self.session['user1']
                return(redirect(login))    
            else:
                return(HttpResponse('both password not match'))
                
        return(render(self,'changepassword.html'))    

def servcie(self,p):
    obj=clean.objects.get(id=p)
    qty=1
    if 'psub' in self.POST:
        if '+' in self.POST.get('psub'):
            qty=int(self.POST['qty'])+1   
            
        else:
            qty=int(self.POST['qty'])
            if qty>1:
                qty=qty-1
                
    
    return(render(self,'spage.html',{'obj':obj,'qty':qty}))

def edit_cart_qunatity(self,d,s1):
        obj=user.objects.get(email=self.session['email'])
        g=mycart.objects.get(person=obj.pk,serv_id=d)
        print(g)
        n=g.quantity
        if s1=='+':
            g.quantity=n+1
            g.save()

        elif(n>1):
            g.quantity=n-1
            g.save()
            
        return(redirect('mycart'))


def addcart(self,d,s1):
    if 'email' in self.session:

        per=user.objects.get(email=self.session['email'])
        s=clean.objects.get(id=d)
    
        if mycart.objects.filter(person_id=per.pk,serv_id=s.id,status=False).exists():
            return(HttpResponse('this service already in your cart choose another one'))

        else:
            iv=mycart()
            iv.person=per
            iv.serv=s
            iv.quantity=int(s1)
            iv.date=datetime.datetime.now()
            iv.save()
    return(redirect('service',d))

def show_mycart(self):
  
    if 'email' in self.session:
        obj=user.objects.get(email=self.session['email'])
        all=mycart.objects.filter(person=obj.pk)
        l=[]
        q=[]
        p=0
        for i in all:
            l.append(i.serv)
            q.append(i)
            p=p+i.serv.price*i.quantity
        k=dict(zip(l,q))    
        return(render(self,'mycartpage.html',{'k':k,'n':obj,'p':p}))

def removecart(self,d):
    if 'email' in self.session:
        o=user.objects.get(email=self.session['email'])
        y=get_object_or_404(mycart,serv=d,person=o.pk)
        y.delete()
        return(redirect('mycart'))  



def cartorder(self):
         
    o=user.objects.get(email=self.session['email'])
    obj=mycart.objects.filter(person=o.pk)
    l=[]
    q=[]
    p=0
    s=''
    
    for i in obj:
        print('1')
        l.append(i.serv)
        q.append(i)
        s+=i.serv.title+"  id="+str(i.serv.id)+" Qunatity ="+str(i.quantity)+','
        p=p+i.serv.price*i.quantity
        
    
    if self.POST:
        
        n=self.POST['name']
        st=self.POST['state']
        ct=self.POST['city']
        ad=self.POST['address']
        pin=self.POST['pincode']
        ph=self.POST['phone']
        dat=self.POST['date']
    
        iv=orders()
        iv.oemail=self.session['email']
        iv.services=s
        iv.name=n
        iv.service_date=dat
        iv.placed_at=datetime.datetime.now()
        iv.contact=ph
        iv.amount=p
        iv.adddress=str(ad)+str(ct)+str(st)+'\n'+str(pin)
        
        amount=p
        client = razorpay.Client(
            # auth=("rzp_test_9nmrK825fjo0Ym", "1f1icPZDRCKvac3lzpOmLSl1"))
            auth=("rzp_test_EStipO5V3HYyYg","BBj3vCrCI2rG7DknExHIqDfT"))

        payment = client.order.create({'amount':amount*100, 'currency': 'INR',
                                       'payment_capture': '1'})
        iv.save()
        return(redirect('payment'))
    
    k=dict(zip(l,q))
    return(render(self,'orderpage.html',{'k':k,'p':p}))


def serviceorder(self,d,s):
    
    o=user.objects.get(email=self.session['email'])
    obj=clean.objects.get(id=d)
    l=[]
    q=[]
    l.append(obj)
    p=obj.price
    qty=int(s)
    q.append(qty)
    
                
    
    if self.POST:
    
        n=self.POST['name']
        st=self.POST['state']
        ct=self.POST['city']
        ad=self.POST['address']
        pin=self.POST['pincode']
        ph=self.POST['phone']
        dat=self.POST['date']
    
        iv=orders()
        iv.oemail=self.session['email']
        iv.services=obj.title+" id = "+str(d)+" Qunatity ="+s+','
        iv.name=n
        iv.service_date=dat
        iv.contact=ph
        iv.service_date=dat
        iv.placed_at=datetime.datetime.now()
        iv.amount=p*qty
        iv.adddress=str(ad)+str(ct)+str(st)+'\n'+str(pin)
        
        amount = p*qty

        client = razorpay.Client(
            # auth=("rzp_test_9nmrK825fjo0Ym", "1f1icPZDRCKvac3lzpOmLSl1"))
            auth=("rzp_test_EStipO5V3HYyYg","BBj3vCrCI2rG7DknExHIqDfT"))

        payment = client.order.create({'amount': amount, 'currency': 'INR',
                                       'payment_capture': '1'})
        
        iv.save()
        return(redirect('payment'))
    
    k=dict(zip(l,q))
    return(render(self,'orderpage.html',{'k':k,'p':p*qty,'qty':qty}))

def payment(self):
    obj=orders.objects.last()
    print(obj.amount,obj.adddress)
    return(render(self,'success.html'))