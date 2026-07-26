from numpy import mean
from scipy import stats

from teams_division import assign_group_labels, group_data_by


def perform_permutation_test(
    data: tuple, test_name: str, use_rank_statistic: bool = True
):
    multiple_groups = len(data) > 2

    test_statistic = None
    if multiple_groups:
        if use_rank_statistic:
            test_statistic = kruskal_statistic
        else:
            test_statistic = f_statistic
    else:
        if use_rank_statistic:
            test_statistic = mann_whitney_u_statistic
        else:
            test_statistic = mean_diff_statistic

    results = stats.permutation_test(
        data,
        test_statistic,
        permutation_type="independent",
        alternative="greater" if multiple_groups else "two-sided",
        random_state=42,
    )

    report_test_results(test_name, results)


def perform_t_test(data: tuple, test_name: str):
    report_test_results(test_name, stats.ttest_ind(data[0], data[1], equal_var=False))


def perform_all_tests(dataset, is_regular_season: bool):
    test_name_prefix = "Regular season" if is_regular_season else "Play off"
    test_fnc = perform_t_test if is_regular_season else perform_permutation_test

    assign_group_labels(dataset)

    grouped_by_tax = group_data_by(
        dataset, "Taxation", ["Low", "Medium", "High"], "Performance"
    )
    grouped_by_origin = group_data_by(
        dataset, "Origin", ["Canada", "USA"], "Performance"
    )
    grouped_by_tradition = group_data_by(
        dataset, "Tradition", ["Traditional", "Expansion"], "Performance"
    )

    test_fnc(grouped_by_origin, f"{test_name_prefix} by origin")
    test_fnc(
        grouped_by_tradition,
        f"{test_name_prefix} by tradition",
    )
    perform_permutation_test(
        grouped_by_tax, f"{test_name_prefix} by taxation", not is_regular_season
    )


def f_statistic(*samples):
    return stats.f_oneway(*samples).statistic


def mann_whitney_u_statistic(x, y):
    return stats.mannwhitneyu(x, y).statistic


def kruskal_statistic(*samples):
    return stats.kruskal(*samples).statistic


def mean_diff_statistic(x, y):
    return mean(x) - mean(y)


def report_test_results(test_name: str, test_result):
    print(f"=== {test_name} ===")
    print(f"P-value: {test_result.pvalue:.4f}")
    print(f"Test statistic: {test_result.statistic:.4f}")
    print("=" * (len(test_name) + 8), end="\n\n")
