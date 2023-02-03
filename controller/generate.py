from flask import Flask, Response, request,jsonify, make_response
import tensorflow as tf
import numpy as np
from flask_restful import Resource
from transformers import TFAutoModelForSeq2SeqLM
from transformers import AutoTokenizer


class summarize(Resource):
    def post(self):
        content=request.json
        sentence=content['input']
        tokenizer = AutoTokenizer.from_pretrained("./tfmodel")
        
        inputs = tokenizer(sentence, return_tensors="tf").input_ids
        model = TFAutoModelForSeq2SeqLM.from_pretrained("./tfmodel",from_pt=True)
        text =  "paraphrase: " + sentence + " </s>"
        outputs = model.generate(inputs, max_new_tokens=100, do_sample=False)
        output=tokenizer.decode(outputs[0], skip_special_tokens=True)

        print(f"Sentence: {sentence}")
        return make_response(jsonify({"Result":output,"statusCode":200}))
