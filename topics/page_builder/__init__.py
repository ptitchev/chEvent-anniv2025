class PageBuilder:
    def __init__(
            self,
            page_name,
            page_title,
            page_icon,
            build_func
            ):
        self.page_name = page_name
        self.page_title = page_title
        self.page_icon = page_icon
        self.build_func = build_func

    def build(self, session):
        self.build_func(session)
