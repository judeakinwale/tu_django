from django_extensions.management.jobs import DailyJob


class Job(DailyJob):
    help = """Daily job to send a list of attendees to an event creator,
              a week before it starts"""

    def execute(self):
        # executing empty sample job
        from payment import views
        views.event_creator_attendee_list_email()
        
