import boto3
from boto3.dynamodb.conditions import Attr

class RecipeScanner:
    def __init__(self, region='us-east-1', table_name='recipes'):
        self.dynamodb = boto3.resource('dynamodb', region_name=region)
        self.table = self.dynamodb.Table(table_name)

    def get_recipes_by_cuisine(self, cuisine):
        response = self.table.scan(
            FilterExpression=Attr('cuisine').eq(cuisine)
        )
        return response.get('Items', [])

    def print_ingredients(self, recipes):
        for recipe in recipes:
            print(recipe.get('ingredients'))

# Sample usage:
if __name__ == "__main__":
    scanner = RecipeScanner()
    indian_recipes = scanner.get_recipes_by_cuisine('indian')
    scanner.print_ingredients(indian_recipes)
