# app.py
import streamlit as st
import asyncio
from config.docker_handler import start_docker_container, stop_docker_container
from team.dsa_team import get_dsa_team
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult
from config.constants import ROLE_MAP
import os

st.set_page_config(page_title="DSA Wizard", page_icon = '🧙‍♂️')

st.title("🧙‍♂️ DSA Wizard : Welcome!! ")
st.write(" Which DSA problem's solution should I brew today?...")

# --- Friendly role mapping ---
ROLE = ROLE_MAP

# Input form
url = st.text_input(" Enter Your DSA Problem's URL and Click the 'Solve' button:", "", placeholder = "Paste URL here and engage my wizards")
start_btn = st.button("Solve")

# Chat container
chat_box = st.container()

if start_btn and url:
    async def run_solver(task_url: str):
        dsa_team, docker = get_dsa_team()
        try:
            await start_docker_container(docker)

            with chat_box:
                st.spinner("Wizards are solving the problem...")

            async for message in dsa_team.run_stream(task=task_url):
                if isinstance(message, TextMessage):
                    role = ROLE.get(message.source, message.source)
                    with chat_box:
                        if message.source.startswith("user"):
                            with st.chat_message("User:",avatar=role):
                                st.markdown(f"User: {message.content}")
                        elif message.source.startswith("Problem_Fetcher_Agent"):
                            with st.chat_message("Problem_Fetcher_Agent",avatar=role):
                                st.markdown(f"Wizard FA: {message.content}")
                        elif message.source.startswith("DSA_problem_solver_agent"):
                            with st.chat_message("DSA_problem_solver_agent",avatar=role):
                                st.markdown(f"Wizard PS: {message.content}")
                        elif message.source.startswith("Code_Executor_Agent"):
                            with st.chat_message("Code_Executor_Agent", avatar=role):
                                st.markdown(f"Wizard Exec: {message.content}")

                elif isinstance(message, TaskResult):
                    role = ROLE.get("Problem_Fetcher_Agent", "system")
                    with chat_box:
                        with st.chat_message(role):
                            st.markdown(f"Wizards are {message.stop_reason} brewing your solution.")

        except Exception as e:
            st.error(f"Error: {str(e)}")
        finally:
            await stop_docker_container(docker)

    # Run async loop safely inside Streamlit
    asyncio.run(run_solver(url))

    solution = "temp/solution.py"

    if os.path.exists(solution):
        with open("solution.py","r") as f:
            code = f.read()

        with chat_box:
            st.download_button("Download Solution.py", 
                               data = code, 
                               on_click = "ignore", 
                               icon = ":material/download:",
                               mime = "text/x-python")

    st.success("Problem Solved! 🎉")