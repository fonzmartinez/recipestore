from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe   
from django.contrib.auth.mixins import LoginRequiredMixin  
from .forms import RecipeSearchForm
import pandas as pd
from .utils import get_recipename_from_id, get_chart

      
# Create your views here.
def home(request):
   return render(request, 'recipes/recipes_home.html')

class RecipeListView(LoginRequiredMixin, ListView):           
   model = Recipe                        
   template_name = 'recipes/main.html'   

class RecipeDetailView(LoginRequiredMixin, DetailView):                     
   model = Recipe                                    
   template_name = 'recipes/detail.html'       


def records(request):
   form = RecipeSearchForm(request.POST or None)
   recipes_df=None
   chart = None

   #check if the button is clicked
   if request.method =='POST':
       #read recipe_name and chart_type
       recipe_name = request.POST.get('recipe_name')
       chart_type = request.POST.get('chart_type')

       #apply filter to extract data
       qs =Recipe.objects.filter(recipe_name=recipe_name)
       if qs:      #if data found
           #convert the queryset values to pandas dataframe
           recipes_df=pd.DataFrame(qs.values()) 

           #convert the ID to Name of book
           recipes_df['recipe_id']=recipes_df['recipe_id'].apply(get_recipename_from_id)

           chart=get_chart(chart_type, recipes_df, labels=recipes_df['recipe_name'].values)

           #convert the dataframe to HTML
           recipes_df=recipes_df.to_html()

       #display in terminal - needed for debugging during development only
       print (recipe_name, chart_type)


       print ('Exploring querysets:')
       print ('Case 1: Output of Recipe.objects.all()')
       qs=Recipe.objects.all()
       print (qs)

       print ('Case 2: Output of Recipe.objects.filter(recipe_name=recipe_name)')
       qs =Recipe.objects.filter(recipe_name=recipe_name)
       print (qs)

       print ('Case 3: Output of qs.values')
       print (qs.values())

       print ('Case 4: Output of qs.values_list()')
       print (qs.values_list())



   #pack up data to be sent to template in the context dictionary
   context={
           'form': form,
           'recipes_df': recipes_df,
           'chart': chart
   }

   #load the recipes/record.html page using the data that you just prepared
   return render(request, 'recipes/records.html', context)
