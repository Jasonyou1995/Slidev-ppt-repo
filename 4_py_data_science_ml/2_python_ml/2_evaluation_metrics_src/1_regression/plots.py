import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error
import os

OUTPUT_DIR = 'img'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# --------------------------------------------------------------------------------
# --- Generate Random Data: 180+ points ---
# --------------------------------------------------------------------------------
np.random.seed(42)
N = 200
y_true = np.random.uniform(10, 30, N)
y_pred = y_true + np.random.normal(0, 2, N)  # Add some noise

# --------------------------------------------------------------------------------
# --- Manual Calculations vs sklearn ---
# --------------------------------------------------------------------------------
# MAE: Manual calculation
errors_abs = np.abs(y_true - y_pred)
mae_manual = np.sum(errors_abs) / N
mae_sklearn = mean_absolute_error(y_true, y_pred)

# MSE: Manual calculation
errors_squared = (y_true - y_pred) ** 2
mse_manual = np.sum(errors_squared) / N
mse_sklearn = mean_squared_error(y_true, y_pred)

# RMSE: Manual calculation
rmse_manual = np.sqrt(mse_manual)
rmse_from_sklearn = np.sqrt(mse_sklearn)

print(f"MAE - Manual: {mae_manual:.4f}, sklearn: {mae_sklearn:.4f}")
print(f"MSE - Manual: {mse_manual:.4f}, sklearn: {mse_sklearn:.4f}")
print(f"RMSE - Manual: {rmse_manual:.4f}, from sklearn MSE: {rmse_from_sklearn:.4f}")

# --------------------------------------------------------------------------------
# --- Plot 1: MAE Overview ---
# --------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(y_true, y_pred, color='blue', s=20, alpha=0.6, label='Predicted Points ($\hat{y}$)')
ax.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], 
        color='gray', linestyle='--', label='Perfect Prediction ($y = \hat{y}$)')

# Plot sample error lines (show first 20 for clarity)
for i in range(min(20, N)):
    ax.plot([y_true[i], y_true[i]], [y_true[i], y_pred[i]], 
           color='darkorange', linestyle='-', linewidth=1, alpha=0.5)

mae_formula = r'$\text{MAE} = \frac{1}{N} \sum_{i=1}^{N} |y_i - \hat{y}_i|$'
ax.text(0.95, 0.1, mae_formula, transform=ax.transAxes, fontsize=14,
        verticalalignment='bottom', horizontalalignment='right',
        bbox=dict(boxstyle="round,pad=0.5", fc="lightblue", alpha=0.7))

# result_text = f'MAE: {mae_manual:.2f}\nMSE: {mse_manual:.2f}\nRMSE: {rmse_manual:.2f}'
result_text = f'MAE: {mae_sklearn:.2f}'
ax.text(0.05, 0.95, result_text, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', horizontalalignment='left', color='blue', fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.4", fc="white", alpha=0.8))

ax.set_xlabel('Actual Value ($y$)', fontsize=12)
ax.set_ylabel('Predicted Value ($\hat{y}$)', fontsize=12)
ax.set_title('Mean Absolute Error (MAE): Linear Error Measurement', fontsize=14, fontweight='bold')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(fontsize=10)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '01_mae_overview.png'), dpi=300, bbox_inches='tight')
plt.close()
print(f"Saved: {OUTPUT_DIR}/01_mae_overview.png")

# --------------------------------------------------------------------------------
# --- Plot 2: MAE Limitation - Extreme Cases ---
# All have same MAE but very different error patterns
# --------------------------------------------------------------------------------
target_mae = 3.0

# Scenario 1: Normal balanced errors
y_true_1 = np.random.uniform(10, 30, N)
y_pred_1 = y_true_1 + np.random.normal(0, target_mae, N)
mae_1 = np.mean(np.abs(y_true_1 - y_pred_1))
# Adjust to match target MAE
y_pred_1 = y_true_1 + (y_pred_1 - y_true_1) * (target_mae / mae_1)

# Scenario 2: Normal with slight variation
y_true_2 = np.random.uniform(10, 30, N)
y_pred_2 = y_true_2 + np.random.normal(0, target_mae * 0.8, N)
mae_2 = np.mean(np.abs(y_true_2 - y_pred_2))
y_pred_2 = y_true_2 + (y_pred_2 - y_true_2) * (target_mae / mae_2)

