import datetime

now = datetime.datetime.now()
minutes = now.minute
seconds = now.second
print(f"Time: {minutes}, {seconds}")