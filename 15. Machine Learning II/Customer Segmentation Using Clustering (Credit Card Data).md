# Lab: Customer Segmentation Using Clustering (Credit Card Data)

## 1. Lab Title & Objectives

### Lab Title  
**Customer Segmentation with Unsupervised Clustering**

### Objectives  
In this lab, you will practice applying **unsupervised clustering algorithms** to a real-world dataset.  
The focus is on **data preparation, algorithm choice, and interpretation**, not on prediction accuracy.

By the end of this lab, you should understand:
- How clustering differs from supervised learning
- How preprocessing decisions affect clustering results
- How to interpret clusters from a **data science and business perspective**

This lab is **exploratory**: there are no labels and no “correct” answers.

---

## 2. Dataset Overview

### Business Context  
The dataset represents **credit card usage behavior** of active customers.  
The business goal is **customer segmentation** to support marketing strategy, such as:
- identifying high-value customers
- understanding spending patterns
- tailoring products or offers

### Dataset Description  
- Approximately **9000 credit card holders**
- Behavior summarized over the **last 6 months**
- **Customer-level** data (one row per customer)
- **18 numerical features** describing usage patterns

Each feature reflects **how customers use their credit cards**, not who they are.

---

## 3. High-Level Data Science Workflow (MANDATORY)

When clustering real data, a data scientist typically follows these steps:

- **Understand the data**
  - What does each feature represent?
  - What kind of behavior might it capture?

- **Clean and preprocess**
  - Handle missing values
  - Remove non-informative identifiers

- **Scale features**
  - Ensure all variables contribute fairly to distance calculations

- **Choose a clustering algorithm**
  - Based on data size, assumptions, and interpretability

- **Evaluate clustering quality**
  - Use diagnostic tools (not ground truth)
  - Balance metrics with interpretability

- **Interpret clusters**
  - Translate numeric patterns into meaningful profiles
  - Relate clusters to the business context

Clustering is **iterative**: insights often lead back to earlier steps.

---

## 4. Data Preparation Steps

Before applying clustering, consider the following steps:

- **Handling missing values**
  - Identify features with missing values
  - Decide whether to impute, remove rows, or remove features
  - Consider how missingness may reflect customer behavior

- **Removing identifier columns**
  - Drop columns such as customer IDs
  - Identifiers do not carry behavioral information and can distort clustering

- **Feature scaling**
  - Apply standardization or normalization
  - Required because clustering relies on distance calculations
  - Without scaling, features with large numeric ranges dominate

- **Optional: Dimensionality reduction (PCA)**
  - Can help with visualization
  - Can reduce noise and redundancy
  - Should be used carefully to preserve interpretability

---

## 5. Clustering Algorithms to Practice

### K-Means (Mandatory)

Why K-Means:
- Simple and widely used
- Scales well to large datasets
- Easy to interpret cluster centroids

Key assumptions:
- Clusters are roughly spherical
- Distance to the cluster center is meaningful
- Features are properly scaled
w
What to observe:
- How cluster centers differ
- How customers are distributed across clusters
- Sensitivity to the number of clusters

### Optional (Brief Exploration)
- **Hierarchical Clustering**: useful for visualizing cluster structure
- **DBSCAN**: useful for detecting noise and irregular clusters

These are optional extensions if time allows.

---

## 6. Model Selection & Evaluation

Because clustering is unsupervised, evaluation is **diagnostic**, not definitive.

Common approaches:
- **Elbow method**
  - Look at how within-cluster variation decreases
  - Identify diminishing returns when adding more clusters

- **Silhouette score**
  - Measures separation between clusters
  - Higher values suggest better-defined clusters

- **Practical interpretability**
  - Can you explain clusters meaningfully?
  - Do clusters differ in important behavioral features?

Final choice of number of clusters should balance:
- Quantitative signals
- Business usefulness
- Simplicity

---

## 7. Cluster Interpretation

After clustering, focus on **understanding the clusters**:

- **Profile clusters**
  - Compute average values of features per cluster
  - Identify dominant behaviors (e.g., high spending, frequent cash advances)

- **Translate to business meaning**
  - Describe clusters in plain language
  - Example: “Low balance, frequent installment users”

- **Avoid over-interpretation**
  - Clusters describe patterns, not individuals
  - Boundaries between clusters are not absolute

**Important reminder:**  
Clusters are **descriptive**, not ground truth.

---

## 8. Expected Learning Outcomes

After completing this lab, you should be able to:

- Explain how clustering differs from supervised learning
- Prepare real-world behavioral data for clustering
- Apply K-Means and justify preprocessing choices
- Reason about the number of clusters
- Interpret clusters in a business-relevant way
- Critically question clustering results and limitations

---

## 9. Optional Extensions (Bonus)

If time permits, explore one or more of the following:

- Compare K-Means with another clustering algorithm
- Visualize clusters using PCA
- Study how changing feature scaling affects clusters
- Propose hypothetical marketing strategies for each cluster
- Analyze cluster stability under different random initializations

---

### Final Note

This lab is about **thinking like a data scientist**, not finding a single correct answer.  
Your reasoning and interpretation matter more than the algorithm itself.