# Scenario 3: EXTREME - One side huge errors, other side perfect (almost vertical line)
y_true_3 = np.random.uniform(10, 30, N)
y_pred_3 = y_true_3.copy()
# First half: perfect predictions
y_pred_3[:N//2] = y_true_3[:N//2]
# Second half: huge errors to achieve target MAE
# Total error needed: target_mae * N
# Since first half has 0 error, second half needs: target_mae * N
errors_needed = target_mae * N
y_pred_3[N//2:] = y_true_3[N//2:] + np.random.choice([-1, 1], N//2) * (errors_needed / (N//2))
# Verify and adjust
mae_3 = np.mean(np.abs(y_true_3 - y_pred_3))
if abs(mae_3 - target_mae) > 0.01:
    y_pred_3[N//2:] = y_true_3[N//2:] + (y_pred_3[N//2:] - y_true_3[N//2:]) * (target_mae / mae_3)

# Scenario 4: EXTREME - Most points perfect, few massive errors
y_true_4 = np.random.uniform(10, 30, N)
y_pred_4 = y_true_4.copy()
# 95% perfect
num_perfect = int(0.95 * N)
y_pred_4[:num_perfect] = y_true_4[:num_perfect]
# 5% massive errors to achieve target MAE
num_outliers = N - num_perfect
errors_per_outlier = (target_mae * N) / num_outliers
y_pred_4[num_perfect:] = y_true_4[num_perfect:] + np.random.choice([-1, 1], num_outliers) * errors_per_outlier
# Verify and adjust
mae_4 = np.mean(np.abs(y_true_4 - y_pred_4))
if abs(mae_4 - target_mae) > 0.01:
    y_pred_4[num_perfect:] = y_true_4[num_perfect:] + (y_pred_4[num_perfect:] - y_true_4[num_perfect:]) * (target_mae / mae_4)

scenarios = [
    (y_true_1, y_pred_1, 'Normal: Balanced Errors'),
    (y_true_2, y_pred_2, 'Normal: Slight Variation'),
    (y_true_3, y_pred_3, 'EXTREME: Half Perfect, Half Large Errors'),
    (y_true_4, y_pred_4, 'EXTREME: Most Perfect, Few Massive Errors')
]

fig, axes = plt.subplots(2, 2, figsize=(14, 12))
axes = axes.flatten()

for idx, (y_t, y_p, title) in enumerate(scenarios):
    ax = axes[idx]
    errors = np.abs(y_t - y_p)
    
    ax.scatter(y_t, y_p, color='blue', s=10, alpha=0.5, zorder=3)
    ax.plot([y_t.min(), y_t.max()], [y_t.min(), y_t.max()], 
           color='gray', linestyle='--', linewidth=1.5, alpha=0.5)
    
    # Plot error lines - show all for extreme cases
    for i in range(N):
        error_size = errors[i]
        color = 'red' if error_size > target_mae * 2 else 'darkorange'
        linewidth = 2 if error_size > target_mae * 2 else 0.5
        ax.plot([y_t[i], y_t[i]], [y_t[i], y_p[i]], 
               color=color, linestyle='-', linewidth=linewidth, alpha=0.6, zorder=2)
    
    # Calculate all metrics for this scenario
    errors_abs = np.abs(y_t - y_p)
    errors_sq = (y_t - y_p) ** 2
    mae = np.mean(errors_abs)
    mse = np.mean(errors_sq)
    rmse = np.sqrt(mse)
    
    ax.text(0.05, 0.95, f'MAE: {mae:.2f}', transform=ax.transAxes,
           fontsize=11, verticalalignment='top', horizontalalignment='left',
           bbox=dict(boxstyle="round,pad=0.3", fc="yellow", alpha=0.7), fontweight='bold')
    
    ax.set_xlabel('Actual Value ($y$)', fontsize=10)
    ax.set_ylabel('Predicted Value ($\hat{y}$)', fontsize=10)
    ax.set_title(title, fontsize=11, fontweight='bold')
    ax.grid(True, linestyle=':', alpha=0.6)

fig.suptitle(f'MAE Limitation: Same MAE ({target_mae:.1f}), Different Error Patterns', 
            fontsize=16, fontweight='bold', y=0.995)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '02_mae_limitation_comparison.png'), dpi=300, bbox_inches='tight')
plt.close()
print(f"Saved: {OUTPUT_DIR}/02_mae_limitation_comparison.png")

# --------------------------------------------------------------------------------
# --- Plot 3: MSE Overview ---
# --------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(y_true, y_pred, color='blue', s=20, alpha=0.6, label='Predicted Points ($\hat{y}$)')
ax.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()],
        color='gray', linestyle='--', label='Perfect Prediction ($y = \hat{y}$)')

