# E-commerce-Multikart
![multikart image](multikart.png)


# class ImageExample(AbstractModel):
#     image = models.ImageField(upload_to = 'media/categories/')

#     class Meta:
#         verbose_name = 'Category'
#         verbose_name_plural = 'Categories'

# class Tag(AbstractModel):
#     title = models.CharField(max_length = 30, db_index = True)             

#     def __str__(self):
#         return self.title


# class Story(AbstractModel):
#     tags = models.ManyToManyField(Tag, through = 'StoryTag' )              many to many
#     author = models.ForeignKey(User, on_delete = models.Cascade )          one    to many

 new_product.main_version.product_id.get_absolute_url

 
class ImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductVersionAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

class ProductAdmin(admin.ModelAdmin):
    inlines = [ ImageInline, ProductVersionInline]

admin.site.register(Product, ProductAdmin)


# rsgplyanccjavxjk

