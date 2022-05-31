
from modeltranslation.translator import translator, TranslationOptions
from product.models import Product,Category,ProductVersion

class ProductTranslationOptions(TranslationOptions):
 fields = ('title','description',)



class CategoryTranslationOptions(TranslationOptions):
 fields = ('title',)



class ProductVersionTranslationOptions(TranslationOptions):
 fields = ('title',)


translator.register(Product, ProductTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(ProductVersion, ProductVersionTranslationOptions)