# RecSys Notes

links:

* <http://d2l.ai/chapter_recommender-systems/index.html>

## BPR

Summary:

* Pairwise loss function. Develop datasets with pairs of interactions, where 1 is a positive ("seen"/"rated highly") user-item interaction, and 0 is a negative ("not seen").
* Users, items represented as embeddings.
* Prediction is the dot product of the user and item embedding.
* Loss (see `from recbole.model.loss.BPRLoss`) is just:

```-torch.log(self.gamma + torch.sigmoid(pos_score - neg_score)).mean()```

breaking this down:

* `pos_score - neg_score` is the difference between the prediction for the "positive" item and the "negative" item
* `torch.sigmoid` scales this difference to the range 0--1. If `pos_score - neg_score` is large, this will be close to 1, and vice-versa.
* `-torch.log` converts the sigmoid to a loss (e.g., sigmoid values close to 0 will have high loss)
* `.mean()` averages the loss for the mini-batch
* (minor) `gamma` ensures we do not try to compute `log(0)`

## recbole

limitations:

* recbole fails to train a model with numpy 1.24 or greater ("AttributeError: module 'numpy' has no attribute 'float'."). Downgrade to 1.23
* mps doesn't seem to be supported, so fall back to cpu
