php-redis-admin 安装

NOTE: 在nginx上配置php-redis-admin尝试了只执行第8步就成功
1. 安装phpize
$ sudo apt-get install php5-dev

2. 安装 pecl
$ sudo apt-get install php-pear

3.
$ sudo pecl install igbinary

4. 下载代码
git clone git@github.com:nicolasff/phpredis.git

5. 编译
cd phpredis
./config
./configure --enable-redis-igbinary
make && make install

6. 在/etc/php5/conf.d目录下添加redis.ini文件

$ cat redis.ini
extension=redis.so

7. 重启apapche2服务

8. 下载php-redis-admin代码

git clone https://github.com/ErikDubbelboer/phpRedisAdmin.git /var/www
cd /var/www/phpRedisAdmin
git clone https://github.com/nrk/predis.git vender

访问http://localhost:8080/phpRedisAdmin查看效果


9. 配置
默认情况下，php-redis-admin只显示当前主机db 0下面的所有keys

通过复制phpRedisAdmin/config.sample.inc.php 为phpRedisAdmin/config.inc.php
可以配置要连接的redis数据库形式，多个db以及用户认证等。
如设置显示db 0 和 db 5 并设置访问用户
<pre>

<?php
//Copy this file to config.inc.php and make changes to that file to customize your configuration.

$config = array(
  'servers' => array(
    array(
      'name' => 'local server db 0', // Optional name.
      'host' => '127.0.0.1',
      'port' => 6379,
      'filter' => '*',
      'db' => '0',


      // Optional Redis authentication.
      //'auth' => 'redispasswordhere' // Warning: The password is sent in plain-text to the Redis server.
    ),

    array(
      'name' => 'local server db 5', // Optional name.
      'host' => '127.0.0.1',
      'port' => 6379,
      'filter' => '*',
      'db' => '5',


      // Optional Redis authentication.
      //'auth' => 'redispasswordhere' // Warning: The password is sent in plain-text to the Redis server.
    ),

    /*array(
      'host' => 'localhost',
      'port' => 6380
    ),*/

    /*array(
      'name' => 'local db 2',
      'host' => 'localhost',
      'port' => 6379,
      'db'   => 1 // Optional database number, see http://redis.io/commands/select
      'filter' => 'something:*' // Show only parts of database for speed or security reasons
      'seperator' => '/', // Use a different seperator on this database
      'flush' => false, // Set to true to enable the flushdb button for this instance.
      'encoding' => 'cp1251', // Set for view values in other encoding
    )*/
  ),


  'seperator' => ':',


  // Uncomment to show less information and make phpRedisAdmin fire less commands to the Redis server. Recommended for a really busy Redis server.
  //'faster' => true,


  // Uncomment to enable HTTP authentication
  'login' => array(
    // Username => Password
    // Multiple combinations can be used
    'admin' => array(
      'password' => 'admin',
    ),
    'guest' => array(
      'password' => '',
      'servers'  => array(1) // Optional list of servers this user can access.
    )
  ),


  // You can ignore settings below this point.

  'maxkeylen'           => 100,
  'count_elements_page' => 100
);

?>
</pre>
