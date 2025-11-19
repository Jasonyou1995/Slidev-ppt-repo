# Regression Evaluation Metrics - Visualization Guide

This folder contains visualization plots for teaching regression evaluation metrics: MAE, MSE, and RMSE.

## Plot Files

### 01_mae_overview.png
**Purpose**: Introduction to Mean Absolute Error (MAE)
- Shows the basic concept of MAE
- Demonstrates how MAE calculates average absolute differences
- Visualizes error lines connecting actual to predicted values
- Includes MAE formula and all three metrics (MAE, MSE, RMSE) for comparison

**When to use**: Start your presentation with this plot to introduce MAE as the simplest metric.

**Slidev usage**:
```markdown
---
layout: center
---

# Mean Absolute Error (MAE)

![MAE Overview](01_mae_overview.png)
```

---

### 02_mae_limitation_comparison.png
**Purpose**: Demonstrates MAE's limitation with large errors
- Shows four scenarios with identical MAE (3.0) but different error distributions
- Highlights why MAE doesn't penalize large errors effectively
- Visual comparison: Normal errors vs. Extreme cases (half perfect/half large errors, few massive errors)
- Each subplot shows MAE value

**When to use**: After introducing MAE, use this to explain why we need other metrics that penalize large errors more.

**Slidev usage**:
```markdown
---
layout: center
---

# MAE Limitation

![MAE Comparison](02_mae_limitation_comparison.png)

All four scenarios have the same MAE, but very different error patterns!
```

---

### 03_mse_overview.png
**Purpose**: Introduction to Mean Squared Error (MSE)
- Shows how MSE squares errors to penalize large errors more
- Error line thickness represents squared error magnitude
- Demonstrates MSE's sensitivity to outliers
- Includes MSE formula and all three metrics (MAE, MSE, RMSE) for comparison

**When to use**: Introduce MSE as a solution to MAE's limitation. Show how it penalizes large errors more heavily.

**Slidev usage**:
```markdown
---
layout: center
---

# Mean Squared Error (MSE)

![MSE Overview](03_mse_overview.png)

MSE squares errors, making large errors much more costly!
```

---

### 04_rmse_overview.png
**Purpose**: Introduction to Root Mean Squared Error (RMSE)
- Shows RMSE as the square root of MSE
- Brings the metric back to original units (more interpretable)
- Still penalizes large errors like MSE
- Includes RMSE formula and all three metrics (MAE, MSE, RMSE) for comparison

**When to use**: Explain RMSE as a more interpretable version of MSE that maintains the same penalty structure.

**Slidev usage**:
```markdown
---
layout: center
---

# Root Mean Squared Error (RMSE)

![RMSE Overview](04_rmse_overview.png)

RMSE = √MSE: Same penalty structure, but in original units!
```

---

### 05_all_metrics_comparison.png
**Purpose**: Comprehensive comparison of all three metrics across different error patterns
- Same four scenarios as plot 02 (same MAE, different error distributions)
- Shows MAE, MSE, and RMSE for each scenario side-by-side
- Demonstrates how MSE and RMSE differ dramatically even when MAE is the same
- Perfect for showing why squared metrics (MSE/RMSE) are better at detecting extreme errors

**When to use**: After introducing all three metrics, use this to show how they compare across different error patterns. This clearly demonstrates why MSE/RMSE are preferred when large errors matter.

**Slidev usage**:
```markdown
---
layout: center
---

# All Metrics Comparison

![All Metrics](05_all_metrics_comparison.png)

Notice how MSE and RMSE differ dramatically even when MAE is identical!
```

---

## Recommended Presentation Order

1. **01_mae_overview.png** - Start with MAE (simplest concept, shows all metrics)
2. **02_mae_limitation_comparison.png** - Show why MAE isn't perfect
3. **03_mse_overview.png** - Introduce MSE as a solution (shows all metrics)
4. **04_rmse_overview.png** - Show RMSE as an interpretable alternative (shows all metrics)
5. **05_all_metrics_comparison.png** - Compare all three metrics across scenarios

## Slidev Integration Tips

### Using Images in Slidev

1. **Relative Path**: If your `slides.md` is in the parent directory:
   ```markdown
   ![MAE](img/01_mae_overview.png)
   ```

2. **Full Path**: For absolute paths:
   ```markdown
   ![MAE](/path/to/img/01_mae_overview.png)
   ```

3. **With Layouts**: Combine with Slidev layouts:
   ```markdown
   ---
   layout: image-right
   image: img/01_mae_overview.png
   ---
   
   # Mean Absolute Error
   
   MAE measures the average magnitude of errors...
   ```

4. **Two-Column Layout**: Compare metrics side-by-side:
   ```markdown
   ---
   layout: two-cols
   ---
   
   # MAE vs MSE
   
   ::left::
   ![MAE](img/01_mae_overview.png)
   
   ::right::
   ![MSE](img/03_mse_overview.png)
   ```

### Best Practices

- **High Resolution**: All plots are saved at 300 DPI for crisp presentation
- **Consistent Style**: All plots use the same color scheme and formatting
- **Clear Labels**: Formulas and results are clearly annotated
- **Grid Layout**: Use the 2x2 comparison plot to show multiple concepts at once

## Technical Details

- **Format**: PNG (300 DPI)
- **Color Scheme**: 
  - Blue: Predicted points
  - Gray: Perfect prediction line
  - Orange/Red: Error lines (red for large errors)
- **Font Size**: Optimized for presentation viewing
- **Aspect Ratio**: 8:6 (suitable for slides)

## Alternative Plots (Predicted on X-axis, Actual on Y-axis)

An alternative set of plots is available in the `alternative/` subfolder with swapped axes:
- **X-axis**: Predicted Value ($\hat{y}$)
- **Y-axis**: Actual Value ($y$)

### When to Use Alternative Orientation

Some practitioners prefer this orientation because:
- It follows the traditional regression convention (predictor on X, response on Y)
- Horizontal error lines may be more intuitive for some audiences
- Emphasizes how actual values vary with predictions

### Differences from Main Plots

- **Error lines**: Horizontal instead of vertical
- **Interpretation**: Points to the right of diagonal = overprediction, left = underprediction
- **Same metrics**: All calculations remain identical, only visualization differs

### Available Alternative Plots

All five plots are available in `alternative/`:
- `alternative/01_mae_overview.png`
- `alternative/02_mae_limitation_comparison.png`
- `alternative/03_mse_overview.png`
- `alternative/04_rmse_overview.png`
- `alternative/05_all_metrics_comparison.png`

**Note**: The main plots (Actual on X, Predicted on Y) are recommended for teaching error metrics because vertical error lines align naturally with the concept of "error magnitude" and make it easier to visualize MAE/MSE/RMSE calculations. However, both conventions are valid and you may choose based on your audience's preferences or field conventions.

## Regenerating Plots

To regenerate all plots (including alternatives), run:
```bash
python plots.py
```

All plots will be saved automatically:
- Main plots → `img/` folder
- Alternative plots → `img/alternative/` folder

