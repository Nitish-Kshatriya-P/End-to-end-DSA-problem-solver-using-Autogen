import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
from autogen_core.tools import FunctionTool


async def scraper(task: str) -> str:
    """ Return the DSA problem in the following format:
            1. Problem Title:
            2. Difficulty Level:
            3. Problem Description:
            4. Test Cases or Examples:
                1. #Test case/Example 1
                2. #Test case/Example 2
                3. #Test case/Example 3
            5. Constraints
    """
    try:
        async with AsyncWebCrawler() as crawler:

            result = await crawler.arun(task,
                                    config = CrawlerRunConfig(
                                        excluded_tags=['form', 'header', 'footer', 'nav'],
                                        exclude_external_links = True,
                                        exclude_social_media_links= True
                ))
            result_mark = result.markdown
    except Exception as e:
        error_msg = f"Error fetching from {task}: {str(e)}"
        print(error_msg)
        return error_msg
    
    return result_mark

def scrape():
    return asyncio.run(scraper())

fetch_prob = FunctionTool(scrape,
                          description="A tool to fetch the DSA problem from the given url.")

def get_web_scraper():
    return fetch_prob