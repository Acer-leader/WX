# Django
- https://docs.djangoproject.com/zh-hans/2.0/intro/tutorial01/  官方文档
- 验证是否已经安装了Django 和运行着的版本号
    
        python -c "import django; print(django.get_version()
        python -m django --version   //查看版本号
- 创建一个项目

        jango-admin.py startproject <name>
        #<name>  项目名称
        
        mysite/
                manage.py
                mysite/
                        __init__.py
                        settings.py
                        urls.py
                        wsgi.py
                     
- 更换端口

        python manage.py runserver 8080 
        #如果要更换你的端口，切换到8080 只需要这样即可
       
               
- 运行项目

        python manage.py runserver 
        
        
        #若出现下面情况说明运行成功
        
        Performing system checks...
        0 errors found
        May 13, 2015 - 15:50:53
        Django version 1.8, using settings 'mysite.setting
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CONTROL-C.
        
        
- 创建你的应用

        python manage.py startapp <name>
        #创建一个app 省去额外的创建
        
        目录结构如下：
        polls/
            __init__.py
            models.py
            tests.py
            views.py
- 激活模型
        
        python manage.py sql polls  #1.8
        python manage.py makemigrations polls      #2.0

        poll = models .ForeignKey(Poll,on_delete=models.CASCADE)
        #Django2.0一定要把 on_delete=models.CASCADE 这个参数加上 不然报错
        


