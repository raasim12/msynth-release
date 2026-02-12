import subprocess

# Define the parameter ranges
densities = ['dense', 'hetero', 'scattered', 'fatty']
radii = ['5.0', '7.0', '9.0']
lesion_densities = ['1.0', '1.06', '1.1']
dose_percents = ['20%', '40%', '60%', '80%', '100%']

# Map the table you provided (Density -> Percent -> Value)
dose_map = {
    'dense':     {'20%': '1.73e09', '40%': '3.47e09', '60%': '5.20e09', '80%': '6.94e09', '100%': '8.67e09'},
    'hetero':    {'20%': '2.04e09', '40%': '4.08e09', '60%': '6.12e09', '80%': '8.16e09', '100%': '1.02e10'},
    'scattered': {'20%': '4.08e09', '40%': '8.16e09', '60%': '1.22e10', '80%': '1.63e10', '100%': '2.04e10'},
    'fatty':     {'20%': '4.44e09', '40%': '8.88e09', '60%': '1.33e10', '80%': '1.78e10', '100%': '2.22e10'}
}

def run_download():
    for dens in densities:
        for rad in radii:
            for l_dens in lesion_densities:
                for pct in dose_percents:
                    # Get the specific dose value from the map
                    current_dose = dose_map[dens][pct]
                    
                    print(f"--- Starting: {dens}, Radius: {rad}, Lesion: {l_dens}, Dose: {pct} ({current_dose}) ---")
                    
                    # Construct the command
                    cmd = [
                        "python", "-u", "preprocess_and_train_device_models.py",
                        "--density", dens,
                        "--detector", "SIM",
                        "--size", rad,
                        "--lesiondensity", l_dens,
                        "--dose", current_dose
                    ]
                    
                    # Execute and wait for it to finish before next one
                    subprocess.run(cmd)

if __name__ == "__main__":
    run_download()