# Plot error lines - thickness shows squared error
max_sq_error = np.max(errors_squared)
for i in range(min(20, N)):
    sq_error = errors_squared[i]
    linewidth = 1 + (sq_error / max_sq_error) * 3
    ax.plot([y_true[i], y_true[i]], [y_true[i], y_pred[i]],
           color='darkred', linestyle='-', linewidth=linewidth, alpha=0.6)

mse_formula = r'$\text{MSE} = \frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2$'
ax.text(0.95, 0.1, mse_formula, transform=ax.transAxes, fontsize=14,
        verticalalignment='bottom', horizontalalignment='right',
        bbox=dict(boxstyle="round,pad=0.5", fc="lightcoral", alpha=0.7))

# result_text = f'MAE: {mae_manual:.2f}\nMSE: {mse_manual:.2f}\nRMSE: {rmse_manual:.2f}'
result_text = f'MAE: {mae_manual:.2f}\nMSE: {mse_manual:.2f}'

ax.text(0.05, 0.95, result_text, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', horizontalalignment='left', color='darkred', fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.4", fc="white", alpha=0.8))

ax.set_xlabel('Actual Value ($y$)', fontsize=12)
ax.set_ylabel('Predicted Value ($\hat{y}$)', fontsize=12)
ax.set_title('Mean Squared Error (MSE): Squared Error Measurement', fontsize=14, fontweight='bold')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(fontsize=10)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '03_mse_overview.png'), dpi=300, bbox_inches='tight')
plt.close()
print(f"Saved: {OUTPUT_DIR}/03_mse_overview.png")

# --------------------------------------------------------------------------------
# --- Plot 4: RMSE Overview ---
# --------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(y_true, y_pred, color='blue', s=20, alpha=0.6, label='Predicted Points ($\hat{y}$)')
ax.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()],
        color='gray', linestyle='--', label='Perfect Prediction ($y = \hat{y}$)')

# Plot error lines
for i in range(min(20, N)):
    ax.plot([y_true[i], y_true[i]], [y_true[i], y_pred[i]],
           color='purple', linestyle='-', linewidth=1, alpha=0.5)

rmse_formula = r'$\text{RMSE} = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2}$'
ax.text(0.95, 0.1, rmse_formula, transform=ax.transAxes, fontsize=14,
        verticalalignment='bottom', horizontalalignment='right',
        bbox=dict(boxstyle="round,pad=0.5", fc="lavender", alpha=0.7))

result_text = f'MAE: {mae_manual:.2f}\nMSE: {mse_manual:.2f}\nRMSE: {rmse_manual:.2f}'
ax.text(0.05, 0.95, result_text, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', horizontalalignment='left', color='purple', fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.4", fc="white", alpha=0.8))

ax.set_xlabel('Actual Value ($y$)', fontsize=12)
ax.set_ylabel('Predicted Value ($\hat{y}$)', fontsize=12)
ax.set_title('Root Mean Squared Error (RMSE): Interpretable Squared Error', fontsize=14, fontweight='bold')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(fontsize=10)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '04_rmse_overview.png'), dpi=300, bbox_inches='tight')
plt.close()
print(f"Saved: {OUTPUT_DIR}/04_rmse_overview.png")

# --------------------------------------------------------------------------------
# --- Plot 5: All Metrics Comparison - Same as Plot 2 but with MAE, MSE, RMSE ---
# --------------------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(14, 12))
axes = axes.flatten()

