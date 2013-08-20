# -*- coding: utf-8 -*-
from django.template import Library
import datetime
import base64

register = Library()


def left_str(value,length):
    '从左边截取指定长度的字符串，一个中文算两个字符'

    try:
        value = value.decode('utf-8')
    except:
        pass

    if length <=0:
        return value

    result = ''

    value_byte_length = len(value.encode('GB18030'))

    # 如果编码后的字符串的长度还不到指定长度，则直接返回
    if value_byte_length<=length :
        return value



    cut_len = 0 #记录已截取长度
    for c in value:
        cut_len += len(c.encode('GB18030'))
        if cut_len <= length:
            result += c


    return result
register.filter(left_str)


def file_path(value):
    '反问文件相对路径'
    return '/up/%s'%value
register.filter(file_path)



def rating_to_star(value):
    '把平均得分转换成星星，例如10分=长度为50的星星'
    if not value:
        return 0
    return int(round(value * 5 /5,0) *5)
register.filter(rating_to_star)


def format_content(value):
    '格式化内容显示，替换换行符等'
    return value.replace("\n","<br/>").replace(" ","&nbsp")
register.filter(format_content)


def format_news(value):
    return value.replace("[page]","").replace('  ',u'　')
register.filter(format_news)


def format_date(date_time):
    '格式化日期输出'
    result = ''
    try:
        if isinstance(date_time,datetime.datetime):
            result =  unicode(date_time.strftime('%Y-%m-%d'))
    except:
        result = u''
    return result
register.filter(format_date)

def format_ymdate(date_time):
    '格式化日期输出'
    if isinstance(date_time,datetime.datetime):
        return  unicode(date_time.strftime('%Y-%m'))
    else:
        return ''
register.filter(format_ymdate)

def timezone_str_to_datetime(t):
    '''将带时区的日期字符串转换成python日期'''
    return datetime.datetime.strptime(t,'%Y-%m-%dT%H:%M:%S+08:00')
register.filter(timezone_str_to_datetime)

def format_pass_time(date_time):
    '输出日期格式为xx天前'
    import math
    span = datetime.datetime.now() - date_time
    seconds =  math.trunc(span.total_seconds())
    result = date_time
    print(seconds)
    if seconds<=60:
        return '1分钟前'
    if seconds <= 60*60:
        return '%s分钟前'%(seconds/60)
    if seconds <= 60*60*24:
        return '%s小时前'%(seconds/60/60)
    if seconds <= 60*60*24*365:
        if seconds/60/60/24==1:
            return '昨天'
        else:
            return '%s天前'%(seconds/60/60/24)
    if seconds > 60*60*24*365:
        return '%s年前'%(seconds/60/60/24/365)
    return result
register.filter(format_pass_time)



def get_state(state):
    state_dict = {0:'<font color=red>隐藏</font>',
                  1:'显示'}
    return state_dict.get(state,'未知')
register.filter(get_state)

def get_sms_state(state):
    '''获取消息是否读取的状态'''
    stateDict = {'unread':'<font color=red>未读</font>',
                 'readed':'已读'}
    return stateDict.get(state,'未知')
register.filter(get_sms_state)


def cut_by_space(value):
    return value.split(' ')[0]


def first_pic(pics,picType):
    '''从pics中获取第一个图片的大、中小图片，picType可以为spic,mpic,pic'''
    if pics:
        return pics[0][picType]
    else:
        return None
register.filter(first_pic)

def base64_url_encode(value):
    '''base64基于url安全的加密函数'''
    value=value.encode(encoding="utf-8")
    return base64.urlsafe_b64encode(value)
register.filter(base64_url_encode)

def get_percent(value,maxValue):
    return float(value)/maxValue*100
register.filter(get_percent)


if __name__ == "__main__":
    print(left_str(u'aab我们都是害虫333',12))
    print(format_pass_time(datetime.datetime.strptime('2011-07-23 1:10:01','%Y-%m-%d %H:%M:%S')))
    print(cut_by_space('helloworld'))