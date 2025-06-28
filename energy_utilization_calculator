import streamlit as st

st.set_page_config(page_title="⚡ Energy Utilization Calculator", page_icon="🔋")

st.title("🔋 Diesel Car + Household Power Duration Calculator")
st.markdown("Enter an energy value and unit to see how far a diesel car can go or how many homes it can power.")

# --- User Input ---
energy_value = st.number_input("🔢 Enter energy value", value=0.005, min_value=0.0)
energy_unit = st.selectbox("⚙ Select energy unit", ["MWh", "GWh", "TWh"])

# --- Functions ---
def format_time(years_float):
    years = int(years_float)
    months = int((years_float - years) * 12)
    days = int((((years_float - years) * 12) - months) * 30.44)
    return f"{years} years, {months} months, {days} days"

def calculate_diesel_operation(value, unit):
    MJ_per_litre_diesel = 36
    km_per_litre = 20
    yearly_distance_km = 15000
    litres_per_year = yearly_distance_km / km_per_litre

    unit_to_joules = {
        "MWh": 1e6 * 3600,
        "GWh": 1e9 * 3600,
        "TWh": 1e12 * 3600
    }

    if unit not in unit_to_joules:
        return "❌ Invalid energy unit.", None

    total_energy_J = value * unit_to_joules[unit]
    total_energy_MJ = total_energy_J / 1e6
    diesel_litres = total_energy_MJ / MJ_per_litre_diesel
    operation_years = diesel_litres / litres_per_year
    human_readable_time = format_time(operation_years)

    diesel_msg = f"🚗 {value} {unit} can run a diesel car for:\n🔹 *{human_readable_time}* (≈ {operation_years:,.2f} years)"
    return diesel_msg, operation_years

def calculate_household_support(value, unit):
    household_annual_kWh = 3600
    unit_to_kWh = {
        "MWh": value * 1e3,
        "GWh": value * 1e6,
        "TWh": value * 1e9
    }

    if unit not in unit_to_kWh:
        return "❌ Invalid energy unit."

    total_kWh = unit_to_kWh[unit]
    num_households = total_kWh / household_annual_kWh

    household_msg = (
        f"🏠 {value} {unit} can power approximately:\n"
        f"🔹 *{int(num_households):,} households* for 1 year (each @ 300 kWh/month)"
    )
    return household_msg

# --- Run Calculations ---
diesel_result, _ = calculate_diesel_operation(energy_value, energy_unit)
household_result = calculate_household_support(energy_value, energy_unit)

# --- Show Output ---
st.subheader("🔍 Results")
st.success(diesel_result)
st.info(household_result)
