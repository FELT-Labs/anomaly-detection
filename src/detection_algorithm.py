"""Algorithm file used in the Ocean protocol algorithm."""
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from feltlabs.config import TrainingConfig
from feltlabs.core.data import load_data
from feltlabs.model import load_model

sns.set_theme()


def main():
    config = TrainingConfig(data_type="csv", target_column=-1)
    model = load_model(config.custom_data_path, config.experimental)
    # Load data and train model
    X, y = load_data(config)

    # Dictionary mapping model name to calculated value (e.g. {"Mean": 10, ...})
    values = {m.model_name: m.predict(None) for m in model.models}
    print(values)

    threshold = 2
    anomaly = abs((y - values["Mean"]) / values["Std"]) > threshold

    plt.figure(figsize=(10, 7))
    plt.plot(anomaly, label=f"Total anomalies: {sum(anomaly)}")

    nonzero = np.nonzero(anomaly)[0]
    plt.scatter(nonzero, np.ones_like(nonzero), c="r")
    for x in nonzero:
        plt.annotate(
            f"{x}",
            (x, 1),
            textcoords="offset points",
            xytext=(0, 5),
            ha="center",
        )

    plt.xlabel("Production Period")
    plt.ylabel("Anomaly")
    plt.yticks([0, 1], ["No", "Yes"])
    plt.legend(title="Status", loc=6)
    plt.title("Anomaly status for each period")
    plt.savefig(config.output_folder / "result.jpg")


if __name__ == "__main__":
    main()
