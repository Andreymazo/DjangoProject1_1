from django import template
from catalog.models import Product
register = template.Library()

f = {
    "crab": "https://cdn.elebase.io/5d486d2e-87b2-401e-a93d-d0502e0d1a87/3869e9d5-c0a8-4250-8582-1dfa99af1e89-bah554d1fec2df8f02b0.jpg?w=680&h=382&fit=crop&rot=auto&dpr=2&q=75",

    "onion": "https://www.nicepng.com/png/detail/774-7744337_red-onion-fresh-onion.png",

    "lobster": "https://outerbanksthisweek.com/sites/default/files/business/6348/food-items/image-7-jimmys.jpg",

    "lemon": "https://i.pinimg.com/originals/f0/d8/a7/f0d8a7aedec7b6634da14684eb529518.jpg"
}
@register.filter()

@register.filter
def mediapath(text):
    print(str(text))
    return '' + str(text)

@register.simple_tag
def mediapath(text):
    print(str(text))
    return '' + str(text)

# def zamena_path(path):#path1 -j: path2 - preview
#     for i,j in f.items():
#         if i == Product.product_name and j == Product.preview:
#             return j
#         return path