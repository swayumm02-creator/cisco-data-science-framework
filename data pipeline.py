import math
class DataPipelineValidator:
    def __init__(self, dataset_name: str, total_records: int):
        self.dataset_name = dataset_name
        self.total_records = total_records

    def process_and_clean_data(self, anomaly_rate: float) -> dict:
        
        if not (0.0 <= anomaly_rate <= 1.0):
            raise ValueError("Anomaly rate must be between 0.0 and 1.0")
            
        corrupted_signals = math.ceil(self.total_records * anomaly_rate)
        verified_records = self.total_records - corrupted_signals
        efficiency_score = (verified_records / self.total_records) * 100
        
        return {
            "dataset_identity": self.dataset_name,
            "total_ingested_rows": self.total_records,
            "anomalies_purged": corrupted_signals,
            "production_ready_rows": verified_records,
            "pipeline_efficiency_pct": round(efficiency_score, 2)
        }

if __name__ == "__main__":
    print("[INFO] Initializing Cisco AI/ML Data Pipeline Simulator...")
    
   
    pipeline = DataPipelineValidator(dataset_name="Retail_Sales_Inventory", total_records=15500)
    metrics = pipeline.process_and_clean_data(anomaly_rate=0.045)
    
    print("\n--- PIPELINE EXECUTION METRICS ---")
    for key, value in metrics.items():
        formatted_key = key.replace("_", " ").title()
        print(f"{formatted_key}: {value}")
    print("----------------------------------")
    print("[SUCCESS] Data pipeline validated for ML model ingestion.")
