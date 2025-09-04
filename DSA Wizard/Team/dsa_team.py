from autogen_agentchat.teams import RoundRobinGroupChat
from agents.problem_solver_agent import get_problem_solver_agent
from agents.Code_executor import get_code_executor_agent
from agents.problem_scraper import get_problem_scraper
from config.constants import TEXT_MENTION, MAX_TURNS
from autogen_agentchat.conditions import TextMentionTermination

problem_solver_ag = get_problem_solver_agent()
Code_executor_ag, docker = get_code_executor_agent()
prob_scraper = get_problem_scraper()

termination_Condition = TextMentionTermination(TEXT_MENTION)

def get_dsa_team():
    teams = RoundRobinGroupChat(
            participants = [prob_scraper, problem_solver_ag, Code_executor_ag],
            termination_condition = termination_Condition,
            max_turns = MAX_TURNS
        )
    return teams, docker
