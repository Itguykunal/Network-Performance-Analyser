import speedtest
from NBM import monitor_bandwidth
from Export import export_data

test = speedtest.Speedtest()
option = int(input('''What speed do you want to test:
1) Download Speed
2) Upload Speed
3) Ping
4) Bandwidth Monitor
5) Export Data
Your Choice: '''))

download_result = None  # Define download_result variable

if option == 1:
    print("Performing download test...")
    download_result = test.download()
    print(f"Download speed: {int(download_result / 1024 / 1024)} Mbit/s")
elif option == 2:
    print("Performing upload test...")
    upload_result = test.upload()
    print(f"Upload speed: {int(upload_result / 1024 / 1024)} Mbit/s")
elif option == 3:
    print("Performing ping test...")
    ping_result = test.results.ping
    print(f"Ping: {int(ping_result)} ms")
elif option == 4:
    print("Starting bandwidth monitoring...")
    monitor_bandwidth()
elif option == 5:
    download_result = test.download()
    upload_result = test.upload()
    ping_result = test.results.ping

    export_format = input("Choose export format (json/csv): ")
    filename = input("Enter file name for export: ")
    if export_format == 'json':
        data = {
            "download_speed": int(download_result / 1024 / 1024),
            "upload_speed": int(upload_result / 1024 / 1024),
            "ping": int(ping_result)
        }
    elif export_format == 'csv':
        data = [{
            "download_speed": int(download_result / 1024 / 1024),
            "upload_speed": int(upload_result / 1024 / 1024),
            "ping": int(ping_result)
        }]
    else:
        print("Invalid export format.")
        exit(1)

    export_data(data, filename, export_format)
else:
    print("Invalid option.")
 