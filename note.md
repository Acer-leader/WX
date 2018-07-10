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
        
- Django-sqlmigrate命令接收一个迁移的名称
        
         python manage.py sqlmigrate polls 0001
         #会成为可读的创建数据表的模式

- 检查项目中出现的问题 

        python manage.py check
        
- 改变模型/model需要这三步：
        
        编辑 models.py 文件，改变模型。
        运行 python manage.py makemigrations 为模型的改变生成迁移文件。
        运行 python manage.py migrate 来应用数据库迁移。                      
- API 交互式的Python的命令行
    
        python manage.py shell
        #继续以下命令
        
        类似命令
        from polls.models import Choice, Question
        Question.objects.all()
        from django.utils import timezone
        q = Question(question_text="What's new?", pub_date=timezone.now())
        q.save()
        q.id
        q.question_text  等等
-  Django的管理页面
 
        python manage.py createsuperuser
        #创建超级管理员
        这里设置的密码是  admin ---- root123456  

- Django的命名空间以及视图
    
         在当下的url路由加上app_name=''即可，在html使用空间命名的时候只需要
         {%  url '<name>:<name>' %}
         
# 轻轻松松看张美女  链接速度太慢看不到美女

![image](https://github.com/then-on/WX/blob/master/Pic/1.jpg?raw=true) 
![image](https://github.com/then-on/WX/blob/master/Pic/2.jpg?raw=true)

      
- 测试 BUG
        
        一般在app页面下的tests.py 文件当中，命令是
        python manage.py test polls
        
- 后台的制作

         后面选项用这些代码表示 
         from .models import Question, Choice
         from django.contrib import admin
        # class ChoiceInline(admin.StackedInline):
        #     model = Choice
        #     extra = 3
        class ChoiceInline(admin.TabularInline):
            model = Choice
            extra = 0
        class QuestionAdmin(admin.ModelAdmin):
            fieldsets = [
                (None, {'fields': ['question_text']}),
                ('Date information', {'fields': ['pub_date']}),
            ]
            inlines = [ChoiceInline]
        admin.site.register(Question,QuestionAdmin)
        
        #extra = 3  表示的是 choice 后面的选项是3个字段
        通过 TabularInline``（替代 ``StackedInline ），关联对象以一种表格式的方式展示，显得更加紧凑：
        
- 过滤器

        过滤器，使用 list_filter。将以下代码添加至 QuestionAdmin：  
        list_filter = ['pub_date']           
        #根据 pub_date 这个时间来进行来查找 。这样做添加了一个“过滤器”侧边栏，允许人们以 pub_date 字段来过滤列表：
         
- 搜索框
        
        在列表的顶部增加一个搜索框。当输入待搜项时，Django 将搜索 question_text 字段。
        你可以使用任意多的字段——由于后台使用 LIKE 来查询数据，
        将待搜索的字段数限制为一个不会出问题大小，会便于数据库进行查询操作。
        admin/search_fields = ['question_text']

- 查看Django的源文件

        如果你不知道 Django 源码在你系统的哪个位置，运行以下命令：
        $ python -c "import django; print(django.__path__)"