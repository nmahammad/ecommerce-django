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
