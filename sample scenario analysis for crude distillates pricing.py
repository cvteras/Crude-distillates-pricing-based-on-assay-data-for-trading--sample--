# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 20:20:57 2025

@author: cgarn
"""

# scenario_analysis.py

import pandas as pd

# --- Assay Yields (Volume % per barrel) ---
assay_yields = {
    '30-65': 0.035,  # IBP-65F
    '65-100': 0.052,
    '100-150': 0.091,
    '150-200': 0.093,
    '200-250': 0.102,
    '250-300': 0.111,
    '300-350': 0.106,
    '350-370': 0.038,
    '370-450': 0.0359,
    '450-500': 0.0133,
    '500-550': 0.066,
    '550+': 0.051,
    'Residuum': 0.108
}

# --- Base Spot Prices ($/barrel) ---
spot_prices = {
    '30-65': 40,
    '65-100': 60,
    '100-150': 65,
    '150-200': 90,
    '200-250': 110,
    '250-300': 95,
    '300-350': 120,
    '350-370': 75,
    '370-450':80,
    '450-500': 120,
    '500-550': 110,
    '550+': 55,
    'Residuum': 45
}

# --- Function to run scenario analysis ---
def run_scenario(spot_multiplier):
    data = []
    for cut in assay_yields:
        yield_fraction = assay_yields[cut]
        spot_price = spot_prices[cut] * spot_multiplier.get(cut, 1)
        revenue = yield_fraction * spot_price
        data.append({'Cut': cut, 'Yield %': yield_fraction * 100, 'Adjusted Spot Price ($/bbl)': spot_price, 'Revenue Contribution ($/bbl)': revenue})

    results_df = pd.DataFrame(data)
    total_price = results_df['Revenue Contribution ($/bbl)'].sum()
    return results_df, total_price

# --- Example Scenario: Prices move ---
# (e.g., Gasoline and Diesel increase 10%, Residuum drops 5%)
price_change_scenario = {
    '100-150': 1.10,  # Heavy Naphtha (Gasoline range up 10%)
    '250-300': 1.10,  # Diesel up 10%
    'Residuum': 0.95  # Residual fuel down 5%
}

# --- Run the Scenario ---
scenario_df, scenario_total_price = run_scenario(price_change_scenario)

# --- Output ---
print(scenario_df)
print("\nTotal Selling Price per Barrel under Scenario: ${:.2f}".format(scenario_total_price))

# --- Save to Excel ---
scenario_df.to_excel('scenario_assay_pricing_output.xlsx', index=False)
print("\nScenario results saved to 'scenario_assay_pricing_output.xlsx'")
