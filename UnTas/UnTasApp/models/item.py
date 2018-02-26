from django.db import models

class Item(models.Model):

	#choices used to define the state of a product 
	#https://docs.djangoproject.com/en/2.0/ref/models/fields/ section choices
	PERFECT_STATE = 'PS'
	LIGHTLY_DAMAGED = 'LD'
	HEAVLY_DAMAGED = 'HD'
	PRODUCT_LOSS = 'PL'

	PRODUCT_STATE_CHOICES = (
		(PERFECT_STATE, 'perfect state'),
		(LIGHTLY_DAMAGED, 'lightly damaged'),
		(HEAVLY_DAMAGED, 'heavly damaged'),
		(PRODUCT_LOSS, 'product loss'),
		)

	category_id	= models.ForeignKey(ItemCategory, on_delete=models.SET_NULL)
	code	= models.CharField(max_length=100, default='NO_CODE')
	name	= models.CharField(max_length=100, default='NO_NAME')
	price	= models.IntegerField(default=0)
	colors 	= models.CharField(max_length=100, null=True)
	image	= models.ImageField(null=True) #check how it specifically works
	state	= models.CharField(max_length=100, choices=PRODUCT_STATE_CHOICES, default=PERFECT_STATE)