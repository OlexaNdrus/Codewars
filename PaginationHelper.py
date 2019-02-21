# TODO: complete this class
from math import ceil

class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items=items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        number = self.item_count()/float(self.items)
        return ceil(number)

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        total_pages=self.page_count()
        num=-1
        if page_index<=total_pages:
            if page_index==total_pages:
                num=self.item_count()  % self.items
            else:
                num=self.items
        return num


    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        page=-1
        if 0<= item_index <= self.items and self.collection:
            page=item_index//self.items
        return page

collection = range(1,15)
test=PaginationHelper(collection, 15)
print(test.item_count())
print(test.page_count())
print(test.page_index(5))
print(test.page_item_count(15))