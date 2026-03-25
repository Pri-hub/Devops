import psutil

#script to check cpu threshold 

def check_cpu_threshold():
    cpu_threshold = int(input("Enter the cpu Threshold"))
    current_cpu = psutil.cpu_percent(interval=1)

    if current_cpu > cpu_threshold:
        print("CPU alert email sent...",current_cpu)

    else:
        print("cpu in safe state")

check_cpu_threshold()


battery = psutil.sensors_battery()
print("Battery percentage:", battery.percent)
if battery.percent < 20:
    print("Battery low alert email sent...", battery.percent)   
else:
    print("Battery level is sufficient")
print("Battery level is sufficient")

user=psutil.users()
print("Current logged in users:", len(user))
for u in user:
    print("User:", u.name, "Logged in since:", u.started)