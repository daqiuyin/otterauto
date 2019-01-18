# otterauto
这个是基于chromedriver来实现的
主要用的函数是selenium
在Linux安装chromedirver要注意一下几点
1：options.add_argument('--no-sandbox')要有这个参数
2：driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver",chrome_options=options)指定在使用chromedriver并且chromedriver有x权限
3:在安装
