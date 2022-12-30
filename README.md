# Anomaly Detection
**Anomaly detection demo for SBIC 2022**

<a target="_blank" href="https://colab.research.google.com/github/https://colab.research.google.com/github/FELT-Labs/anomaly-detection/blob/main/main.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

[**Anomaly Detection on YouTube:**](http://www.youtube.com/watch?v=IKwxdvDpu6A)  
[![Demo video on YouTube](http://img.youtube.com/vi/IKwxdvDpu6A/hqdefault.jpg)](http://www.youtube.com/watch?v=IKwxdvDpu6A)


## Introduction
Anomaly detection is common problem found in many different industries. This repository demonstrates usage of FELT for anomaly detection on distributed data. You can image 3 factories each producing same product (cables in our case). Using FELT and Ocean Protocol we can calculate statistics across all datasets without revealing data itself. After that we can use those statistics for detecting anomalies in each factory.

### Requirements
Using version `0.5.1` of FELT Labs application. more requirements are listed in [requirements.txt](./requirements.txt).

### Datasets
You can find the dataset files in [datasets](./datasets/) folder. Same files are published on Ocean Protocol as 3 different datasets. With following DIDs:

1. [did:op:493def4e00cda410adde2017ebaf5d644cf2bdec81cec5fee29d1fc9c73d66fa](https://market.oceanprotocol.com/asset/did:op:493def4e00cda410adde2017ebaf5d644cf2bdec81cec5fee29d1fc9c73d66fa)
2. [did:op:9e7f56f83422b156c016fe83e87722dac4b882ba9cd03f6d88e39fea04495669](https://market.oceanprotocol.com/asset/did:op:9e7f56f83422b156c016fe83e87722dac4b882ba9cd03f6d88e39fea04495669)
3. [did:op:53ffd278eff009d92a130db6f3b7415158d17f176ceef8114b0071bf6ec40a88](https://market.oceanprotocol.com/asset/did:op:53ffd278eff009d92a130db6f3b7415158d17f176ceef8114b0071bf6ec40a88)

Data are created from [this dataset](https://www.kaggle.com/datasets/osroru/copper-wire-production-line-dataset). This data captures basic properties from copper wire production line. Each line in this dataset represents one production period.

### Algorithm
Algorithm used for final evaluation is in [src/detection_algorithm.py](./src/detection_algorithm.py). We published this file as Ocean Protocol asset with following DID:

* [did:op:782ffe6742573ae168dc448b2e0cbe393ffbf7840ca03456f482ee48b8fcb743](https://market.oceanprotocol.com/asset/did:op:782ffe6742573ae168dc448b2e0cbe393ffbf7840ca03456f482ee48b8fcb743)

The algorithm works as follows. Based on the trained model (containing value of mean and standard deviation), we calculate z-score for each data point:

$$
\text{z-score} = \frac{x - mean}{\sigma}
$$

Then we assume that point is anomaly if z-score is greater than 2. Finally, the algorithm creates simple chart and stores the results.


# Usage - Decentralized
## Federated Analytics
1. Go to FELT web application: <https://app.feltlabs.ai/multiple> (you will need to connect Meta Mast)
2. Pick name and fill following DIDs of our datasets:
    * [did:op:493def4e00cda410adde2017ebaf5d644cf2bdec81cec5fee29d1fc9c73d66fa](https://market.oceanprotocol.com/asset/did:op:493def4e00cda410adde2017ebaf5d644cf2bdec81cec5fee29d1fc9c73d66fa)
    * [did:op:9e7f56f83422b156c016fe83e87722dac4b882ba9cd03f6d88e39fea04495669](https://market.oceanprotocol.com/asset/did:op:9e7f56f83422b156c016fe83e87722dac4b882ba9cd03f6d88e39fea04495669)
    * [did:op:53ffd278eff009d92a130db6f3b7415158d17f176ceef8114b0071bf6ec40a88](https://market.oceanprotocol.com/asset/did:op:53ffd278eff009d92a130db6f3b7415158d17f176ceef8114b0071bf6ec40a88)
3. In next step pick `Analytics` and select both `Mean` and `Standard deviation`
4. In the last step leave target column equal to `-1` and start the training 

This will start local jobs for each dataset. In order to combine local results into final model. Do following:

5. Go to: <https://app.feltlabs.ai/jobs>
6. Open up you job and click `Reload` until all jobs finished
7. Click `Aggregation` button at bottom to create final model
8. Wait for aggregation to finished (use `Reload` button) and download the final model

## Evaluation of Final Model
We already published the algorithm for evaluation. We just need to run it on our data.
1. Go to: <https://app.feltlabs.ai/experimental>
2. Pick name, **upload final model** and fill following DIDs:
    * Data: [did:op:493def4e00cda410adde2017ebaf5d644cf2bdec81cec5fee29d1fc9c73d66fa](https://market.oceanprotocol.com/asset/did:op:493def4e00cda410adde2017ebaf5d644cf2bdec81cec5fee29d1fc9c73d66fa)
    * Algorithm: [did:op:782ffe6742573ae168dc448b2e0cbe393ffbf7840ca03456f482ee48b8fcb743](https://market.oceanprotocol.com/asset/did:op:782ffe6742573ae168dc448b2e0cbe393ffbf7840ca03456f482ee48b8fcb743)
3. Start the algorithm using `Run` button
4. Go to: <https://app.feltlabs.ai/jobs>
5. Wait until your compute job is finished (use `Reload` button) and then download `result.jpg` with final chart


# Usage - Local
This simulates the decentralized process in local environment.

## Install
Install Python 3.8 or newer.
```bash
pip install -r requirements.txt
# In case you want to contribute to repository run following as well:
pre-commit install
```
Then you can start jupyter lab/notebook as follows:
```bash
jupyter lab
```

### Using Makefile
Alternatively, you can use [Makefile](./Makefile) which will create virtual environment and install requirements for you. Using following command:
```bash
make install
```

## Main file
Once you have requirements installed and jupyter running. You can open [main.ipynb](./main.ipynb) which will walk you through the main usage of FELT.

You can also open the notebook in Google Colab:

<a target="_blank" href="https://colab.research.google.com/github/https://colab.research.google.com/github/FELT-Labs/anomaly-detection/blob/main/main.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>
