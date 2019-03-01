from menu import Menu, MenuItem
from .models import MenuLine

menulines = MenuLine.objects.filter(parent__isnull=True)

for menuline in menulines:
    Menu.add_item("main", MenuItem(menuline.name,
                                   menuline.link,
                                   icon=menuline.icon))
