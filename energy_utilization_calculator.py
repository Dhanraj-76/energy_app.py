import tkinter as tk
from tkinter import ttk, messagebox
import streamlit as st

def format_time(years_float):
    years = int(years_float)
    months = int((years_float - years) * 12)
    days = int((((years_float - years) * 12) - months) * 30.44)
    return f"{years} years, {months} months, {days} days"

def calculate_diesel_operation(value, unit):
    MJ_per_litre_diesel = 36
    km_per_litre = 20
    yearly_distance_km = 15000
    litres_per_year = yearly_distance_km / km_per_litre  # = 750

    unit_to_joules = {
        "MWh": 1e6 * 3600,
        "GWh": 1e9 * 3600,
        "TWh": 1e12 * 3600
    }

    if unit not in unit_to_joules:
        return " Invalid energy unit.", None

    total_energy_J = value * unit_to_joules[unit]
    total_energy_MJ = total_energy_J / 1e6

    diesel_litres = total_energy_MJ / MJ_per_litre_diesel
    operation_years = diesel_litres / litres_per_year
    human_readable_time = format_time(operation_years)

    diesel_msg = f" {value} {unit} can run a diesel car for:\n🔹 {human_readable_time} (≈ {operation_years:,.2f} years)"
    return diesel_msg, operation_years

def calculate_household_support(value, unit):
    household_annual_kWh = 3600

    unit_to_kWh = {
        "MWh": value * 1e3,
        "GWh": value * 1e6,
        "TWh": value * 1e9
    }

    if unit not in unit_to_kWh:
        return " Invalid energy unit."

    total_kWh = unit_to_kWh[unit]
    num_households = total_kWh / household_annual_kWh

    household_msg = (
        f" {value} {unit} can power approximately:\n"
        f" {int(num_households):,} households for 1 year (each @ 300 kWh/month)"
    )
    return household_msg


def calculate_results():
    try:
        energy_value = float(entry_value.get())
        energy_unit = unit_var.get()

        diesel_result, _ = calculate_diesel_operation(energy_value, energy_unit)
        household_result = calculate_household_support(energy_value, energy_unit)

        result_text.set(f"=== ENERGY USAGE RESULTS ===\n\n{diesel_result}\n\n{household_result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for energy value.")


root = tk.Tk()
root.title(" Diesel Car + Household Energy Duration Calculator")

root.geometry("600x400")
root.resizable(False, False)

frame = ttk.Frame(root, padding=20)
frame.pack(expand=True, fill="both")

# Input: Energy Value
ttk.Label(frame, text="Enter Energy Value:").grid(row=0, column=0, sticky="w")
entry_value = ttk.Entry(frame, width=20)
entry_value.grid(row=0, column=1)

# Input: Energy Unit Dropdown
ttk.Label(frame, text="Select Energy Unit:").grid(row=1, column=0, sticky="w")
unit_var = tk.StringVar(value="GWh")
unit_menu = ttk.Combobox(frame, textvariable=unit_var, values=["MWh", "GWh", "TWh"], state="readonly")
unit_menu.grid(row=1, column=1)

# Calculate Button
calc_button = ttk.Button(frame, text="Calculate", command=calculate_results)
calc_button.grid(row=2, column=0, columnspan=2, pady=10)

# Output Text
result_text = tk.StringVar()
result_label = ttk.Label(frame, textvariable=result_text, justify="left", wraplength=550)
result_label.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
