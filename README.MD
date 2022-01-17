# Create Chatbot with Rasa & Python

Framework: https://rasa.com/

Install Rasa on your local `pip install rasa`

we can create a rasa project `rasa init`

## What is NLU?

NLU is “Natural Language Understanding”

We store our chatbot's data in `data` folder.
    In `nlu.yml` file, we set the intents.

`rasa shell` helps us to connect the chatbot from terminal
`rasa shell nlu` helps us to parse the input text to check the input parameter how much near intents are in `nlu.yml` file

What happens if we type something that doesn't exist in `nlu.yml` file?
    Rasa try to understand from context.

We define all responses the chatbot will response store in `domain.yml` file. 
We create stories in `data/stories.yml` file. Like flow.
We define all potential questions in `nlu.yml`

If we want to apply the changes, we need to use `rasa train`

# Entities
If we want to extract data from intent, we need to use this in `nlu.yml` file: `[VARIABLE VALUE](variable_name)`
We say "entities" for this. And we need to define all entities in `domain.yml` file
```
entities:
  - city
```


# Slots
If we want to store entities to use later by chatbot, we need to use slots. Rasa store slots as key-value pairs.
Also, we define slots in `domain.yml` file

```
slots:
  city:
    type: text
    mappings:
      - auto_fill: true
      - type: from_entity
        entity: city
```

We can use slots in texts we define for the intents like this:
`I am going to search time zone for {city}`

# Actions
If we want to create custom actions:
1. we need to update both of these files:
   - domain.yml
   - stories.yml
2. Create custom actions in `actions.py`
3. Before run the chatbot, run the actions server
    - Chatbot and actions can communicate by using this way
    - Go to `endpoints.yml` file and uncomment `action_endpoint`

`rasa run actions` runs the actions server