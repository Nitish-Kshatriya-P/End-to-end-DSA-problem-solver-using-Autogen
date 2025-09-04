from autogen_agentchat.agents import AssistantAgent
from config.settings import get_model_client_2
from Tools.Web_scraper import get_web_scraper

mod_client = get_model_client_2()
tool = get_web_scraper()

def get_problem_scraper():
    problem_scraper_agent = AssistantAgent(
        name = "Problem_Fetcher_Agent",
        model_client = mod_client,
        system_message = '''
        You are an agent that fetches DSA problem from the web as fast as possible only on your first turn. 
        Use the get_web_scraper for calling the tool to scrape webpage.
        You will be provided with a URL to a DSA problem.
        Don't print the calling of youe web scraper tool on the screen.
        Print this only once in your first turn: "Scraping..."
        After the tool scrapes the DSA problem you will get the main bits from the scraped data (as mentioned below).
        And you will return the DSA problem in the following output.
        Return the DSA problem in the following format:
        1. Problem Title:
        2. Difficulty Level:
        3. Problem Description:
        4. Test Cases or Examples:
            1. #Test case/Example 1
            2. #Test case/Example 2
            3. #Test case/Example 3
        5. Constraints

        Directly you will print the information of the problem to the user in the above structured format after the problem is fetched internally.
        And pass the same details of this information to the problem_solver_ag.
        You should all the above only on your first turn.
        
        From your second turn do the below validation.
        If code executor agent did not execute the testcases properly then ask the problem solver agent to generate a new solution.
        Only after the code executor agent has completely executed all the 3 testcases successfully and after the python code is saved in a solution.py file.
        Once all of the above is done you have to say "STOP" to stop the conversation.
            ''',
        tools = [tool],
        reflect_on_tool_use= True,
        description = "An agent that fetches DSA problem from the given URL."   
    )

    return problem_scraper_agent