from django_filters import FilterSet
from .models import Product

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class ProductFilter(FilterSet):
    class Meta:
        # В Meta классе мы должны указать Django модель, в которой будем фильтровать записи.
        model = Product
        # В fields мы описываем по каким полям модели будет производиться фильтрация.
        fields = {
            'name': ['icontains'],  # поиск по названию
            'quantity': ['gt'],  # количество товаров должно быть больше или равно
            'price': ['lt', 'gt'],  # цена должна быть меньше/больше или равна указанной
        }

