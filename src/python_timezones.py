import pytz, datetime

print("Timezones")
timezone_list = {'1':'Europe/Dublin',
                 '2':'Europe/Rome',
                 '3':'Pacific/Marquesas',
                 '4':'Pacific/Samoa',
                 '5':'Universal',
                 '6':'Singapore',
                 '7':'Pacific/Yap',
                 '8':'Indian/Mauritius',
                 '9':'Indian/Mahe'}

print("Choose a time zone from the menu below")
for tz in sorted(timezone_list):
    print(tz,timezone_list[tz])
choice = input("Enter your choise, enter 0 will quit the program \n")
if choice == '0':
    exit

if choice in timezone_list.keys():
    tz_to_display = pytz.timezone(timezone_list[choice])
    world_time = datetime.datetime.now(tz=tz_to_display)
    print("Time in {} is {} {}".format(timezone_list[choice],world_time.strftime('%A %x %X'),world_time.tzname()))
    print("Local time is {}".format(datetime.datetime.now().strftime('%A %x %X')))
    print("UTC time is {}".format(datetime.datetime.utcnow().strftime('%A %x %X')))

