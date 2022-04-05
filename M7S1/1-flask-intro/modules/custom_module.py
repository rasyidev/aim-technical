import pandas as pd
from IPython.display import display, Markdown

def get_http_info(r):
    display(Markdown(f"# HTTP Message"))
    display(Markdown(f"## r Headers / Response Message"))
    display(Markdown(f"""**{r.request.method}** {r.url} **{r.status_code}**"""))
    r_headers = dict(r.request.headers)
    df = pd.DataFrame(r_headers.values(), index=r_headers.keys())
    display(df.style.hide(axis="columns"))
    display(Markdown("<hr style='border:2px solid grey'>"))
    display(Markdown("## Response Headers / Response Message"))
    response_headers = dict(r.headers)
    df = pd.DataFrame(response_headers.values(), index=response_headers.keys())
    display(df.style.hide(axis="columns"))
    display(Markdown("### Response Body"))
    
    if r.headers['Content-Type'].split(";")[0] == 'application/json':
        display(r.json())
    else:
        display(r.text)
    