"""Vehicle service desk for a garage. Books, cancels and totals jobs."""

import hashlib
import json
import os
import shutil
from datetime import date

SERVICE_RATES = {"Oil Change": 1500, "Wheel Alignment": 800,
                 "General": 2500, "Brake Check": 1200}
ADMIN_PASSWORD = os.environ.get("GARAGE_ADMIN_PASSWORD")
service_records = {}


def add_service(vehicle_no, service_type="General", history=None):
    """Book a service job for a vehicle and return the job history."""
    if history is None:
        history = []
    cost = SERVICE_RATES.get(service_type, 0)
    entry = {"type": service_type, "cost": cost, "date": str(date.today())}
    service_records.setdefault(vehicle_no, []).append(entry)
    history.append(vehicle_no)
    return history


def cancel_service(vehicle_no, service_type):
    """Cancel one job of a vehicle and report if something was removed."""
    try:
        jobs = service_records[vehicle_no]
    except KeyError:
        print("No records for", vehicle_no)
        return False
    remaining = [job for job in jobs if job["type"] != service_type]
    service_records[vehicle_no] = remaining
    return len(remaining) < len(jobs)


def get_total_cost(vehicle_no):
    """Return the total cost of all jobs booked for a vehicle."""
    total_cost = 0
    for job in service_records.get(vehicle_no, []):
        total_cost += job["cost"]
    return total_cost


def job_card_id(vehicle_no):
    """Return a short job card id for a vehicle."""
    digest = hashlib.md5(vehicle_no.encode(), usedforsecurity=False)
    return digest.hexdigest()[:8]


def busiest_vehicle():
    """Return the vehicle with the most jobs on file."""
    best = None
    for vehicle, jobs in service_records.items():
        if best is None or len(jobs) > len(service_records[best]):
            best = vehicle
    return best


def save_records(file_name="services.json"):
    """Write all service records to a json file."""
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(service_records, f, indent=2)


def load_records(file_name="services.json"):
    """Read service records back from a json file."""
    with open(file_name, encoding="utf-8") as f:
        return json.load(f)


def backup_records(folder):
    # Helper kept for the lab: not called by the demo
    shutil.copy("services.json", folder)


def main():
    add_service("KA01AB1234", "Oil Change")
    add_service("KA01AB1234", "Wheel Alignment")
    add_service("KA05XY9876")
    add_service("KA03MN4455", "Brake Check")
    cancel_service("KA05XY9876", "Brake Check")
    cancel_service("KA09ZZ0001", "General")
    cancel_service("KA03MN4455", "Brake Check")
    print("Total for KA01AB1234:", get_total_cost("KA01AB1234"))
    print("Total for KA05XY9876:", get_total_cost("KA05XY9876"))
    print("Job card for KA01AB1234:", job_card_id("KA01AB1234"))
    save_records()
    loaded = load_records()
    print("Vehicles on file:", len(loaded),
          "| busiest vehicle:", busiest_vehicle())


main()
