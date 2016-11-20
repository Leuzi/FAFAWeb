from . import models
from webLions.constants import *


class NewsManager():

	@classmethod
	def show_news(self, page=CPAGE, items=CITEMS):
		news = models.New.objects.all()

		start = (page-1)*items

		return news[start:(start+items)]
	
	@classmethod
	def show_new(self, slug):
		
		return models.New.objects.get(Slug=slug)
