# class FishiCakeMaker:
#     def __init__(self, param):
#         self._fish_name = param
#         pass

#     def show_name(self) :
#         print(self._fish_name)

# fish = FishiCakeMaker("붕어빵")
# fish.show_name()

class FishiCakeMaker:
    def __init__(self, **kwargs) :
        self._size = 10
        self._flavor = "팥"
        self._price = 100
        if "size" in kwargs:
            self._size = kwargs.get("size")
        if "flavor" in kwargs :
            self._flavor = kwargs.get("flavor")
        if "price" in kwargs :
            self._price = kwargs.get("price")

    # def show(self) :
    #     print("붕어빵 크기 {}".format(self._size))
    #     print("붕어빵 종류 {}".format(self._flavor))
    #     print("붕어빵 가격 {}".format(self._price))

# fish = FishiCakeMaker()
# fish1 = FishiCakeMaker(size=20, price=300)
# fish2 = FishiCakeMaker(size=30, price=500, flavor="초콜렛")

# fish.show()
# fish1.show()
# fish2.show()

class MarketGoods(FishiCakeMaker) :
    def __init__(self, margin=1000, **kwargs ):
        super.__init__(**kwargs)
        self._market_price = self._price + margin

    def show(self) :
        print(self._flavor, self._market_price)

fish1 = MarketGoods(size=20, price=500)
fish1.show()


