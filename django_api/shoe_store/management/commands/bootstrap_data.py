from django.core.management.base import BaseCommand, CommandError
from shoe_store.models import ShoeType, ShoeColor


class Command(BaseCommand):
    help = "adds some basic data into the shoe type and shoe color tables"

    def handle(self, *args, **options):
        ShoeColor.objects.create(color_name="Red")
        ShoeColor.objects.create(color_name="Orange")
        ShoeColor.objects.create(color_name="Yellow")
        ShoeColor.objects.create(color_name="Green")
        ShoeColor.objects.create(color_name="Blue")
        ShoeColor.objects.create(color_name="Indigo")
        ShoeColor.objects.create(color_name="Violet")
        ShoeColor.objects.create(color_name="White")
        ShoeColor.objects.create(color_name="Black")

        ShoeType.objects.create(style="sneaker")
        ShoeType.objects.create(style="boot")
        ShoeType.objects.create(style="sandal")
        ShoeType.objects.create(style="dress")
        ShoeType.objects.create(style="other")

        self.stdout.write(self.style.SUCCESS('Successfully entered starter data into the shoe color and shoe type tables'))