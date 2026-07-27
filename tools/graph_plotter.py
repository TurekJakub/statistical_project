#!/usr/bin/env python3

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

root_dir = Path(__file__).resolve().parents[1]
sys.path.append(str(root_dir))

from src.playoffs import prepare_playoff_dataset
from src.regular import prepare_regular_season_dataset
from src.teams_division import assign_group_labels


def plot_graphs(is_regular_season: bool, output_path: str):
    data = (
        prepare_regular_season_dataset()
        if is_regular_season
        else prepare_playoff_dataset()
    )
    assign_group_labels(data)

    stage_label = "základní části" if is_regular_season else "playoff"

    data["Origin"] = data["Origin"].replace({"Canada": "Kanada"})
    data["Tradition"] = data["Tradition"].replace(
        {"Traditional": "Tradiční", "Expansion": "Expanzní"}
    )
    data["Taxation"] = data["Taxation"].replace(
        {"Low": "Nízká", "Medium": "Střední", "High": "Vysoká"}
    )

    sns.set_theme(style="darkgrid")

    _, ax = plt.subplots(1, 3, figsize=(16, 9))

    graph_args = [
        ["Origin", "Blues", "Země původu", ["Kanada", "USA"], "země původu"],
        [
            "Tradition",
            "Greens",
            "Tradice",
            ["Tradiční", "Expanzní"],
            "hokejové tradice",
        ],
        [
            "Taxation",
            "Oranges",
            "Daňová zátěž",
            ["Nízká", "Střední", "Vysoká"],
            "daňové zátěže",
        ],
    ]

    for idx, arg in enumerate(graph_args):
        ax[idx].set_xlabel(arg[2], fontsize=14)
        ax[idx].set_title(f"Úspěšnost v {stage_label} dle {arg[4]}", fontsize=15)

        if is_regular_season:
            ax[idx].set_ylabel("Úspěšnost", fontsize=14)
            sns.violinplot(
                data=data,
                x=arg[0],
                y="Performance",
                hue=arg[0],
                ax=ax[idx],
                palette=arg[1],
                legend=False,
                order=arg[3],
            )
            sns.stripplot(
                data=data,
                x=arg[0],
                y="Performance",
                color="black",
                alpha=0.3,
                jitter=0.2,
                size=4,
                ax=ax[idx],
                order=arg[3],
            )
        else:
            ax[idx].set_ylabel("Celkový počet startů v lize", fontsize=14)
            sns.countplot(
                data=data,
                x=arg[0],
                hue="Performance",
                ax=ax[idx],
                palette=arg[1],
                order=arg[3],
            )
            ax[idx].legend(title="Vyhraných kol playoff", loc="upper left")

    plt.tight_layout()
    plt.savefig(output_path)


def main():
    plot_graphs(True, "docs/images/regular_season_plot.png")
    plot_graphs(False, "docs/images/playoffs_plot.png")


if __name__ == "__main__":
    main()
