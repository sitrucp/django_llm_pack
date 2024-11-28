# Django LLM Pack

Django LLM Pack is a simple python tool that simplifies the process of extracting relevant code from your Django project for analysis with Large Language Models (LLMs) such as Claude, ChatGPT or Gemini.

It is inspired by Repomix ([https://github.com/yamadashy/repomix](https://github.com/yamadashy/repomix)) which is a similar tool but for javascript applications.

I used Repomix on itself, and gave the output to ChatGPT, prompting it to generate a version specifically for Django apps.

**How to use it:**

1. **Modify configuration:** 
    - `CODE_EXTENSIONS`: A list of file extensions to include in the output (e.g., `.py`, `.html`, `.css`).
    - `EXCLUDE_DIRS`: Directories to exclude from the extraction (e.g., `venv`, `static`).
    - `USER_EXCLUDE_PATHS`: Additional specific paths to exclude, which might not be covered by `EXCLUDE_DIRS`.
	
2. **Run the code:** Execute the script.

3. **Project Path:** Enter the path to your Django project directory when prompted.

4. **Output:** The script will generate a single file named `django_code.txt` within your Django project directory. This file will contain the condensed Django project code.

5. **LLM Analysis:** Upload the `django_code.txt` file to your chosen LLM for further analysis, discussion, or to ask specific questions about your code.

