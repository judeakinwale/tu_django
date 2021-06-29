from django_extensions.management.jobs import DailyJob


class Job(DailyJob):
    help = "Daily job to delete outdated events"

    def execute(self):
        # executing empty sample job
        from payment import views
        views.delete_outdated_events()
