### Hyper parameter Tuning in ML

<p>Hyperparameter tuning is the process of selecting the best set of hyperparameters for a machine learning model. Hyperparameters are configuration settings set before training begins (unlike model parameters that are learned from the data during training).</p>

#### Examples of hyperparameters:

- Learning rate
- Number of hidden layers in a neural network
- Number of trees in a random forest
- Regularization strength
- Batch size

<p>The goal of tuning is to find the hyperparameters that give the best performance on a validation set (i.e., data not used during training).</p>

### Practical Example: Hyperparameter Tuning with a Random Forest

**Problem**: Classify whether a patient has diabetes based on medical data (using the popular Pima Indians Diabetes dataset).
