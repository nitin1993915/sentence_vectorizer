# Sentence Vectorizer Service

## Initial Setup and Local Deployment
1. Clone git repository. 
2. Install the required Python packages from the *requirements.txt* file.
3. Set Consul Env Variables.
    ```
    Currently None
    ```
4. Run `uvicorn app:app --port 8000 --host 0.0.0.0`

## Docker Deployment
1. `docker build -t contianer_registery/sent_vectorizer:version .`
2. `docker run -d -p 8000:8000 --name sent_vectorizer -t contianer_registery/sent_vectorizer:version --restart unless-stopped -e ENV1 -e ENV2  --add-host {HOST1}:{IP}`

## API Endpoints
 1. POST /vectorize_text    `Returns an array of type float and size 500 for the input text as **sentence_text**`
 2. GET /health_check       `Health Check`

## Usage

a) Extracting vectors for the sentence_text 
    ```

    sample curl  : 
    curl --location --request POST 'http://0.0.0.0:8000/nlp/v1/vectorize_text' \
    --header 'Content-Type: application/json' \
    --data-raw '{
                  "sentence_text": "This is an example sentence"
                }'
    

    sample output : {
                    "status": true,
                    "sentence_vector": [1.32, 0.393, .... 0.9312]
                    }
    ```
## Testing using FastAPI TestClient
1. Check for test_app.py and required library installed in environment (`pytest`).
2. Run `pytest`
