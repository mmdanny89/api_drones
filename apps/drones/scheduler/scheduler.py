from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
import sys
from apps.drones.models import LogBattery, Drone


def check_battery_sattus():
    all_drones = Drone.objects.all()
    if all_drones:
        for drone in all_drones:
            log = LogBattery(log={"drone": drone.serial_number, "batery": drone.get_battery_capacity()})
            log.save()


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    scheduler.add_job(check_battery_sattus, 'interval', minutes=3, name='register_log', jobstore='default')
    register_events(scheduler)
    scheduler.start()
    print("Scheduler started...", file=sys.stdout)
