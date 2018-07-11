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
        
        
 - 打包这个应用
 
 
        使用setuptools 来打包程序 使用pip 来安装这个应用。
        步骤
        1.首先，在你的 Django 项目目录外创建一个名为 django-polls 的文件夹，用于盛放 polls。
        2.将 polls 目录移入 django-polls 目录。
        3.创建一个名为 django-polls/README.rst 的文件，包含以下内容：
            :8000/polls/ to participate in the poll.=====
            Polls
            =====
            
            Polls is a simple Django app to conduct Web-based polls. For each
            question, visitors can choose between a fixed number of answers.
            
            Detailed documentation is in the "docs" directory.
            
            Quick start
            -----------
            
            1. Add "polls" to your INSTALLED_APPS setting like this::
            
                INSTALLED_APPS = [
                    ...
                    'polls',
                ]
            
            2. Include the polls URLconf in your project urls.py like this::
            
                path('polls/', include('polls.urls')),
            
            3. Run `python manage.py migrate` to create the polls models.
            
            4. Start the development server and visit http://127.0.0.1:8000/admin/
               to create a poll (you'll need the Admin app enabled).
            
            5. Visit http://127.0.0.1
        4.创建一个 django-polls/LICENSE 文件。选择一个非本教程使用的授权协议，但是要足以说明发布代码没有授权证书是 不可能的 。Django 和很多兼容 Django 的应用是以 BSD 授权协议发布的；不过，你可以自己选择一个授权协议。
          只要确定你选择的协议能够限制未来会使用你的代码的人。
        5.下一步我们将创建 setup.py 用于说明如何构建和安装应用的细节。
        关于此文件的完整介绍超出了此教程的范围，但是 setuptools docs 有详细的介绍。创建文件 django-polls/setup.py 包含以下内容：
                import os
                from setuptools import find_packages, setup

                with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
                    README = readme.read()
                
                # allow setup.py to be run from any path
                os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
                
                setup(
                    name='django-polls',
                    version='0.1',
                    packages=find_packages(),
                    include_package_data=True,
                    license='BSD License',  # example license
                    description='A simple Django app to conduct Web-based polls.',
                    long_description=README,
                    url='https://www.example.com/',
                    author='Your Name',
                    author_email='yourname@example.com',
                    classifiers=[
                        'Environment :: Web Environment',
                        'Framework :: Django',
                        'Framework :: Django :: X.Y',  # replace "X.Y" as appropriate
                        'Intended Audience :: Developers',
                        'License :: OSI Approved :: BSD License',  # example license
                        'Operating System :: OS Independent',
                        'Programming Language :: Python',
                        'Programming Language :: Python :: 3.5',
                        'Programming Language :: Python :: 3.6',
                        'Topic :: Internet :: WWW/HTTP',
                        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                    ],
                )
                          
        6.默认包中只包含 Python 模块和包。为了包含额外文件，我们需要创建一个名为 MANIFEST.in 的文件。上一步中关于 setuptools 的文档详细介绍了这个文件。为了包含模板、README.rst 和我们的 LICENSE 文件，
        创建文件 django-polls/MANIFEST.in 包含以下内容                 
                include LICENSE
                include README.rst
                recursive-include polls/static *
                recursive-include polls/templates *
        7. 在应用中包含详细文档是可选的，但我们推荐你这样做。创建一个空目录 django-polls/docs 用于未来编写文档。
           额外添加一行至 django-polls/MANIFEST.in
                recursive-include docs *
                recursive-include docs *
        
        8.试着构建你自己的应用包通过 ptyhon setup.py sdist （在 django-polls``目录内）。这将创建一个名为 ``dist 的目录并构建你自己的应用包， 
          django-polls-0.1.tar.gz。       
          提示：进入该文件目录下在运行该命令 
                 