from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

from main import process_logs_vectorized


def generate_error_chart(
    log_file: str = "app.log",
    output_image: str = "error_report.png",
) -> None:
    summary_df = process_logs_vectorized(Path(log_file))

    if summary_df.empty:
        print("Không có dữ liệu lỗi để vẽ biểu đồ.")
        return

    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(7, 4.5))

    sns.barplot(
        data=summary_df,
        x="level",
        y="count",
        palette="Blues_r",
        hue="level",
        legend=False,
    )

    plt.title(
        "Thống kê tần suất lỗi (Log Analysis)",
        fontsize=13,
        fontweight="bold",
    )
    plt.xlabel(
        "Mức độ lỗi (Log Level)",
        fontsize=11,
    )
    plt.ylabel(
        "Số lượng (Count)",
        fontsize=11,
    )
    plt.tight_layout()

    plt.savefig(output_image, dpi=300)
    plt.close()
    print(f"---> Đã xuất biểu đồ thành công: {output_image}")


if __name__ == "__main__":
    generate_error_chart()
