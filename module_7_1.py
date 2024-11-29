from pprint import pprint

class Product :
    def __init__(self,name,weight,category):
        self.name = name
        self.weight = float(weight)
        self.category = category

    def __str__(self):
        return f'{self.name} ,{self.weight} ,{self.category}'


class Shop :
    __file_name = 'products.txt'
    file = open(__file_name,'w')
    file.close()

    def get_products(self) :
        file = open(self.__file_name,'r')
        list_product = file.read()
        file.close()
        return list_product

    def add(self,*products):
        str_product = self.get_products()
        for product in products:
            if product.name in str_product :
                print(f'Продукт {product.name} уже в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'{product}\n')
                file.close()


s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')

p2 = Product('Spaghetti', 3.4, 'Groceries')

p3 = Product('Potato', 5.5, 'Vegetables')



print(p2)



s1.add(p1, p2, p3)
s1.add(p1, p2, p3)



print(s1.get_products())