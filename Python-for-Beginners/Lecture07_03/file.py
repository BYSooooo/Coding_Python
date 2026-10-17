import csv

def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", "w")
    writer = csv.writer(file)

    # New Row - Key
    writer.writerow(["Title", "Company", "Reward", "Link"])
    # Add Rows - get Datas
    for job in jobs:
        writer.writerow(job.values())

    file.close()