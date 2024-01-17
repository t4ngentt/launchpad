
# Personality Simulation | LAUNCHPAD


## Installation

1. Clone the repo
2. Install the requirements in virtual environment

```pip install -r requirements.txt```

3. Navigate to chatbot_api folder

```cd chatbot_api```

4. Run flask application 
```flask run```

5. The application will now be ready to run locally on ```localhost:5000```



    
## Environment Variables

To run this project, you will need to add the following environment variables to the config.yaml file

`API_KEY` : This is the key associated with your OpenAI account. Visit https://platform.openai.com/account/api-keys be informed about API keys.

This file is to be stored inside the virtual environment `chatbot_api`






## Routes

The only availed route is for the landing page at localhost:5000

The only other route is localhost:5000/chat, which can be accessed via POST method.


## Features

The chatbot in its current state refreshes the page after every query instance. And also does not posses any context window capabilities. Meaning each query from the user will be treated as a separate instance.

This will be fixed, where the user will be able to have a scrolling chat window, and the context window/memory to the chatbot will be implemented.

