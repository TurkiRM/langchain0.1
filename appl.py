{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "d349b74e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting langchain\n",
      "  Obtaining dependency information for langchain from https://files.pythonhosted.org/packages/b0/58/9a8777dff52bf5485c391cf3951e3d3b787afdc5967b29e25694ea014377/langchain-0.1.12-py3-none-any.whl.metadata\n",
      "  Downloading langchain-0.1.12-py3-none-any.whl.metadata (13 kB)\n",
      "Requirement already satisfied: PyYAML>=5.3 in c:\\users\\user\\anaconda3\\lib\\site-packages (from langchain) (6.0.1)\n",
      "Requirement already satisfied: SQLAlchemy<3,>=1.4 in c:\\users\\user\\anaconda3\\lib\\site-packages (from langchain) (2.0.21)\n",
      "Requirement already satisfied: aiohttp<4.0.0,>=3.8.3 in c:\\users\\user\\anaconda3\\lib\\site-packages (from langchain) (3.8.5)\n",
      "Collecting dataclasses-json<0.7,>=0.5.7 (from langchain)\n",
      "  Obtaining dependency information for dataclasses-json<0.7,>=0.5.7 from https://files.pythonhosted.org/packages/91/ca/7219b838086086972e662c19e908694bdc6744537fb41b70392501b8b5e4/dataclasses_json-0.6.4-py3-none-any.whl.metadata\n",
      "  Downloading dataclasses_json-0.6.4-py3-none-any.whl.metadata (25 kB)\n",
      "Collecting jsonpatch<2.0,>=1.33 (from langchain)\n",
      "  Obtaining dependency information for jsonpatch<2.0,>=1.33 from https://files.pythonhosted.org/packages/73/07/02e16ed01e04a374e644b575638ec7987ae846d25ad97bcc9945a3ee4b0e/jsonpatch-1.33-py2.py3-none-any.whl.metadata\n",
      "  Downloading jsonpatch-1.33-py2.py3-none-any.whl.metadata (3.0 kB)\n",
      "Collecting langchain-community<0.1,>=0.0.28 (from langchain)\n",
      "  Obtaining dependency information for langchain-community<0.1,>=0.0.28 from https://files.pythonhosted.org/packages/f9/c5/40e0fa5fddce3028052d6ae9596c5629dd6f81176c78e229c58e58409f55/langchain_community-0.0.28-py3-none-any.whl.metadata\n",
      "  Downloading langchain_community-0.0.28-py3-none-any.whl.metadata (8.3 kB)\n",
      "Collecting langchain-core<0.2.0,>=0.1.31 (from langchain)\n",
      "  Obtaining dependency information for langchain-core<0.2.0,>=0.1.31 from https://files.pythonhosted.org/packages/9d/ac/f590500b92b00f2984a33f116f4b59b32e52698ecf014fa9927135bc1c7e/langchain_core-0.1.32-py3-none-any.whl.metadata\n",
      "  Downloading langchain_core-0.1.32-py3-none-any.whl.metadata (6.0 kB)\n",
      "Collecting langchain-text-splitters<0.1,>=0.0.1 (from langchain)\n",
      "  Obtaining dependency information for langchain-text-splitters<0.1,>=0.0.1 from https://files.pythonhosted.org/packages/9d/a1/aec824080111e9b4a4802b51b988032faa193828c865e11233d1b18e88fa/langchain_text_splitters-0.0.1-py3-none-any.whl.metadata\n",
      "  Downloading langchain_text_splitters-0.0.1-py3-none-any.whl.metadata (2.0 kB)\n",
      "Collecting langsmith<0.2.0,>=0.1.17 (from langchain)\n",
      "  Obtaining dependency information for langsmith<0.2.0,>=0.1.17 from https://files.pythonhosted.org/packages/d1/c1/92361b2ad30b3fd1c5db89504ff97e55db18f87026285449457afad7f90b/langsmith-0.1.26-py3-none-any.whl.metadata\n",
      "  Downloading langsmith-0.1.26-py3-none-any.whl.metadata (13 kB)\n",
      "Requirement already satisfied: numpy<2,>=1 in c:\\users\\user\\anaconda3\\lib\\site-packages (from langchain) (1.24.3)\n",
      "Requirement already satisfied: pydantic<3,>=1 in c:\\users\\user\\anaconda3\\lib\\site-packages (from langchain) (2.5.2)\n",
      "Requirement already satisfied: requests<3,>=2 in c:\\users\\user\\anaconda3\\lib\\site-packages (from langchain) (2.31.0)\n",
      "Requirement already satisfied: tenacity<9.0.0,>=8.1.0 in c:\\users\\user\\anaconda3\\lib\\site-packages (from langchain) (8.2.2)\n",
      "Requirement already satisfied: attrs>=17.3.0 in c:\\users\\user\\anaconda3\\lib\\site-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (23.1.0)\n",
      "Requirement already satisfied: charset-normalizer<4.0,>=2.0 in c:\\users\\user\\anaconda3\\lib\\site-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (2.0.4)\n",
      "Requirement already satisfied: multidict<7.0,>=4.5 in c:\\users\\user\\anaconda3\\lib\\site-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (6.0.2)\n",
      "Requirement already satisfied: async-timeout<5.0,>=4.0.0a3 in c:\\users\\user\\anaconda3\\lib\\site-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (4.0.2)\n",
      "Requirement already satisfied: yarl<2.0,>=1.0 in c:\\users\\user\\anaconda3\\lib\\site-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (1.8.1)\n",
      "Requirement already satisfied: frozenlist>=1.1.1 in c:\\users\\user\\anaconda3\\lib\\site-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (1.4.0)\n",
      "Requirement already satisfied: aiosignal>=1.1.2 in c:\\users\\user\\anaconda3\\lib\\site-packages (from aiohttp<4.0.0,>=3.8.3->langchain) (1.2.0)\n",
      "Collecting marshmallow<4.0.0,>=3.18.0 (from dataclasses-json<0.7,>=0.5.7->langchain)\n",
      "  Obtaining dependency information for marshmallow<4.0.0,>=3.18.0 from https://files.pythonhosted.org/packages/38/04/37055b7013dfaaf66e3a9a51e46857cc9be151476a891b995fa70da7e139/marshmallow-3.21.1-py3-none-any.whl.metadata\n",
      "  Downloading marshmallow-3.21.1-py3-none-any.whl.metadata (7.2 kB)\n",
      "Collecting typing-inspect<1,>=0.4.0 (from dataclasses-json<0.7,>=0.5.7->langchain)\n",
      "  Obtaining dependency information for typing-inspect<1,>=0.4.0 from https://files.pythonhosted.org/packages/65/f3/107a22063bf27bdccf2024833d3445f4eea42b2e598abfbd46f6a63b6cb0/typing_inspect-0.9.0-py3-none-any.whl.metadata\n",
      "  Downloading typing_inspect-0.9.0-py3-none-any.whl.metadata (1.5 kB)\n",
      "Requirement already satisfied: jsonpointer>=1.9 in c:\\users\\user\\anaconda3\\lib\\site-packages (from jsonpatch<2.0,>=1.33->langchain) (2.1)\n",
      "Requirement already satisfied: anyio<5,>=3 in c:\\users\\user\\anaconda3\\lib\\site-packages (from langchain-core<0.2.0,>=0.1.31->langchain) (3.7.1)\n",
      "Collecting packaging<24.0,>=23.2 (from langchain-core<0.2.0,>=0.1.31->langchain)\n",
      "  Obtaining dependency information for packaging<24.0,>=23.2 from https://files.pythonhosted.org/packages/ec/1a/610693ac4ee14fcdf2d9bf3c493370e4f2ef7ae2e19217d7a237ff42367d/packaging-23.2-py3-none-any.whl.metadata\n",
      "  Using cached packaging-23.2-py3-none-any.whl.metadata (3.2 kB)\n",
      "Collecting orjson<4.0.0,>=3.9.14 (from langsmith<0.2.0,>=0.1.17->langchain)\n",
      "  Obtaining dependency information for orjson<4.0.0,>=3.9.14 from https://files.pythonhosted.org/packages/8c/37/3623de71a63c2182f121d9efba488ad606a9934d2f4ba3df51baf428fe96/orjson-3.9.15-cp311-none-win_amd64.whl.metadata\n",
      "  Downloading orjson-3.9.15-cp311-none-win_amd64.whl.metadata (50 kB)\n",
      "     ---------------------------------------- 0.0/50.7 kB ? eta -:--:--\n",
      "     ------------------------------ ------- 41.0/50.7 kB 991.0 kB/s eta 0:00:01\n",
      "     ---------------------------------------- 50.7/50.7 kB 1.3 MB/s eta 0:00:00\n",
      "Requirement already satisfied: annotated-types>=0.4.0 in c:\\users\\user\\anaconda3\\lib\\site-packages (from pydantic<3,>=1->langchain) (0.6.0)\n",
      "Requirement already satisfied: pydantic-core==2.14.5 in c:\\users\\user\\anaconda3\\lib\\site-packages (from pydantic<3,>=1->langchain) (2.14.5)\n",
      "Requirement already satisfied: typing-extensions>=4.6.1 in c:\\users\\user\\anaconda3\\lib\\site-packages (from pydantic<3,>=1->langchain) (4.8.0)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\user\\anaconda3\\lib\\site-packages (from requests<3,>=2->langchain) (3.4)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\user\\anaconda3\\lib\\site-packages (from requests<3,>=2->langchain) (1.26.18)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\user\\anaconda3\\lib\\site-packages (from requests<3,>=2->langchain) (2023.7.22)\n",
      "Requirement already satisfied: greenlet!=0.4.17 in c:\\users\\user\\anaconda3\\lib\\site-packages (from SQLAlchemy<3,>=1.4->langchain) (2.0.1)\n",
      "Requirement already satisfied: sniffio>=1.1 in c:\\users\\user\\anaconda3\\lib\\site-packages (from anyio<5,>=3->langchain-core<0.2.0,>=0.1.31->langchain) (1.2.0)\n",
      "Requirement already satisfied: mypy-extensions>=0.3.0 in c:\\users\\user\\anaconda3\\lib\\site-packages (from typing-inspect<1,>=0.4.0->dataclasses-json<0.7,>=0.5.7->langchain) (1.0.0)\n",
      "Downloading langchain-0.1.12-py3-none-any.whl (809 kB)\n",
      "   ---------------------------------------- 0.0/809.1 kB ? eta -:--:--\n",
      "   ----- ---------------------------------- 112.6/809.1 kB 2.2 MB/s eta 0:00:01\n",
      "   ----------- ---------------------------- 235.5/809.1 kB 2.4 MB/s eta 0:00:01\n",
      "   ---------------- ----------------------- 337.9/809.1 kB 2.3 MB/s eta 0:00:01\n",
      "   -------------------------- ------------- 532.5/809.1 kB 2.8 MB/s eta 0:00:01\n",
      "   -------------------------------- ------- 655.4/809.1 kB 3.0 MB/s eta 0:00:01\n",
      "   ------------------------------------- -- 757.8/809.1 kB 2.7 MB/s eta 0:00:01\n",
      "   ---------------------------------------- 809.1/809.1 kB 2.6 MB/s eta 0:00:00\n",
      "Downloading dataclasses_json-0.6.4-py3-none-any.whl (28 kB)\n",
      "Downloading jsonpatch-1.33-py2.py3-none-any.whl (12 kB)\n",
      "Downloading langchain_community-0.0.28-py3-none-any.whl (1.8 MB)\n",
      "   ---------------------------------------- 0.0/1.8 MB ? eta -:--:--\n",
      "   --- ------------------------------------ 0.2/1.8 MB 4.6 MB/s eta 0:00:01\n",
      "   ------ --------------------------------- 0.3/1.8 MB 3.2 MB/s eta 0:00:01\n",
      "   ----------- ---------------------------- 0.5/1.8 MB 3.7 MB/s eta 0:00:01\n",
      "   ---------------- ----------------------- 0.7/1.8 MB 3.8 MB/s eta 0:00:01\n",
      "   ------------------ --------------------- 0.8/1.8 MB 3.6 MB/s eta 0:00:01\n",
      "   ---------------------- ----------------- 1.0/1.8 MB 3.6 MB/s eta 0:00:01\n",
      "   --------------------------- ------------ 1.2/1.8 MB 3.7 MB/s eta 0:00:01\n",
      "   ------------------------------- -------- 1.4/1.8 MB 3.7 MB/s eta 0:00:01\n",
      "   ----------------------------------- ---- 1.6/1.8 MB 3.8 MB/s eta 0:00:01\n",
      "   ---------------------------------------  1.8/1.8 MB 3.9 MB/s eta 0:00:01\n",
      "   ---------------------------------------- 1.8/1.8 MB 3.7 MB/s eta 0:00:00\n",
      "Downloading langchain_core-0.1.32-py3-none-any.whl (260 kB)\n",
      "   ---------------------------------------- 0.0/260.9 kB ? eta -:--:--\n",
      "   ---------- ----------------------------- 71.7/260.9 kB 1.9 MB/s eta 0:00:01\n",
      "   -------------------------- ------------- 174.1/260.9 kB 2.6 MB/s eta 0:00:01\n",
      "   ---------------------------------------- 260.9/260.9 kB 2.3 MB/s eta 0:00:00\n",
      "Downloading langchain_text_splitters-0.0.1-py3-none-any.whl (21 kB)\n",
      "Downloading langsmith-0.1.26-py3-none-any.whl (67 kB)\n",
      "   ---------------------------------------- 0.0/67.9 kB ? eta -:--:--\n",
      "   ---------------------------------------- 67.9/67.9 kB 3.8 MB/s eta 0:00:00\n",
      "Downloading marshmallow-3.21.1-py3-none-any.whl (49 kB)\n",
      "   ---------------------------------------- 0.0/49.4 kB ? eta -:--:--\n",
      "   ---------------------------------------- 49.4/49.4 kB ? eta 0:00:00\n",
      "Downloading orjson-3.9.15-cp311-none-win_amd64.whl (136 kB)\n",
      "   ---------------------------------------- 0.0/136.0 kB ? eta -:--:--\n",
      "   --------------------------- ------------ 92.2/136.0 kB 2.6 MB/s eta 0:00:01\n",
      "   ---------------------------------------- 136.0/136.0 kB 2.7 MB/s eta 0:00:00\n",
      "Using cached packaging-23.2-py3-none-any.whl (53 kB)\n",
      "Downloading typing_inspect-0.9.0-py3-none-any.whl (8.8 kB)\n",
      "Installing collected packages: typing-inspect, packaging, orjson, jsonpatch, marshmallow, langsmith, dataclasses-json, langchain-core, langchain-text-splitters, langchain-community, langchain\n",
      "  Attempting uninstall: packaging\n",
      "    Found existing installation: packaging 23.1\n",
      "    Uninstalling packaging-23.1:\n",
      "      Successfully uninstalled packaging-23.1\n",
      "  Attempting uninstall: orjson\n",
      "    Found existing installation: orjson 3.9.10\n",
      "    Uninstalling orjson-3.9.10:\n",
      "      Successfully uninstalled orjson-3.9.10\n",
      "  Attempting uninstall: jsonpatch\n",
      "    Found existing installation: jsonpatch 1.32\n",
      "    Uninstalling jsonpatch-1.32:\n",
      "      Successfully uninstalled jsonpatch-1.32\n",
      "Successfully installed dataclasses-json-0.6.4 jsonpatch-1.33 langchain-0.1.12 langchain-community-0.0.28 langchain-core-0.1.32 langchain-text-splitters-0.0.1 langsmith-0.1.26 marshmallow-3.21.1 orjson-3.9.15 packaging-23.2 typing-inspect-0.9.0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.\n",
      "tables 3.8.0 requires blosc2~=2.0.0, which is not installed.\n",
      "tables 3.8.0 requires cython>=0.29.21, which is not installed.\n",
      "python-lsp-black 1.2.1 requires black>=22.3.0, but you have black 0.0 which is incompatible.\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "!pip install langchain\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "38e58535",
   "metadata": {},
   "outputs": [],
   "source": [
    "from apikey import apikey\n",
    "os.environ ['OPENAI_API_KEY']=  apikey"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "9c96d376",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "from langchain.llms import OpenAI"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "67032c27",
   "metadata": {},
   "outputs": [],
   "source": [
    "st.title ('RMG')\n",
    "prompt = st.text_input ('Plug in your prompt here')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "74e7ad84",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
