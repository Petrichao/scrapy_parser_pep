from collections import defaultdict
import csv
from datetime import datetime

from .settings import BASE_DIR


class PepParsePipeline:

    def open_spider(self, spider):
        self.status_count = defaultdict(int)

    def process_item(self, item, spider):
        self.status_count[item['status']] += 1
        return item

    def close_spider(self, spider):
        date = datetime.strftime(datetime.now(), '%Y-%m-%d_%H-%M-%S')
        file = BASE_DIR / f'status_summary_{date}.csv'
        with open(file, 'w', encoding='utf-8', newline='') as csv_file:
            csv.writer(
                csv_file,
                dialect=csv.excel,
                quoting=csv.QUOTE_NONE
            ).writerows(
                (
                    ('Status', 'Quantity'),
                    *self.status_count.items(),
                    ('Total', sum(self.status_count.values()))
                )
            )