for idx, (y_t, y_p, title) in enumerate(scenarios):
    ax = axes[idx]
    errors = np.abs(y_t - y_p)
    
    ax.scatter(y_t, y_p, color='blue', s=10, alpha=0.5, zorder=3)
    ax.plot([y_t.min(), y_t.max()], [y_t.min(), y_t.max()], 
           color='gray', linestyle='--', linewidth=1.5, alpha=0.5)
    
    # Plot error lines - show all for extreme cases
    for i in range(N):
        error_size = errors[i]
        color = 'red' if error_size > target_mae * 2 else 'darkorange'
        linewidth = 2 if error_size > target_mae * 2 else 0.5
        ax.plot([y_t[i], y_t[i]], [y_t[i], y_p[i]], 
               color=color, linestyle='-', linewidth=linewidth, alpha=0.6, zorder=2)
    
    # Calculate all metrics for this scenario
    errors_abs = np.abs(y_t - y_p)
    errors_sq = (y_t - y_p) ** 2
    mae = np.mean(errors_abs)
    mse = np.mean(errors_sq)
    rmse = np.sqrt(mse)
    
    # Show all three metrics
    metrics_text = f'MAE: {mae:.2f}\nMSE: {mse:.2f}\nRMSE: {rmse:.2f}'
    ax.text(0.05, 0.95, metrics_text, transform=ax.transAxes,
           fontsize=10, verticalalignment='top', horizontalalignment='left',
           bbox=dict(boxstyle="round,pad=0.4", fc="yellow", alpha=0.8), fontweight='bold')
    
    ax.set_xlabel('Actual Value ($y$)', fontsize=10)
    ax.set_ylabel('Predicted Value ($\hat{y}$)', fontsize=10)
    ax.set_title(title, fontsize=11, fontweight='bold')
    ax.grid(True, linestyle=':', alpha=0.6)

fig.suptitle('Metrics Comparison: Same MAE, Different MSE & RMSE Patterns', 
            fontsize=16, fontweight='bold', y=0.995)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, '05_all_metrics_comparison.png'), dpi=300, bbox_inches='tight')
plt.close()
print(f"Saved: {OUTPUT_DIR}/05_all_metrics_comparison.png")

print("-" * 60)
print("All plots generated successfully!")

# --------------------------------------------------------------------------------
# --- Alternative Plots: Predicted on X-axis, Actual on Y-axis ---
# Alternative convention: Some practitioners prefer this orientation
# --------------------------------------------------------------------------------
ALT_OUTPUT_DIR = os.path.join(OUTPUT_DIR, 'alternative')
os.makedirs(ALT_OUTPUT_DIR, exist_ok=True)
print("\nGenerating alternative plots (Predicted on X, Actual on Y)...")
print("-" * 60)

# --------------------------------------------------------------------------------
# --- Alternative Plot 1: MAE Overview ---
# --------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(y_pred, y_true, color='blue', s=20, alpha=0.6, label='Actual Points ($y$)')
ax.plot([y_pred.min(), y_pred.max()], [y_pred.min(), y_pred.max()], 
        color='gray', linestyle='--', label='Perfect Prediction ($y = \hat{y}$)')

# Plot horizontal error lines (show first 20 for clarity)
for i in range(min(20, N)):
    ax.plot([y_pred[i], y_true[i]], [y_true[i], y_true[i]], 
           color='darkorange', linestyle='-', linewidth=1, alpha=0.5)

mae_formula = r'$\text{MAE} = \frac{1}{N} \sum_{i=1}^{N} |y_i - \hat{y}_i|$'
ax.text(0.95, 0.1, mae_formula, transform=ax.transAxes, fontsize=14,
        verticalalignment='bottom', horizontalalignment='right',
        bbox=dict(boxstyle="round,pad=0.5", fc="lightblue", alpha=0.7))

