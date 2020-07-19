# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import json


class TutorialPipeline:
    def process_item(self, item, spider):
        return item

class AuthorFilterPipeline:

    def __init__(self):
        self.authors = { "Albert Einstein" }

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        author = adapter.get("author")
        if author in self.authors:
            return item
        else:
            raise DropItem("Not from wanted author")

class JsonWriterPipeline:

    def open_spider(self, spider):
        self.file = open("quotes.jl", "w")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = f"{json.dumps(ItemAdapter(item).asdict(), indent=4)}\n"
        self.file.write(line)
        return item
