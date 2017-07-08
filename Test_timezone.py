import pytz
from pytz import timezone
import datetime

Timezone_list= pytz.all_timezones

print(Timezone_list)


local_tz = timezone('Asia/Kolkata')
t = local_tz.localize(datetime.datetime(1983, 11, 7, 14, 52))

t_utc = t.astimezone(pytz.UTC)

print(t_utc.hour)
