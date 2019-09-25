class Book:
    
    book_kinds = ('Программирование', 'Кулинария', 'Эзотерика') 
        
    def __init__(self, name, pages, kind, feature):
        
        if kind not in Book.book_kinds:
            print('ERROR: Books kind' + kind + ' does not exist!')           
        else:
            self.name = name
            self.pages = pages
            self.kind = kind
            self.feature = feature
           
    def __eq__(self, other):
        return (self.name, self.kind, self.feature, self.pages) == \
    (other.name, other.kind, other.feature, other.pages)
    
    def __lt__(self, other):
        return (Book.book_kinds.index(self.kind), self.name, self.pages, self.feature) \
    < (Book.book_kinds.index(other.kind), other.name, other.pages, other.feature)
    
    def __gt__(self, other):
        return (Book.book_kinds.index(self.kind), self.name, self.pages, self.feature) \
    > (Book.book_kinds.index(other.kind), other.name, other.pages, other.feature)
    
    def __repr__(self):
        return "Книга ({0}, {1}): {2}. {3} стр.".format(self.kind, self.feature,
                                                          self.name, self.pages)
        
        
class Disc:
    
    types = ('CD', 'DVD')
    content = ('Музыка', 'Видео', 'Программы')
        
    def __init__(self, name, dtype, content):
        if dtype not in Disc.types:
            print('ERROR: Disk type must be CD or DVD!')   
        else:
            if content not in Disc.content:
                print('ERROR: Wrong content category!')  
            else:
                self.name = name
                self.dtype = dtype
                self.content = content     
    
    def __eq__(self, other):
        return (self.name, self.dtype, self.content) ==  (
                                       other.name, other.dtype, other.content)
        
    def __lt__(self, other):
        ord1_self = Disc.types.index(self.dtype)
        ord2_self = Disc.content.index(self.content)
        ord1_other = Disc.types.index(other.dtype)
        ord2_other = Disc.content.index(other.content)
        return (ord1_self, ord2_self,self.name) < \
                (ord1_other, ord2_other, other.name)
                
    def __gt__(self, other):
        ord1_self = Disc.types.index(self.dtype)
        ord2_self = Disc.content.index(self.content)
        ord1_other = Disc.types.index(other.dtype)
        ord2_other = Disc.content.index(other.content)
        return (ord1_self, ord2_self,self.name) > \
                (ord1_other, ord2_other, other.name)
                
                
    def __repr__(self):
        return "Диск ({0}, {1}): {2}.".format(self.dtype, self.content,
                                                          self.name)
    

class Goods:
    
    categories = ('Book', 'Disc')
    
    def __init__(self, instance, price, barcode):
        if instance.__class__.__name__ not in Goods.categories:
            print('ERROR: Instance must be "Book" or "Disc"')
        else:
            self.name = instance.name
            self.price = price
            self.barcode = barcode
            self.instance = instance
        
    def __eq__(self, other):
        return (self.instance, self.barcode, self.price) == \
               (other.instance, other.barcode, other.price) \
               if self.__class__ == other.__class__ else False
        
    def __lt__(self, other):
        ord_self = Goods.categories.index(self.instance.__class__.__name__)
        ord_other = Goods.categories.index(other.instance.__class__.__name__)
        return (self.instance, self.barcode, self.price) > \
               (other.instance, other.barcode, other.price) \
               if ord_self == ord_other else ord_self < ord_other
                   
    def __gt__(self, other):
        ord_self = Goods.categories.index(self.__class__.__name__)
        ord_other = Goods.categories.index(ther.__class__.__name__)
        return (self.instance, self.barcode, self.price) > \
               (other.instance, other.barcode, other.price) \
               if ord_self == ord_other else ord_self > ord_other
    
    
    def __repr__(self):
            return repr(self.instance) + \
                    " цена: {0} руб. id={1}".format(self.price, self.barcode)
        

if __name__ == '__main__':
    
    import random as rnd
        
    #Список книг
    b = [Book("Рашид Абдульхабиб - Всё о плове", 122, 'Кулинария', 'Мясцо'),
         Book("Поваренная книга Анархиста", 322, 'Кулинария', 'Селитра'),
         Book("Идеальный код на крестах", 379, 'Программирование', 'C++'),
         Book("Древние языки", 666, 'Программирование', 'ALGOL'), 
         Book("Гороскопы", 219, 'Эзотерика', 45),
         Book("Некрономикон", 313, 'Эзотерика', 99)]
   
    # Список дисков    
    d = [Disc("Armik - Malaga", "CD", "Музыка"),
         Disc('Трилогия "Властелин колец" (full hd)', "CD", "Видео"),
         Disc('Windows 95', "CD", "Программы"),     
         Disc("Paco de Lucia - Greatest Hits", "DVD", "Музыка"),
         Disc('Операцыя "Ы"  и прочие шалости Шурика', "DVD", "Видео"),
         Disc('Kaspersky Resque Disc', "DVD", "Программы")]
    
    # goods - список товаров в случайном порядке
    rnd.seed(13)
    collection = b + d
    rnd.shuffle(collection)
     
    goods = []
    for item in collection:
        goods.append(Goods(item, rnd.randint(100, 1000), rnd.randint(100000,999999)))
    
    # Вывод списка товаров "как есть"
    print ("\n\t Исходный список товаров\n")
    for item in goods:
        print(item)
    
    # Вывод списка товаров по категориям
    print ("\n\t Упорядоченный список товаров\n")
    goods.sort(reverse=True)
    for item in goods:
        print(item)   
        
# Не реализованы исключения при некорректом определении экземпляра класса
# PEP-8
    
 

