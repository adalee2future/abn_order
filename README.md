## 异常交易监控日报

功能实现: 下载dtquery发送的excel邮件，读取excel, 计算，绘图，生成报表，发邮件。

注：发邮件功能只能在公司网络内网（如eleme-staff、VPN）里实现。

## 使用

```
# 准备，只需第一次
echo 0 > max_mail.id # 设置上次最新邮件id
mkdir data # 用于放下载的数据
mkdir cached # 用于放数据缓存
mkdir output # 用于放生成的html文件
mkdir log # 用于放代码运行日志
# 设置邮箱以及密码
cat << EOF >> ~/.profile
export mail_user="xxx@ele.me"
export mail_passwd="xxxxxxx"
EOF
# 跑昨日日报
./run.ksh
# 跑20170315日报
./run.ksh 20170315
# 跑昨日日报并发log
./abn_ord_dly
```

### 自定义日期，收件人

* 默认日期: 昨天； 设定日期20170315，如 `./run.ksh 20170315`
* 收件人: 修改run.ksh中的to=, 多个收件人用逗号隔开

## 各个文件功能

* abn_order_daily2.Rmd 产生日报正文
* abn_ord_dly_app.Rmd 产生日报细分异常明细表格
* abn_ord_dly_smy.Rmd 邮件正文，即日报摘要
* receivemail.py 收邮件，下载dtquery的邮件里的excel附件
* skipmail.py 用于优化收邮件，先skip掉已有邮件，然后再等待dtquery发送的excel
* generate_report.ksh 跑3个Rmd文件
* sendmail.py 发送日报
* sendlog.py 程序跑完自动发送log给自己
* style.css 日报正文以及明细的css配置
* style2.css 日报邮件正文的css配置
* run.ksh 把流程串起来，收数据，产生日报，发邮件
* abn_ord_dly 跑run.ksh，并把log发给自己
