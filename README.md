# Run LLM on CPU

### Download and place file in same directory from below or try another model
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/blob/main/llama-2-7b-chat.Q2_K.gguf

### Setup
```sh
docker compose up -d --build
```

### View html template
http://localhost:5000/

### API endpoint
http://localhost:5000/llama
#### example post query
```python
{
  "system_message": "You are a helpful assistant. You are an expert at PostGIS and Postgresql and SQL and psql.",
  "user_message": "Generate sql query to get area of a school polygon from school table for first school",
  "max_tokens": 200
}
```
