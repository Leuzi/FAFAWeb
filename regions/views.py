from django.shortcuts import render
from FAFAWeb.constants import *
from regions import managers

def get_regions(self):

	regions = RegionManager.getAllRegions()
	
	return regions