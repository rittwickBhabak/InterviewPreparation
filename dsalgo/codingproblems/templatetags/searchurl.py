from django import template 

register = template.Library() 

# @register.filter(name="searchurl")
def searchurl(value):
    return value.replace(' ', '+')

register.filter('searchurl', searchurl)