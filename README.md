# Migrate Colab model training to Paperspace

 * Add dependencies from StyleGAN2 and forambulator
 * Add tfrecords for grayscaled 128x128 Mikrotax coccoliths
 * In theory we can now register and [run this model in Gradient-CI](https://docs.paperspace.com/gradient/tutorials/registering-models-in-gradient)

## Running an experiment

As per https://docs.paperspace.com/gradient/tutorials/registering-models-in-gradient after creating a project:

```
gradient experiments run singlenode \
  --name coccoliths \
  --projectId [GOES HERE] \
  --container tensorflow/tensorflow:1.9.0-gpu \
  --machineType Free-P5000 \
  --command "python train.py" \
  --modelType Tensorflow \
  --modelPath "/storage/model"
```
