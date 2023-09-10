from django.test import TestCase
from .models import Recipe
from .forms import RecipeSearchForm

# Create your tests here.

class RecipeModelTest(TestCase):
    def setUpTestData():
        Recipe.objects.create(recipe_id='1', recipe_name='Pizza',
        ingredients='dough, cheese, pepperoni', cooking_time='5')

    def test_recipe_name(self):
        recipe = Recipe.objects.get(recipe_id=1)
        field_label = recipe._meta.get_field('recipe_name').verbose_name
        self.assertEqual(field_label, 'recipe name')

    def test_recipe_name_max_length(self):
          recipe = Recipe.objects.get(recipe_id=1)
          max_length = recipe._meta.get_field('recipe_name').max_length
          self.assertEqual(max_length, 120)

    def test_get_absolute_url(self):
        recipe = Recipe.objects.get(recipe_id=1)
        self.assertEqual(recipe.get_absolute_url(), '/list/1')


class RecipesFormTest(TestCase):
    def test_form_renders_recipe_name_input(self):
        form = RecipeSearchForm()
        self.assertIn('recipe_name', form.as_p())

    def test_form_renders_chart_type_input(self):
        form = RecipeSearchForm()
        self.assertIn('chart_type', form.as_p())

    def test_form_valid_data(self):
        form = RecipeSearchForm(
            data={'recipe_name': '#1', 'chart_type': '#2'})
        self.assertTrue(form.is_valid())