# Docker_exercise

The following steps are required to run the API in a docker container:

```python
git clone https://github.com/inverniz/Docker_exercise
cd Docker_exercise
docker build . -t docker_exercise_image
docker run -p 5000:5000 docker_exercise_image
```

The testing of the API can happen with this kind of curl command:
```bash
curl -d '{"VisitsLastYear": 2, "QuestionTextLength": 20}' -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json"
```
