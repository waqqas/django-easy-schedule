from time import sleep

import schedule
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Manage jobs"

    def add_arguments(self, parser):
        parser.add_argument(
            "command",
            default=None,
            type=str,
            help="Command to execute. Possible options are 'run'",
        )

    def handle(self, *args, **options):
        command = options["command"]

        if command == "run":
            self._run(*args, **options)
        else:
            self.stderr.write(self.style.ERROR(f"Invalid command: {command}"))

    def _run(self, *args, **options):
        try:
            while True:
                schedule.run_pending()
                n = schedule.idle_seconds()
                if n is None:
                    # no more jobs
                    break
                elif n > 0:
                    # sleep exactly the right amount of time
                    sleep(n)
        except KeyboardInterrupt:
            pass
        self.stdout.write(self.style.SUCCESS("Done"))
