"""

Coding Exercise
Use a web framework of your choice (Flask, Django, FastAPI, etc) to develop a single
production-quality API endpoint that takes a sentence as input and returns a random 500
dimensional array of floats. For example:
Input: “This is an example sentence”
Output: [1.32, 0.393, .... 0.9312]
Accompanying your code submission, please write a short statement justifying the
considerations you took to make your solution production-quality. What tests and checks
would you do to ensure this fits the purpose?


"""

from fastapi import APIRouter, Request, HTTPException, Header
from fastapi.responses import JSONResponse, Response
import numpy as np
# import rollbar


from schema.request_model import InputText
from schema.response_model import VectorizedText
from json.decoder import JSONDecodeError

router = APIRouter()


VECTOR_SIZE = 500


@router.post('/vectorize_text', response_model=VectorizedText, status_code=200)
async def rank_supplies(input_text: InputText):
    response = JSONResponse(content={'status': False, 'sentence_vector': []})
    try:
        if isinstance(input_text.sentence_text, str):
            random_vector = np.random.random(VECTOR_SIZE).tolist()
            response = JSONResponse(content={'status': True, 'sentence_vector': random_vector})
    # except KeyError as e:
    #     response = JSONResponse(status_code=418, content={"message": "Input payload Missing Key"})
    # except JSONDecodeError as e:
    #     # rollbar.report_message(traceback.format_exc())
    #     response = JSONResponse(status_code=422, content={"message": "The payload is not a valid JSON"})
    except Exception as e:
        raise HTTPException(status_code=500, detail="Request Failed due to Internal Issue, {}".format(e))
    return response


@router.get('/health_check', status_code=200)
async def health_check():
    random_vector = np.random.random(VECTOR_SIZE).tolist()
    result = {"status": True, 'sentence_vector': random_vector}
    resp = JSONResponse(status_code=200, content=result)
    return resp
