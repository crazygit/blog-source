Title: Sentry搭建配置笔记
Date: 2013-12-25 17:05
Tags: sentry
Slug: sentry
Author: crazygit
Summary: how to set up sentry
comments: true
status: draft

Sentry:
http://sentry.readthedocs.org/en/latest/quickstart/index.html
Raven:
http://raven.readthedocs.org/en/latest/config/flask.html

环境:
Python 2.5, 2.6, or 2.7
python-setuptools, python-dev
A real database (PostgreSQL is preferred, MySQL also works)
A UNIX-based operating system

使用虚拟环境安装:
$ easy_install -UZ virtualenv
$ virtualenv /www/sentry/
$ source /www/sentry/bin/activate
$ easy_install -UZ sentry


数据库: 注意mysql数据库要用InnoDB引擎
PostgreSQL, MySQL(you should use InnoDB as your storage engine), sqlite
easy_install -UZ sentry[postgres]
easy_install -UZ sentry[mysql]

使用
$ sentry
usage: sentry [--config=/path/to/settings.py] [command] [options]
查看帮助: sentry --config=/etc/sentry.conf.py help

1. 创建配置文件
sentry init　/etc/sentry.conf.py

2. 按需修改配置文件

3. 数据库版本升级，如果是升级sentry， 可以通过下面的方式升级数据库
3.1. 创建数据库或创建数据库
执行下面的命令(注意：执行改命令时最好是使用mysql的超级用户，否则可能会看到很多错误)
sentry --config=/etc/sentry.conf.py upgrade
It’s very important that you create the default superuser through the upgrade process. If you do not, there is a good chance you’ll see issues in your initial install.

4. 创建用户
# create a new user
sentry --config=/etc/sentry.conf.py createsuperuser

# 设置sentry自己监视自己
# run the automated repair script
sentry --config=/etc/sentry.conf.py repair --owner=<username>

#　启动服务
# Sentry's server runs on port 9000 by default. Make sure your client reflects
# the correct host and port!
sentry --config=/etc/sentry.conf.py start


5. 在Nginx上设置反向代理

http {
  # we limit both on IP (single machine) as well as project ID
  limit_req_zone  $binary_remote_addr  zone=one:10m   rate=3r/s;
  limit_req_zone  $projectid  zone=two:10m   rate=3r/s;

  # limit_req_status requires nginx 1.3.15 or newer
  limit_req_status 429;

  server {
    listen   80;

    proxy_set_header   Host                 $http_host;
    proxy_set_header   X-Real-IP            $remote_addr;
    proxy_set_header   X-Forwarded-For      $proxy_add_x_forwarded_for;
    proxy_set_header   X-Forwarded-Proto    $scheme;
    proxy_redirect     off;

    location / {
      proxy_pass        http://localhost:9000;
    }

    location ~* /api/(?P<projectid>\d+/)?store/ {
      proxy_pass        http://localhost:9000;

      limit_req   zone=one  burst=3  nodelay;
      limit_req   zone=two  burst=10  nodelay;
    }

  }
}

6. 启用SSL(可选)
在sentry配置文件中添加:
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
如果在nginx中配置了反向代理，则还需要修改nginx的配置文件

8. sentry服务监控， 使用Supervisor配置
[program:sentry-web]
directory=/www/sentry/
command=/www/sentry/bin/sentry start http
autostart=true
autorestart=true
redirect_stderr=true

9. 默认情况下是开启了社交登录的认证方式，如果要禁用，可以在配置文件添加
SOCIAL_AUTH_CREATE_USERS = False

10. 缓存配置
You’ll also want to consider configuring cache and buffer settings, which respectively require a cache server and a Redis server. While the Django configuration covers caching in great detail, Sentry allows you to specify a backend for its own internal purposes:

# You'll need to install django-pyblibmc for this example to work
CACHES = {
    'default': {
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
        'LOCATION': 'localhost:11211',
    }
}

SENTRY_CACHE_BACKEND = 'default'
See [Update Buffers] <http://sentry.readthedocs.org/en/latest/buffer/index.html> for information on how to configure update buffers to improve performance on concurrent writes.

11. 一些配置信息
启动服务的如果出错，在配置文件中添加
ALLOWED_HOSTS=['*']

给网站添加URL前缀，方便做反向代理,修改
SENTRY_URL_PREFIX = 'http://sentry.example.com'

默认是允许用户注册的，禁用用户注册
SENTRY_ALLOW_REGISTRATION = False

12. Sentry同样支持Queuen,Buffer,Node Storage, Throttles and Rate Limiting.具体可以参看官方文档

13. 测试部署的环境:
安装raven:
$ pip install raven[flask]

raven test <DSN value>
其中DSN Value就是创建项目后的信息,形式如下:
dsn = 'http://public:secret@example.com/1'
如:

$ raven test 'http://70577ed46173408993dec1a96c47ffb1:4cf084e7765c4fdcbf66996c9127a251@localhost/2'
Using DSN configuration:
  http://70577ed46173408993dec1a96c47ffb1:4cf084e7765c4fdcbf66996c9127a251@localhost/2

Client configuration:
  servers        : ['http://localhost/api/2/store/']
  project        : 2
  public_key     : 70577ed46173408993dec1a96c47ffb1
  secret_key     : 4cf084e7765c4fdcbf66996c9127a251

Sending a test message...
success!
Event ID was 'cd20f499c7c74491a430cd7e9b26423f'








