from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

client = tavilyClient(
    api_keys= os.getenv("TAVILY_API_KEY")
)


def tavily_search(query):
    response = client.search(
        query= query,
        max_result= 6
    )
    
    results= []
    
    for i, r in enumerate(response["results"], 1):
        title   =  r.get("title", "Unknown")
        url     =  r.get("url", "").strip()
        # kep only the first 200 characters to avoid wall_of_text
        if len(snippet) > 300:
            snippet = snippet[:200]. rsplit(" ", 1)[0] + "..."
            
            results.append(f"{i}. **{title}**\n  {url}\n  {snippet}")
            
    return "\n\n".join(results)

    