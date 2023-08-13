
from GeneratePlots import GeneratePlots
from InstanceUpdate import InstanceUpdate
from SmokingAnalytics import SmokingAnalytics

if __name__ == "__main__":
    diagram_output_folder = "LatestDiagrams"
    auto_generate = False
    if input("New Entry? (y)").lower() == 'y':
        InstanceUpdate()
        auto_generate = True
    analytics = SmokingAnalytics("instances.json")
    analytics.print_analytics()

    if auto_generate: # new instance, auto generate
        GeneratePlots(analytics, diagram_output_folder).generate_all_plots()
    else: 
        if input("Generate New Plot? (y)").lower() == 'y':
            GeneratePlots(analytics, diagram_output_folder).generate_all_plots()
