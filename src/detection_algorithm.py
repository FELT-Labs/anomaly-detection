"""Algorithm file used in the Ocean protocol algorithm."""
import matplotlib.pyplot as plt
import numpy as np
from feltlabs.config import TrainingConfig
from feltlabs.core.data import load_data
from feltlabs.model import load_model


def main():
    config = TrainingConfig(target_column=-1)
    model = load_model(config.custom_data_path, config.experimental)
    # Load data and train model
    X, y = load_data(config)
    model.fit(X, y)

    # Dictionary mapping model name to calculated value (e.g. {"Mean": 10, ...})
    values = {m.model_name: m.predict(None) for m in model.models}
    print(values)

    threshold = 2
    anomaly = abs((y - values["Mean"]) / values["Std"]) > threshold

    plt.figure(figsize=(10, 8))
    plt.plot(anomaly, label=f"Total anomalies: {sum(anomaly)}")
    for i, x in enumerate(np.nonzero(anomaly)[0]):
        plt.annotate(
            f"{x}",
            (x, 1),
            textcoords="offset points",
            xytext=(0, 2 + 10 * (i % 2)),
            ha="center",
        )

    plt.xlabel("Production Period")
    plt.ylabel("Anomaly")
    plt.yticks([0, 1], ["No", "Yes"])
    plt.legend(title="Status", loc=6)
    plt.title("Anomaly status for each period")
    plt.savefig(config.output_folder / "result.jpg")

    print(values["Mean"])


if __name__ == "__main__":
    main()
