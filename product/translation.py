from modeltranslation.translator import translator, TranslationOptions
from product.models import Product,Category,ProductVersion, PropertyValue

class ProductTranslationOptions(TranslationOptions):
 fields = ('title','description',)

class CategoryTranslationOptions(TranslationOptions):
 fields = ('title',)

class ProductVersionTranslationOptions(TranslationOptions):
 fields = ('title',)

# class PropertyValueTranslationOptions(TranslationOptions):
#  fields = ('name',)



translator.register(Product, ProductTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(ProductVersion, ProductVersionTranslationOptions)
# translator.register(PropertyValue, PropertyValueTranslationOptions)