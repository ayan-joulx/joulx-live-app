import numpy as np
import os
import glob
import time

class BatchEdgeOptimizer:
    def __init__(self, target_sparsity: float = 0.40):
        self.target_sparsity = target_sparsity

    def process_directory(self, input_dir: str, output_dir: str):
        """
        Directory ke andar mojud saari model files ko batch mein optimize karta hai.
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        search_path = os.path.join(input_dir, "*.npy")
        model_files = glob.glob(search_path)
        
        if not model_files:
            print(f"[-] Batch Error: No .npy model files found in '{input_dir}' directory.")
            return

        print(f"\n[⚡ BATCH EDGE MODULE] Found {len(model_files)} model files for local optimization.")
        print(f"    - Target Sparsity Goal : {self.target_sparsity * 100}%")
        print("-" * 50)

        total_start_time = time.time()
        
        for file_path in model_files:
            filename = os.path.basename(file_path)
            output_path = os.path.join(output_dir, f"optimized_{filename}")
            
            print(f"[*] Processing: {filename}...")
            
            # Load weights
            weights = np.load(file_path)
            total_weights = weights.size
            
            # Thermodynamic entropy & dynamic thresholding
            abs_weights = np.abs(weights)
            energy_state = abs_weights / (np.sum(abs_weights) + 1e-8)
            threshold = np.percentile(energy_state, self.target_sparsity * 100)
            
            mask = energy_state > threshold
            optimized_weights = weights * mask
            
            # Save optimized model locally
            np.save(output_path, optimized_weights)
            
            reduced_weights = total_weights - np.count_nonzero(optimized_weights)
            print(f"    -> Saved to: {output_path} ({reduced_weights:,} params pruned)")

        total_elapsed = time.time() - total_start_time
        print("-" * 50)
        print(f"[✔ BATCH SUCCESS] All files optimized locally in {total_elapsed:.4f} seconds!")

if __name__ == "__main__":
    input_folder = "." # Current directory jahan .npy files hain
    output_folder = "edge_batch_output"
    
    batch_runner = BatchEdgeOptimizer(target_sparsity=0.40)
    batch_runner.process_directory(input_folder, output_folder)