result_text = f'MAE: {mae_sklearn:.2f}'
ax.text(0.05, 0.95, result_text, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', horizontalalignment='left', color='blue', fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.4", fc="white", alpha=0.8))

ax.set_xlabel('Predicted Value ($\hat{y}$)', fontsize=12)
ax.set_ylabel('Actual Value ($y$)', fontsize=12)
ax.set_title('Mean Absolute Error (MAE): Alternative Orientation', fontsize=14, fontweight='bold')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(fontsize=10)
plt.tight_layout()
plt.savefig(os.path.join(ALT_OUTPUT_DIR, '01_mae_overview.png'), dpi=300, bbox_inches='tight')
plt.close()
print(f"Saved: {ALT_OUTPUT_DIR}/01_mae_overview.png")

# --------------------------------------------------------------------------------
# --- Alternative Plot 2: MAE Limitation Comparison ---
# --------------------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(14, 12))
axes = axes.flatten()

for idx, (y_t, y_p, title) in enumerate(scenarios):
    ax = axes[idx]
    errors = np.abs(y_t - y_p)
    
    ax.scatter(y_p, y_t, color='blue', s=10, alpha=0.5, zorder=3)
    ax.plot([y_p.min(), y_p.max()], [y_p.min(), y_p.max()], 
           color='gray', linestyle='--', linewidth=1.5, alpha=0.5)
    
    # Plot horizontal error lines
    for i in range(N):
        error_size = errors[i]
        color = 'red' if error_size > target_mae * 2 else 'darkorange'
        linewidth = 2 if error_size > target_mae * 2 else 0.5
        ax.plot([y_p[i], y_t[i]], [y_t[i], y_t[i]], 
               color=color, linestyle='-', linewidth=linewidth, alpha=0.6, zorder=2)
    
    errors_abs = np.abs(y_t - y_p)
    errors_sq = (y_t - y_p) ** 2
    mae = np.mean(errors_abs)
    mse = np.mean(errors_sq)
    rmse = np.sqrt(mse)
    
    ax.text(0.05, 0.95, f'MAE: {mae:.2f}', transform=ax.transAxes,
           fontsize=11, verticalalignment='top', horizontalalignment='left',
           bbox=dict(boxstyle="round,pad=0.3", fc="yellow", alpha=0.7), fontweight='bold')
    
    ax.set_xlabel('Predicted Value ($\hat{y}$)', fontsize=10)
    ax.set_ylabel('Actual Value ($y$)', fontsize=10)
    ax.set_title(title, fontsize=11, fontweight='bold')
    ax.grid(True, linestyle=':', alpha=0.6)

fig.suptitle(f'MAE Limitation: Alternative Orientation (Same MAE {target_mae:.1f})', 
            fontsize=16, fontweight='bold', y=0.995)
plt.tight_layout()
plt.savefig(os.path.join(ALT_OUTPUT_DIR, '02_mae_limitation_comparison.png'), dpi=300, bbox_inches='tight')
plt.close()
print(f"Saved: {ALT_OUTPUT_DIR}/02_mae_limitation_comparison.png")

# --------------------------------------------------------------------------------
# --- Alternative Plot 3: MSE Overview ---
# --------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(y_pred, y_true, color='blue', s=20, alpha=0.6, label='Actual Points ($y$)')
ax.plot([y_pred.min(), y_pred.max()], [y_pred.min(), y_pred.max()],
        color='gray', linestyle='--', label='Perfect Prediction ($y = \hat{y}$)')

# Plot horizontal error lines - thickness shows squared error
max_sq_error = np.max(errors_squared)
for i in range(min(20, N)):
    sq_error = errors_squared[i]
    linewidth = 1 + (sq_error / max_sq_error) * 3
    ax.plot([y_pred[i], y_true[i]], [y_true[i], y_true[i]],
           color='darkred', linestyle='-', linewidth=linewidth, alpha=0.6)

mse_formula = r'$\text{MSE} = \frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2$'
ax.text(0.95, 0.1, mse_formula, transform=ax.transAxes, fontsize=14,
        verticalalignment='bottom', horizontalalignment='right',
        bbox=dict(boxstyle="round,pad=0.5", fc="lightcoral", alpha=0.7))

result_text = f'MAE: {mae_manual:.2f}\nMSE: {mse_manual:.2f}\nRMSE: {rmse_manual:.2f}'
ax.text(0.05, 0.95, result_text, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', horizontalalignment='left', color='darkred', fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.4", fc="white", alpha=0.8))

ax.set_xlabel('Predicted Value ($\hat{y}$)', fontsize=12)
ax.set_ylabel('Actual Value ($y$)', fontsize=12)
ax.set_title('Mean Squared Error (MSE): Alternative Orientation', fontsize=14, fontweight='bold')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(fontsize=10)
plt.tight_layout()
plt.savefig(os.path.join(ALT_OUTPUT_DIR, '03_mse_overview.png'), dpi=300, bbox_inches='tight')
plt.close()
print(f"Saved: {ALT_OUTPUT_DIR}/03_mse_overview.png")

# --------------------------------------------------------------------------------
# --- Alternative Plot 4: RMSE Overview ---
# --------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(y_pred, y_true, color='blue', s=20, alpha=0.6, label='Actual Points ($y$)')
ax.plot([y_pred.min(), y_pred.max()], [y_pred.min(), y_pred.max()],
        color='gray', linestyle='--', label='Perfect Prediction ($y = \hat{y}$)')

# Plot horizontal error lines
for i in range(min(20, N)):
    ax.plot([y_pred[i], y_true[i]], [y_true[i], y_true[i]],
           color='purple', linestyle='-', linewidth=1, alpha=0.5)

rmse_formula = r'$\text{RMSE} = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2}$'
ax.text(0.95, 0.1, rmse_formula, transform=ax.transAxes, fontsize=14,
        verticalalignment='bottom', horizontalalignment='right',
        bbox=dict(boxstyle="round,pad=0.5", fc="lavender", alpha=0.7))

result_text = f'MAE: {mae_manual:.2f}\nMSE: {mse_manual:.2f}\nRMSE: {rmse_manual:.2f}'
ax.text(0.05, 0.95, result_text, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', horizontalalignment='left', color='purple', fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.4", fc="white", alpha=0.8))

ax.set_xlabel('Predicted Value ($\hat{y}$)', fontsize=12)
ax.set_ylabel('Actual Value ($y$)', fontsize=12)
ax.set_title('Root Mean Squared Error (RMSE): Alternative Orientation', fontsize=14, fontweight='bold')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(fontsize=10)
plt.tight_layout()
plt.savefig(os.path.join(ALT_OUTPUT_DIR, '04_rmse_overview.png'), dpi=300, bbox_inches='tight')
plt.close()
print(f"Saved: {ALT_OUTPUT_DIR}/04_rmse_overview.png")

# --------------------------------------------------------------------------------
# --- Alternative Plot 5: All Metrics Comparison ---
# --------------------------------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(14, 12))
axes = axes.flatten()

for idx, (y_t, y_p, title) in enumerate(scenarios):
    ax = axes[idx]
    errors = np.abs(y_t - y_p)
    
    ax.scatter(y_p, y_t, color='blue', s=10, alpha=0.5, zorder=3)
    ax.plot([y_p.min(), y_p.max()], [y_p.min(), y_p.max()], 
           color='gray', linestyle='--', linewidth=1.5, alpha=0.5)
    
    # Plot horizontal error lines
    for i in range(N):
        error_size = errors[i]
        color = 'red' if error_size > target_mae * 2 else 'darkorange'
        linewidth = 2 if error_size > target_mae * 2 else 0.5
        ax.plot([y_p[i], y_t[i]], [y_t[i], y_t[i]], 
               color=color, linestyle='-', linewidth=linewidth, alpha=0.6, zorder=2)
    
    errors_abs = np.abs(y_t - y_p)
    errors_sq = (y_t - y_p) ** 2
    mae = np.mean(errors_abs)
    mse = np.mean(errors_sq)
    rmse = np.sqrt(mse)
    
    metrics_text = f'MAE: {mae:.2f}\nMSE: {mse:.2f}\nRMSE: {rmse:.2f}'
    ax.text(0.05, 0.95, metrics_text, transform=ax.transAxes,
           fontsize=10, verticalalignment='top', horizontalalignment='left',
           bbox=dict(boxstyle="round,pad=0.4", fc="yellow", alpha=0.8), fontweight='bold')
    
    ax.set_xlabel('Predicted Value ($\hat{y}$)', fontsize=10)
    ax.set_ylabel('Actual Value ($y$)', fontsize=10)
    ax.set_title(title, fontsize=11, fontweight='bold')
    ax.grid(True, linestyle=':', alpha=0.6)

fig.suptitle('Metrics Comparison: Alternative Orientation', 
            fontsize=16, fontweight='bold', y=0.995)
plt.tight_layout()
plt.savefig(os.path.join(ALT_OUTPUT_DIR, '05_all_metrics_comparison.png'), dpi=300, bbox_inches='tight')
plt.close()
print(f"Saved: {ALT_OUTPUT_DIR}/05_all_metrics_comparison.png")

print("-" * 60)
print("Alternative plots generated successfully!")
