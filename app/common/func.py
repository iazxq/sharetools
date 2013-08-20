# -*- coding: utf-8 -*-
import math,datetime,time,random,os,uuid,hashlib,base64
from sharetools import settings
from urlparse import urlparse
import traceback


#与业务相关的函数

def get_rating_text(rating):
    '根据评价数字返回评价文本'
    rating_dict = {
        '1' : '很差',
        '2' : '较差',
        '3' : '还行',
        '4' : '推荐',
        '5' : '力荐',
        }
    return rating_dict.get(repr(rating))


#根据时间撮创建唯一编号，方式：unix时间撮（单位毫秒） + 3位随机数
def create_new_id():
    return int(time.time()*1000*1000) + random.randint(100,999)

def format_date(date_time):
    '格式化日期输出'
    return date_time.strftime('%Y-%m-%d')

def format_date_time(date_time):
    '格式化日期、时间输出'
    return date_time.strftime('%Y-%m-%d %H:%M:%S')

def str_to_date(value):
    '字符串转换成日期格式'
    try:
        #如果传入的参数本身就是日期格式,则直接返回
        if isinstance(value,datetime.datetime):
            return value
        value = str(value)
        format="%Y-%m-%d"
        result = datetime.datetime.strptime(value,format)
        return result
    except:
        return None

def str_to_datetime(str_datetime):
    '字符串转换成日期格式'
    try:
        #如果传入的参数本身就是日期格式,则直接返回
        if isinstance(str_datetime,datetime.datetime):
            return str_datetime

        str_datetime = str(str_datetime)
        format="%Y-%m-%d %H:%M:%S"
        result = datetime.datetime.strptime(str_datetime,format)
        return result
    except:
        return datetime.datetime.now()


def get_int_param_from_post(request,param_name):
    '从request.POST获取整型参数'
    result = 0
    if param_name in request.POST:
        value = request.POST.get(param_name)
        if value.isdigit():
            result = long(value)
    return result

def get_int_param_from_get(request,param_name):
    '从request.GET获取整型参数'
    result = 0
    if param_name in request.GET:
        value = request.GET.get(param_name)
        if value.isdigit():
            result = long(value)
    return result

def get_str_param_from_post(request,param_name):
    '从request.POST获得字符串参数'

    #return request.POST.get(param_name,'').encode('utf-8')
    return request.POST.get(param_name,'')

def get_str_param_from_get(request,param_name):
    '从request.GET获得字符串参数'
    #return request.GET.get(param_name,'').encode('utf-8')
    return request.GET.get(param_name,'')

def get_referrer(request,default_url=''):
    if request.POST.get('referrer',None):
        return request.POST['referrer']

    '返回引用页'
    f = request.META.get('HTTP_REFERER','')
    if f:
        url = urlparse(f)
        return ''.join((url.path,'?',url.query))
    return  default_url

def check_referrer(request,referrer):
    '''检查指定的来源是否合法，如果来源为空或者来源就是当前url，则来源不合法'''
    return referrer and (referrer != request.get_full_path())


def get_url_from(request,default_url=''):
    f= get_str_param_from_get(request,'f')
    if f:
        return f
    return  default_url

def get_new_upload_dir():
    '创建新的上传目录,返回格式/2011/08/12'
    d = datetime.datetime.now()
    return d.strftime('%Y/%m/%d/')


def get_new_filename(filename):
    '返回新的文件名,利用Unix时间戳'
    f,ext=os.path.splitext(filename)
    return '%s%s%s'%(int(float(time.time()*1000)),random.randint(0,99),ext)


def get_new_upload_file_info(file):
    '''
    根据已有文件信息返回上传文件信息
    '''
    #获取上传文件的相对路径信息
    path= get_new_upload_dir()
    #获取上传文件的真实路径信息
    real_path = os.path.join(settings.STATIC_ROOT,settings.UP_DIR,path).replace('\\','/')
    #如果真实路径不存在,则创建
    if not os.path.exists(real_path):
        os.makedirs(real_path)
        #获取新文件名称
    filename = get_new_filename(file)
    #获取新文件的相对路径及名称
    new_file = os.path.join(path,filename).replace('\\','/')
    #小图片相对路径
    small_new_file = os.path.join(path,'s' + filename).replace('\\','/')
    #中图片相对路径
    middle_new_file = os.path.join(path,'m'+filename).replace('\\','/')
    #获取新文件的绝对路径及名称
    real_file = os.path.join(settings.UP_DIR,new_file).replace('\\','/')
    #小图片绝对路径
    small_real_file = os.path.join(settings.UP_DIR,small_new_file).replace('\\','/')
    #中图片绝对路径
    middle_real_file = os.path.join(settings.UP_DIR,middle_new_file).replace('\\','/')

    new_file = settings.UP_URL + new_file
    middle_new_file = settings.UP_URL + middle_new_file
    small_new_file = settings.UP_URL + small_new_file


    return {
        'new_file' : new_file,
        'real_file' : real_file,
        'small_new_file':small_new_file,
        'small_real_file':small_real_file,
        'middle_new_file':middle_new_file,
        'middle_real_file':middle_real_file
        }

def array_to_str(value,split_str='/'):
    '数组转换成'
    result = ''
    if value:
        for s in value:
            result += s + split_str
        result = result[:-1]
    return result

def format_content(str):
    return str.replace("\n","<br/>")


def get_uuid():
    return str(uuid.uuid1())

def get_hash_code(value,sign='7788521'):
    '''返回加入了干扰码的md5'''
    return hashlib.new('md5',value+sign).hexdigest()

def get_exec_time(func,*arg,**argv):
    '''返回函数的执行时间'''
    startTime = datetime.datetime.now()
    func(*arg,**argv)
    endTime = datetime.datetime.now()
    return (endTime-startTime).total_seconds()


def base64_url_encode(value):
    '''base64基于url安全的加密函数'''
    value=value.encode(encoding="utf-8")
    return base64.urlsafe_b64encode(value)


def base64_url_decode(value):
    '''base64基于url安全的解密函数'''
    try:
        value = str(value)
        result= base64.urlsafe_b64decode(value)
        result = unicode(result,'utf-8')
        return result
    except:
        print(traceback.format_exc())
        return None

def fill_id(id,length):
    '''自动填充id到指定的长度'''
    idLength = len(str(id))
    if idLength>length:
        return str(id)
    else:
        return '0'*(length-idLength) + str(id)

def getClientIp(request):
    '''得到客户端的ip地址'''
    try:
        real_ip = request.META['HTTP_X_FORWARDED_FOR']
        regip = real_ip.split(",")[0]
    except:
        try:
            regip = request.META['REMOTE_ADDR']
        except:
            regip = ""
    return regip

def GetIPLocation(ip):
    result = ''
    try:
        import urllib2
        import json
        url = 'http://ip.taobao.com/service/getIpInfo.php?ip=%s'%ip
        content = urllib2.urlopen(url)
        data = json.load(content,encoding='utf-8')
        if data.get('code',None) == 0:
            result = '%s %s %s %s'%(data['data'].get('country',''),data['data'].get('region',''),data['data'].get('city',''),data['data'].get('isp',''))
    except:
         pass
    return result

if __name__ == '__main__':
    print(base64_url_encode('http://www.bandao.cn'))
    print(base64_url_decode('L3VwLzIwMTMvMDQvMjEvMTM2NjU0ODgxNDQxOTE0LmpwZw=='))
    print(str_to_date('2013-08-18'))








