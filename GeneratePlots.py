import os
import matplotlib.pyplot as plt
from SmokingAnalytics import SmokingAnalytics
from datetime import datetime  # Import datetime moduleimport os

class GeneratePlots:
    def __init__(self, analytics, output_folder):
        self.analytics = analytics
        self.output_folder = output_folder

    def plot_combined_chart(self):
        daily_frequency = self.analytics.daily_smoking_frequency()
        daily_duration = self.analytics.daily_total_smoking_duration()

        plt.figure(figsize=(10, 5))
        plt.plot(daily_frequency.keys(), daily_frequency.values(), color='blue', marker='o', label='Daily Frequency')
        plt.plot(daily_duration.keys(), daily_duration.values(), color='green', marker='o', label='Total Duration')
        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.title('Combined Daily Smoking Frequency and Total Duration')
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()

        combined_chart_filename = os.path.join(self.output_folder, "combined_chart.png")
        plt.savefig(combined_chart_filename)
        plt.close()

    def plot_time_trends(self):
        plt.figure(figsize=(10, 5))
        time_trends = self.analytics.time_trends()

        times = list(time_trends.keys())
        count = [data["count"] for data in time_trends.values()]
        duration = [data["duration"] for data in time_trends.values()]

        # Convert times to datetime objects for sorting
        sorted_times = sorted([datetime.strptime(time, "%H:%M") for time in times])

        # Convert sorted times back to strings
        sorted_times_str = [time.strftime("%H:%M") for time in sorted_times]

        # Reorder count and duration lists based on sorted times
        sorted_count = [count[times.index(time)] for time in sorted_times_str]
        sorted_duration = [duration[times.index(time)] for time in sorted_times_str]

        plt.bar(sorted_times_str, sorted_count, color='blue', label='Count')
        plt.plot(sorted_times_str, sorted_duration, color='orange', marker='o', label='Duration (seconds)')

        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.title('Time Trends')
        plt.xticks(rotation=45)
        plt.legend()
        plt.tight_layout()

        time_trends_chart_filename = os.path.join(self.output_folder, "time_trends_chart.png")
        plt.savefig(time_trends_chart_filename)
        plt.close()


    def plot_day_of_week_analysis(self):
        plt.figure(figsize=(7, 5))
        day_of_week_analysis = self.analytics.day_of_week_analysis()
        plt.bar(day_of_week_analysis.keys(), day_of_week_analysis.values(), color='green')
        plt.xlabel('Day of Week')
        plt.ylabel('Instances')
        plt.title('Day of Week Analysis')
        plt.xticks(rotation=45)
        plt.tight_layout()

        day_of_week_chart_filename = os.path.join(self.output_folder, "day_of_week_chart.png")
        plt.savefig(day_of_week_chart_filename)
        plt.close()

    def generate_all_plots(self):
        self.plot_combined_chart()
        self.plot_time_trends()
        self.plot_day_of_week_analysis()


if __name__ == "__main__":
    diagram_output_folder = "LatestDiagrams"  # Specify the output folder
    analytics = SmokingAnalytics("instances.json")
    plot_generator = GeneratePlots(analytics, diagram_output_folder)
    plot_generator.generate_all_plots()
