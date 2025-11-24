from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel team')
        dc = Team.objects.create(name='DC', description='DC team')

        # Create users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Create activities
        Activity.objects.create(user=users[0], type='running', duration=30, points=10)
        Activity.objects.create(user=users[1], type='walking', duration=45, points=8)
        Activity.objects.create(user=users[2], type='strength', duration=60, points=15)
        Activity.objects.create(user=users[3], type='cycling', duration=20, points=5)

        # Create workouts
        w1 = Workout.objects.create(name='Morning Cardio', description='Cardio for all')
        w2 = Workout.objects.create(name='Strength Circuit', description='Strength for all')
        w1.suggested_for.set(users)
        w2.suggested_for.set(users)

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, total_points=18)
        Leaderboard.objects.create(team=dc, total_points=20)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
