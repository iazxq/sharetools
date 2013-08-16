# -*- coding: utf-8 -*-


class Page:
    '页面索引类'
    index = 0 #当前页面序号，比如 2表示第二页
    start = 0 #开始记录编号，比如25表示从第25条开始
    params = '' #url参数
    title = '' #显示标题，默认为索引编号

    def __init__(self,index,start,params,title=None):
        self.index = index
        self.start = start
        self.params = params
        self.title = str(index)
        if title:
            self.title = title


class Pager:
    '分页控件'
    total_count = 0  #总条数
    pages = [] #分页数组
    current_page = 1 #当前页
    page_size = 10 #每页数量
    split_page_count = 6 #最多连续显示的页数
    has_next_page = True #是否有下一页
    has_prev_page = True #是否有上一页
    prev_page = None #上一页页码
    next_page = None #下一页页码
    need_pager = True #是否需要分页
    request = None
    limit_page_count = 1000 #最大页数

    def __init__(self,request,start,page_size,total_count,split_page_count=6,limit_page_count=1000):

        self.total_count = int(total_count)
        self.limit_page_count = limit_page_count
        self.split_page_count = split_page_count

        if page_size:
            self.page_size = int(page_size)

        if start:
            self.current_page = start / self.page_size + 1

        if  self.total_count % self.page_size:
            max_page = self.total_count / self.page_size + 1
        else:
            max_page = self.total_count / self.page_size

        if max_page>limit_page_count:
            max_page = limit_page_count

        if self.split_page_count < 2:
            self.split_page_count = 2

        opages = list()

        pages = range(1,max_page+1)
        index_page = 0
        if self.current_page > self.split_page_count:#当前页码超过6页，先增加前两页，然后增加...然后增加当前页左侧的4页
            opages.extend(self.create_pages(request,pages[:2]))
            opages.extend([self.create_page(request,pages[self.current_page-self.split_page_count/2-1],title='...')])
            opages.extend(self.create_pages(request,pages[self.current_page-self.split_page_count/2:self.current_page]))
            index_page=self.current_page

            if index_page < max_page:
                if self.current_page + self.split_page_count < max_page: #当前页到最后一页超过6页,则需要增加...
                    opages.extend(self.create_pages(request,pages[index_page:self.current_page+self.split_page_count/2-1]))
                    opages.extend([self.create_page(request,pages[self.current_page+self.split_page_count/2-1],title='...')])
                    opages.extend(self.create_pages(request,pages[-2:]))
                else:
                    opages.extend(self.create_pages(request,pages[self.current_page:]))
        else: #当前页码在前10页范围内
            opages.extend(self.create_pages(request,pages[0:self.split_page_count+1])) #如果当前页超过了6页，则直接填充前10页
            index_page =self.split_page_count+1
            if index_page < max_page:
                if index_page + self.split_page_count < max_page: #当前页到最后一页超过6页,则需要增加...
                    opages.extend([self.create_page(request,pages[self.split_page_count+1],title='...')])
                    opages.extend(self.create_pages(request,pages[-2:]))
                else:
                    opages.extend(self.create_pages(request,pages[index_page:]))
        self.pages = opages

        #上一页
        self.has_prev_page = self.current_page > 1
        if self.has_prev_page:
            self.prev_page = Page(self.current_page-1,(self.current_page-2)*self.page_size,self.get_params(request,(self.current_page-2)*self.page_size))

        #下一页
        self.has_next_page = self.current_page < max_page
        if self.has_next_page:
            self.next_page = Page(self.current_page+1,self.current_page*self.page_size,self.get_params(request,self.current_page*self.page_size))

        self.need_pager = len(self.pages)>1 #判断是否需要分页

    def create_page(self,request,page,title=None):
        if not title:
            title = str(page)
        return Page(page,(page-1)*self.page_size,self.get_params(request,(page-1)*self.page_size),title=title)

    def create_pages(self,request,pages,title=None):
        '''
         根据page编号和尺寸返回page对象
        '''
        return map(lambda page: self.create_page(request,page,title=title) ,pages)

    def get_params(self,request,start):
        '返回带有分页表示的参数，格式 ?param1=test&param2=333'

        params_dict = request.GET.copy()
        if params_dict.has_key('start'):
            params_dict['start'] = start
        else:
            params_dict.setdefault('start',start)
        params = ''
        for k,v in params_dict.items():
            params += '%s=%s&'%(k,v)
        if params:
            params = '?' + params[:-1]
        return params
