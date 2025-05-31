# //////////////////////////////////////////////////
# Testing the HF API fromt he official docs
# https://huggingface.co/docs/inference-providers/providers/hf-inference
# //////////////////////////////////////////////////

from huggingface_hub import InferenceClient
from dotenv import load_dotenv


def hfa1_main():
    pass


def hf1():
    client = InferenceClient(
        provider="hf-inference",
        api_key="hf_xxxxxxxxxxxxxxxxxxxxxxxx",
    )

    completion = client.chat.completions.create(
        model="Qwen/Qwen2.5-VL-32B-Instruct",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Describe this image in one sentence."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "https://cdn.britannica.com/61/93061-050-99147DCE/Statue-of-Liberty-Island-New-York-Bay.jpg"
                        }
                    }
                ]
            }
        ],
    )

    print(completion.choices[0].message)
