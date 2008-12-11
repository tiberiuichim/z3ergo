from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile

class BookView(object):
    
    def bookinfo(self):
        return "Title: %s, Author: %s, Publisher: %s" % (
                    self.context.title,
                    self.context.author,
                    self.context.publisher)


class BookAddPage(object):
    template = ViewPageTemplateFile('add.pt')
    
    def __call__(self):
        if 'submit' in self.request.form:
            f = self.request.form
            b = Book()
            b.title, b.author, b.publisher = (
                                              f['title'], 
                                              f['author'], 
                                              f['publisher']
                                              )
            self.context[self.__new_id()] = b
        else:
            return self.template()
        

    def __new_id(self):
        i = 0
        while True:
            if self.context.get(str(i), None) is not None:
                i += 1
                continue
            else:
                return str(i)