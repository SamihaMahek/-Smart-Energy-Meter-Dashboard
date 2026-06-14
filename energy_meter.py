import random
import time

def run_smart_meter():
    print("⚡ --- Smart Grid Electricity Meter Dashboard ---")
    print("Simulating live household consumption data tracking loop...\n")
    
    # Run a simple loop to check power metrics 5 separate times
    for cycle in range(1, 6):
        time.sleep(1.5) # Wait a moment between readings
        
        # Standard domestic electrical parameters
        voltage = round(random.uniform(220.0, 240.0), 1)  # Voltage range in Volts
        current = round(random.uniform(1.0, 5.0), 1)     # Appliance load current in Amps
        
        # Simple Logic rule: If current spikes too high, flag a safety warning alert
        status = "Normal Operation"
        if current > 4.5:
            status = "🚨 ALERT: High Load Grid Threshold Exceeded"
            
        # Standard Electrical Math: Power (Watts) = Voltage * Current
        power = round(voltage * current, 1)
        
        # Display the simple clean logs to the terminal console screen
        print(f"Cycle Check #{cycle}")
        print(f"🔌 Metrics: {voltage} V | {current} A")
        print(f"📊 Calculated Consumption: {power} Watts")
        print(f"🛡️ System Security Status: {status}")
        print("-" * 45)

if __name__ == "__main__":
    run_smart_meter()
