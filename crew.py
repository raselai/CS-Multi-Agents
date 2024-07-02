from crewai import Crew, Process
from agents import support_agent, support_quality_assurance_agent
from task import inquiry_resolution, quality_assurance_review



crew = Crew(
  agents=[support_agent, support_quality_assurance_agent],
  tasks=[inquiry_resolution, quality_assurance_review],
  verbose=2,
  memory=True
)


inputs = {
    "customer": "DeepLearningAI",
    "person": "Nazmul Hoque",
    "inquiry": "How does this course prepare me for the current job market?"
            #    "and kicking it off, specifically "
            #    "how can I add memory to my crew? "
            #    "Can you provide guidance?"
}
result = crew.kickoff(inputs=inputs)
print(result)