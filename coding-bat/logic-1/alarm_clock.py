# Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a
# boolean indicating if we are on vacation, return a string of the form "7:00"
# indicating when the alarm clock should ring. Weekdays, the alarm should be
# "7:00" and on the weekend it should be "10:00". Unless we are on vacation --
# then on weekdays it should be "10:00" and weekends it should be "off".

def alarm_clock(day, vacation):
    on_vacation =['10:00', 'off']
    not_on_vacation = ['7:00', '10:00']

    if vacation:
        if day in range(1, 6):
            return on_vacation[0]
        else:
            return on_vacation[1]
    else:
        if day in range(1, 6):
            return not_on_vacation[0]
        else:
            return not_on_vacation[1]
