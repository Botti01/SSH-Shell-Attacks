# plotting_utils.py

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, precision_recall_curve, auc, f1_score
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

def plot_metrics_over_epochs(y_true, y_pred_probs, epochs):
    """Plot TPR, FPR, TNR, FNR over epochs."""
    metrics = {
        'TPR': [], 'FPR': [], 'TNR': [], 'FNR': []
    }
    
    for epoch_preds in y_pred_probs:
        epoch_pred_binary = (epoch_preds > 0.5).astype(int)
        tp = np.sum((y_true == 1) & (epoch_pred_binary == 1), axis=0)
        fp = np.sum((y_true == 0) & (epoch_pred_binary == 1), axis=0)
        tn = np.sum((y_true == 0) & (epoch_pred_binary == 0), axis=0)
        fn = np.sum((y_true == 1) & (epoch_pred_binary == 0), axis=0)
        
        metrics['TPR'].append(tp / (tp + fn))
        metrics['FPR'].append(fp / (fp + tn))
        metrics['TNR'].append(tn / (tn + fp))
        metrics['FNR'].append(fn / (fn + tp))
    
    # Now plot, averaging over the epochs
    plt.figure(figsize=(12, 8))
    for metric, values in metrics.items():
        # Take the mean across the epochs, and plot it
        plt.plot(range(1, epochs + 1), values, label=metric)
    
    plt.xlabel('Epoch')
    plt.ylabel('Rate')
    plt.title('Metrics Over Epochs')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_loss_curve(train_losses, val_losses):
    """Plot training and validation loss curves with log scale for better visualization."""
    plt.figure(figsize=(10, 6))
    plt.plot(train_losses, label='Training Loss')
    plt.plot(val_losses, label='Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Training and Validation Loss')
    plt.ylim(0, 0.1)  # Set y-axis limits from 0 to 0.5
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_roc_curves(y_true, y_pred_probs, class_names):
    """Plot ROC curves for each class."""
    plt.figure(figsize=(15, 10))
    for i in range(y_true.shape[1]):
        fpr, tpr, _ = roc_curve(y_true[:, i], y_pred_probs[:, i])
        roc_auc = auc(fpr, tpr)
        plt.plot(fpr, tpr, label=f'{class_names[i]} (AUC = {roc_auc:.2f})')
    
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curves for Each Class')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)
    plt.show()

def plot_pr_curves(y_true, y_pred_probs, class_names):
    """Plot Precision-Recall curves for each class."""
    plt.figure(figsize=(15, 10))
    for i in range(y_true.shape[1]):
        precision, recall, _ = precision_recall_curve(y_true[:, i], y_pred_probs[:, i])
        plt.plot(recall, precision, label=class_names[i])
    
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall Curves for Each Class')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)
    plt.show()

def plot_prob_histograms(y_pred_probs, class_names):
    """Plot histograms of prediction probabilities for each class."""
    n_classes = len(class_names)
    n_cols = 3
    n_rows = (n_classes + n_cols - 1) // n_cols
    
    plt.figure(figsize=(15, 5 * n_rows))
    for i in range(n_classes):
        plt.subplot(n_rows, n_cols, i + 1)
        plt.hist(y_pred_probs[:, i], bins=50)
        plt.title(f'Class: {class_names[i]}')
        plt.xlabel('Prediction Probability')
        plt.ylabel('Count')
    plt.tight_layout()
    plt.show()

def plot_3d_roc(y_true, y_pred_probs, class_names, n_classes=3):
    """Plot 3D ROC curve for the first three classes."""
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    for i in range(min(n_classes, len(class_names))):
        fpr, tpr, _ = roc_curve(y_true[:, i], y_pred_probs[:, i])
        ax.plot(fpr, tpr, zs=i, zdir='y', label=class_names[i])
    
    ax.set_xlabel('False Positive Rate')
    ax.set_ylabel('Class')
    ax.set_zlabel('True Positive Rate')
    ax.set_title('3D ROC Curve')
    plt.legend()
    plt.show()

def plot_f1_scores(y_true, y_pred_probs, class_names):
    """Plot class-wise F1 scores."""
    y_pred = (y_pred_probs > 0.5).astype(int)
    f1_scores = [f1_score(y_true[:, i], y_pred[:, i]) for i in range(len(class_names))]
    
    plt.figure(figsize=(12, 6))
    bars = plt.bar(class_names, f1_scores)
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('Class')
    plt.ylabel('F1 Score')
    plt.title('Class-wise F1 Scores')
    
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2f}',
                ha='center', va='bottom')
    plt.tight_layout()
    plt.show()

def plot_performance_metrics(y_true, y_pred_probs, class_names):
    """Plot precision, recall, and F1 score for each class."""
    y_pred = (y_pred_probs > 0.5).astype(int)
    metrics = {
        'Precision': [],
        'Recall': [],
        'F1': []
    }
    
    for i in range(len(class_names)):
        tp = np.sum((y_true[:, i] == 1) & (y_pred[:, i] == 1))
        fp = np.sum((y_true[:, i] == 0) & (y_pred[:, i] == 1))
        fn = np.sum((y_true[:, i] == 1) & (y_pred[:, i] == 0))
        
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0
        f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
        
        metrics['Precision'].append(precision)
        metrics['Recall'].append(recall)
        metrics['F1'].append(f1)
    
    x = np.arange(len(class_names))
    width = 0.25
    
    fig, ax = plt.subplots(figsize=(15, 8))
    ax.bar(x - width, metrics['Precision'], width, label='Precision')
    ax.bar(x, metrics['Recall'], width, label='Recall')
    ax.bar(x + width, metrics['F1'], width, label='F1')
    
    ax.set_ylabel('Score')
    ax.set_title('Model Performance Metrics by Class')
    ax.set_xticks(x)
    ax.set_xticklabels(class_names, rotation=45, ha='right')
    ax.legend()
    plt.tight_layout()
    plt.show()
