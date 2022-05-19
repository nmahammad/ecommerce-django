
from modeltranslation.translator import translator, TranslationOptions
from product.models import Product,Category,ProductVersion

class ProductTranslationOptions(TranslationOptions):
 fields = ('description','title')



class CategoryTranslationOptions(TranslationOptions):
 fields = ('title',)



class ProductVersionTranslationOptions(TranslationOptions):
 fields = ('title',)


translator.register(Product, CategoryTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(ProductVersion, ProductVersionTranslationOptions)