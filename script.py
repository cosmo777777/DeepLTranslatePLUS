import gradio as gr
import os
from deep_translator import DeeplTranslator

params = {
    "activate": True,
    "language string": "zh",
    "model_language":"en",
    "api_key":"",
    "use_free_api":True,
}

language_codes = {'bulgarian': 'bg', 'czech': 'cs', 'danish': 'da', 'german': 'de', 'greek': 'el', 'english': 'en', 'spanish': 'es', 'estonian': 'et', 'finnish': 'fi', 'french': 'fr', 'hungarian': 'hu', 'indonesian': 'id', 'italian': 'it', 'japanese': 'ja', 'lithuanian': 'lt', 'latvian': 'lv', 'dutch': 'nl', 'polish': 'pl', 'portuguese': 'pt', 'romanian': 'ro', 'russian': 'ru', 'slovak': 'sk', 'slovenian': 'sl', 'swedish': 'sv', 'turkish': 'tr', 'ukrainian': 'uk', 'chinese': 'zh'}

def input_modifier(string):
    """
    This function is applied to your text inputs before
    they are fed into the model.
    """
    if not params['activate']:
        return string

    d = DeeplTranslator(source=params['language string'], target=params['model_language'], api_key=params['api_key'],use_free_api= params['use_free_api'])

    return d.translate(string)


def output_modifier(string):
    """
    This function is applied to the model outputs.
    """
    if not params['activate']:
        return string

    d = DeeplTranslator(source=params['model_language'], target=params['language string'], api_key=params['api_key'],use_free_api= params['use_free_api'])

    return d.translate(string)


def bot_prefix_modifier(string):
    """
    This function is only applied in chat mode. It modifies
    the prefix text for the Bot and can be used to bias its
    behavior.
    """

    return string


def ui():

    language_name = list(language_codes.keys())[list(language_codes.values()).index(params['language string'])]
    model_language = list(language_codes.keys())[list(language_codes.values()).index(params['model_language'])]
    with gr.Accordion("DeepL Translate", open=True):
        with gr.Row():
            activate = gr.Checkbox(value=params['activate'], label='Activate translation')
            use_free_api = gr.Checkbox(value=params['use_free_api'], label='free api')
        with gr.Row():
            api_key = gr.Textbox(value="", placeholder="Enter api_key", label="Api-key")
        with gr.Row():
            language = gr.Dropdown(value=language_name, choices=[j for j in language_codes],
                                   label='Translated languages')
            model_language = gr.Dropdown(value=model_language, choices=[k for k in language_codes],
                                   label='Model Language')


    activate.change(lambda x: params.update({"activate": x}), activate, None)
    api_key.change(lambda x: params.update({"api_key": x}), api_key, None)
    use_free_api.change(lambda x: params.update({"use_free_api": x}), use_free_api, None)
    language.change(lambda x: params.update({"language string": language_codes[x]}), language, None)
    model_language.change(lambda x: params.update({"model_language": language_codes[x]}), model_language, None)
