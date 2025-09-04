MODEL1 = 'tngtech/deepseek-r1t2-chimera:free'
FAMILY1 = 'tngtech'
MODEL2 = 'moonshotai/kimi-k2:free'
FAMILY2 = 'moonshotai'
TEXT_MENTION = "DONE"
WORK_DIR = 'temp'
TIMEOUT = 120
MAX_TURNS = 20
ROLE_MAP = {
    "user": "😎",
    "Problem_Fetcher_Agent" : "👾",
    "DSA_problem_solver_agent": "👨‍💻",
    "Code_Executor_Agent": "🤖"
}