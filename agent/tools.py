from langchain_core.tools import tool
from ingestion.chat import ask_repo
import os 
from dotenv import load_dotenv
from tavily import TavilyClient
from github import Github
load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
def get_tools(repo_name: str, github_token: str = None):
    gh = Github(github_token) if github_token else None
    @tool
    def code_search(query:str)->str:
        """Search the codebase for ANYTHING related to the repo — functions, classes, 
    files, logic, implementation details. Use this for ANY question about the code
    including questions about specific files like 'tell me about rag.py' or 
    'what does main.py contain'."""
        return ask_repo(repo_name, query) 
    
    @tool
    def web_search(query:str)->str:
        """Search the web for external documentation, error explanations, 
        library usage, or anything not found in the codebase itself."""
        results = tavily.search(query, max_results=3)
        return results

    # @tool
    # def read_file(file_path: str) -> str:
    #         """Read a specific file from the repo by its path.
    #         Use when asked for the full content, "show me the entire file",Do NOT use for general questions"""
    #         repo = gh.get_repo(repo_name)
    #         try:
    #             content = repo.get_contents(file_path)
    #             return content.decoded_content.decode("utf-8")
    #         except Exception as e:
    #             return f"Could not read file {file_path}: {str(e)}"
    return [code_search, web_search]       