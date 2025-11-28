# Resume-Screening-Agent

A small Streamlit app that evaluates resumes against a Job Description using the Groq API.

## Setup (Windows / PowerShell)

1. Create and activate a virtual environment in the project folder:

```powershell
python -m venv venv
venv\Scripts\activate
```

2. Install requirements (we include `groq` and `python-dotenv`):

```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

3. Add your Groq API key.

You can set the key in several ways on Windows / PowerShell — pick whichever suits your workflow.

- Recommended (local development): create a `.env` file in the project root with:

```text
# .env
GROQ_API_KEY=your_real_groq_key_here
```

 - Temporary (current PowerShell session only):

```powershell
$env:GROQ_API_KEY = "your_real_groq_key_here"
```

 - Persistent for the current user (requires restarting the shell):

```powershell
setx GROQ_API_KEY "your_real_groq_key_here"
```

 - (Optional) Add to your virtual environment activation script so the variable is set when you activate the venv. For PowerShell, you can add this to `venv\Scripts\Activate.ps1` (BE CAREFUL and do not commit real keys):

```powershell
# inside venv\Scripts\Activate.ps1
$env:GROQ_API_KEY = "your_real_groq_key_here"
```

Note: Do not commit your real API key to source control. An example `.env.example` file is provided.

4. Run the app:

```powershell
streamlit run app.py
```

If `groq` is missing for any reason, you can also install it directly using `pip install groq`.

## Notes
- `utils.py` now reads your Groq key from `GROQ_API_KEY` via `python-dotenv` (if `.env` present) or your environment.
- `evaluate_resume()` returns JSON output. `app.py` parses safely and falls back to showing the raw model output if parsing fails.
 - `evaluate_resume()` uses a model name you can configure via the `GROQ_MODEL` environment variable.
	 By default the project uses `llama3-8b-8192`. If you see an error like:
	 ```txt
	 The model `llama3-13b-8k` does not exist or you do not have access to it
	 ```
	 that means your Groq account doesn't have access to the requested model. Fixes:
	 1. Set `GROQ_MODEL` to a model you have access to (e.g. `llama3-8b-8192`) in `.env` or your shell.
	 2. Request access to the model from Groq.
	 3. Or choose a different, commonly-available model in the repo.

Note: The app will automatically retry using a safe fallback model (`llama3-8b-8192`) if the model configured in `GROQ_MODEL` is not available to your Groq account. If the fallback fails as well the app will show a clear error explaining the next steps.