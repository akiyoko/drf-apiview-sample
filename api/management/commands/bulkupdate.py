import time

from django.core.management.base import BaseCommand

from api.models import Book


class Command(BaseCommand):
    help = "Measure the processing time for bulk_update."
    requires_migrations_checks = True
    requires_system_checks = False

    default_total_epoc = 10
    default_count = 1000

    def add_arguments(self, parser):
        parser.add_argument(
            'count', nargs='?',
            type=int,
            help='Loop count',
        )

    def handle(self, *args, **options):
        total_epoc = self.default_total_epoc
        count = self.default_count
        if options['count']:
            count = options['count']
        print(f'count: {count}')

        # 初期レコードを作成
        objs = [Book(title=f'Book{i}', price=1000) for i in range(count * total_epoc)]
        Book.objects.bulk_create(objs)

        elapsed_times = []
        for epoc in range(total_epoc):
            print(f'epoc: {epoc + 1}')
            objs = Book.objects.all()[count * epoc:count * (epoc + 1)]
            for obj in objs:
                obj.title = f'change{epoc + 1}'
            start = time.time()

            # for obj in objs:
            #     obj.save()
            Book.objects.bulk_update(objs, ['title'])

            elapsed_time = time.time() - start
            elapsed_times.append(elapsed_time)
            print(f'elapsed time: {elapsed_time:.5f} secs')

        print(f'Average of elapsed times: {sum(elapsed_times) / total_epoc:.5f} secs')
        print(f'Total count: {Book.objects.all().count()}')
