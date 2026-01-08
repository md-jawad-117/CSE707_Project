import csv
from config import CSV_PATH

#logs the dta in csv file , for each paprcel, its assigned robot and  their time and regular charge taing based on load penatly.

class ExperimentLogger:
    def __init__(self):
        self.file = open(CSV_PATH, "w", newline="")
        self.writer = csv.writer(self.file)
        self.writer.writerow([
            "parcel_id", "load_penalty",
            "delivery_time_sec", "energy_used", "robot_id"
        ])

    def log(self, parcel, robot):
        self.writer.writerow([
            parcel.id,
            robot.id,
            round(parcel.delivery_time - parcel.spawn_time, 3),
            round(1000 - robot.energy, 2),
            robot.id
        ])
        self.file.flush()

    def close(self):
        self.file.close()
