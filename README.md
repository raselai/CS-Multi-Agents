CrewAI Support System
This project implements an AI-powered support system using the CrewAI framework. It consists of two main agents: a Senior Support Representative and a Support Quality Assurance Specialist, working together to provide high-quality customer support.
Features

AI-powered support agents
Automated inquiry resolution
Quality assurance review process
Integration with external tools for web scraping and searching

Prerequisites

Python 3.x
CrewAI library
Langchain library
Groq API key

Installation

Clone this repository:
Copygit clone https://github.com/yourusername/crewai-support-system.git
cd crewai-support-system

Install the required dependencies:
Copypip install crewai langchain-groq python-dotenv

Create a .env file in the project root and add your Groq API key:
CopyGROQ_API_KEY=your_groq_api_key_here


Project Structure

agent.py: Defines the AI agents (Senior Support Representative and Support Quality Assurance Specialist)
tools.py: Contains tools for web scraping and searching
task.py: Defines the tasks for inquiry resolution and quality assurance review

Usage
To use this support system, you need to create a CrewAI instance and run the defined tasks. Here's a basic example:
pythonCopyfrom crewai import Crew
from task import inquiry_resolution, quality_assurance_review

# Create a Crew instance
crew = Crew(
    agents=[inquiry_resolution.agent, quality_assurance_review.agent],
    tasks=[inquiry_resolution, quality_assurance_review]
)

# Run the crew
result = crew.kickoff()
print(result)
Customization
You can customize the agents' roles, goals, and backstories in the agent.py file. Modify the tasks in task.py to adjust the inquiry resolution and quality assurance processes.
Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
License
This project is licensed under the MIT License - see the LICENSE file for details.
