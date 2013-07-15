

class NavMenuModel(object):
    def __init__(self, *kargs, **kwargs):
        super(NavMenuModel, self).__init__(*kargs, **kwargs)
        self.items = {}
        self.index = 0

    def add(self, item):
        self.items[self.index] = item
        self.index += 1
        return self.index

    def remove(self, item_id):
        if item_id in self.items:
            del self.items[item_id]

    def hide(self, item_id):
        if item_id in self.items:
            self.items[item_id].hide = True

    def unhide(self, item_id):
        if item_id in self.items:
            self.items[item_id].hide = False

    def render(self):
        pass


class NavMenuItemModel(object):
    def __init__(self, name, url=None, icon=None, title=None, hide=False, sub_item=None, prefix=None, *kargs, **kwargs):
        super(NavMenuItemModel, self).__init__(*kargs, **kwargs)
        self.name = name
        self.url = url
        self.icon = icon
        self.title = title
        self.hide = hide
        self.sub_item = sub_item
        self.prefix = prefix if prefix else ""

        if not self.url:
            self.url = "{prefix}/{name}"\
                .format(prefix=self.prefix, name=self.name)



    def render(self):
        pass
