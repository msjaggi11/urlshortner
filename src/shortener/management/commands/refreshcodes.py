from django.core.management.base import BaseCommand, CommandError
#from polls.models import Question as Poll
from shortener.models import MehnUrl

class Command(BaseCommand):
    help = 'Refreshes all short codes. Just an example how to create custom commands in Django.'

    def add_arguments(self, parser):
        #parser.add_argument('poll_ids', nargs='+', type=int)
        parser.add_argument('--items',  type=int) #-- becomes optional
        #parser.add_argument('number2',  type=int) #without '--', its required.

    def handle(self, *args, **options):
        # for poll_id in options['poll_ids']:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)

        #     poll.opened = False
        #     poll.save()

        #     self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
        return MehnUrl.objects.refresh_shortcodes(options['items'])
