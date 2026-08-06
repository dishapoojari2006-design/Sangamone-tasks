for hr in range(9, 21):
    for minute in range(0, 60, 5):

        display_hr = hr % 12
        if display_hr == 0:
            display_hr = 12

        hour_angle = (display_hr + minute / 60) * 30
        minute_angle = minute * 6

        angle = abs(hour_angle - minute_angle)

        if angle > 180:
            angle = 360 - angle

        print(f"{hr:02}:{minute:02} - {angle:.1f} degrees")