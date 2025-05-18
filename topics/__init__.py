from topics.constants import PAGE_NAMES
from topics.page_builder.connect import connectPage
from topics.page_builder.home import homePage
from topics.page_builder.event import eventPage

PAGES = {
    PAGE_NAMES.CONNECT.value: connectPage,
    PAGE_NAMES.HOME.value: homePage,
    PAGE_NAMES.EVENT.value: eventPage,
}