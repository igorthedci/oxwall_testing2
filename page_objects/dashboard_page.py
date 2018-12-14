from page_objects.internal_page import InternalPage


class DashboardPage(InternalPage):
    pass

    # TODO Add all elements and actions that you have in Main Page

    def is_this_page(self):
        return self.active_menu.text == "DASHBOARD"
