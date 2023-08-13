import json
from collections import defaultdict
from datetime import datetime, timedelta

class SmokingAnalytics:
    def __init__(self, json_file):
        self.json_file = json_file
        self.data = self.load_json()

    def load_json(self):
        with open(self.json_file, 'r') as file:
            data = json.load(file)
        return data

    def total_smoking_duration(self):
        total_duration = sum(
            instance['duration_seconds']
            for instances in self.data["smoking_instances"].values()
            for instance in instances
        )
        return total_duration

    def average_smoking_duration(self):
        total_duration = self.total_smoking_duration()
        total_instances = sum(
            len(instances)
            for instances in self.data["smoking_instances"].values()
        )
        average_duration = total_duration / total_instances
        return average_duration

    def most_frequent_smoking_time(self):
        smoking_time_counts = defaultdict(int)
        for instances in self.data["smoking_instances"].values():
            for instance in instances:
                smoking_time_counts[instance["time"]] += 1
        most_common_time = max(smoking_time_counts, key=smoking_time_counts.get)
        return most_common_time

    def longest_smoking_session(self):
        longest_duration = max(
            instance['duration_seconds']
            for instances in self.data["smoking_instances"].values()
            for instance in instances
        )
        return longest_duration

    def shortest_smoking_session(self):
        shortest_duration = min(
            instance['duration_seconds']
            for instances in self.data["smoking_instances"].values()
            for instance in instances
        )
        return shortest_duration

    def daily_smoking_frequency(self):
        day_frequency = defaultdict(int)
        for date, instances in self.data["smoking_instances"].items():
            day_frequency[date] = len(instances)
        return day_frequency
   
    def daily_total_smoking_duration(self):
        day_duration = defaultdict(int)
        for date, instances in self.data["smoking_instances"].items():
            day_duration[date] = sum(instance['duration_seconds'] for instance in instances)
        return day_duration

    def time_trends(self):
        time_data = defaultdict(lambda: {"duration": 0, "count": 0})
        for instances in self.data["smoking_instances"].values():
            for instance in instances:
                rounded_time = self.round_to_nearest_half_hour(instance["time"])
                time_data[rounded_time]["duration"] += instance['duration_seconds']
                time_data[rounded_time]["count"] += 1
        
        # Sort the times in chronological order
        sorted_times = sorted(time_data.keys(), key=lambda x: datetime.strptime(x, "%H:%M"))
        
        # Create a dictionary with sorted times and corresponding data
        sorted_time_data = {time: data for time, data in time_data.items() if data["count"] > 0}
        
        return sorted_time_data


    def round_to_nearest_half_hour(self, time):
        dt = datetime.strptime(time, "%H:%M")
        minutes = (dt.minute // 30) * 30
        rounded_time = dt.replace(minute=minutes, second=0, microsecond=0)
        return rounded_time.strftime("%H:%M")


    def day_of_week_analysis(self):
        day_frequency = defaultdict(int)
        for date, instances in self.data["smoking_instances"].items():
            day_name = datetime.strptime(date, "%Y-%m-%d").strftime("%A")
            day_frequency[day_name] += len(instances)
        return day_frequency

    def weekly_trends(self):
        weekly_duration = defaultdict(int)
        for date, instances in self.data["smoking_instances"].items():
            week_start = datetime.strptime(date, "%Y-%m-%d").date() - timedelta(days=datetime.strptime(date, "%Y-%m-%d").weekday())
            week_start = week_start.strftime("%Y-%m-%d")
            for instance in instances:
                weekly_duration[week_start] += instance['duration_seconds']
        return weekly_duration

    def monthly_trends(self):
        monthly_duration = defaultdict(int)
        for date, instances in self.data["smoking_instances"].items():
            month_start = datetime.strptime(date, "%Y-%m-%d").replace(day=1).strftime("%Y-%m-%d")
            for instance in instances:
                monthly_duration[month_start] += instance['duration_seconds']
        return monthly_duration
    
    def print_analytics(self):
        print("Smoking Analytics Summary\n")
        print("Total Smoking Duration:", self.total_smoking_duration(), "seconds")
        print("Average Smoking Duration: {:.2f} seconds".format(self.average_smoking_duration()))
        print("Most Frequent Smoking Time:", self.most_frequent_smoking_time())
        print("Longest Smoking Session:", self.longest_smoking_session(), "seconds")
        print("Shortest Smoking Session:", self.shortest_smoking_session(), "seconds")

        print("\nDaily Smoking Frequency:")
        for date, frequency in self.daily_smoking_frequency().items():
            print(f"{date}: {frequency} times")

        print("\nDaily Total Smoking Duration:")
        for date, duration in self.daily_total_smoking_duration().items():
            print(f"{date}: {duration} seconds")

        print("\nTime Trends:")
        for time, data in sorted(self.time_trends().items(), key=lambda x: datetime.strptime(x[0], "%H:%M")):
            duration = data["duration"]
            count = data["count"]
            print(f"{time}: Duration: {duration} seconds, Count: {count} times")


        print("\nDay of Week Analysis:")
        for day, frequency in self.day_of_week_analysis().items():
            print(f"{day}: {frequency} instances")

        print("\nWeekly Trends:")
        for week, duration in self.weekly_trends().items():
            print(f"Week starting {week}: {duration} seconds")

        print("\nMonthly Trends:")
        for month, duration in self.monthly_trends().items():
            print(f"Month starting {month}: {duration} seconds")

if __name__ == "__main__":
    analytics = SmokingAnalytics("instances.json")
    analytics.print_analytics()    