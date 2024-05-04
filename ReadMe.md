## Step To Start Server

- First move into the server directory `cd server`
- Run the compose file `~/server/docker.compose.yml` to start the databse
- install the requirements with `pip install -r requirements.txt
`
- start the app with `python run.py`

## Step to Start UI

- First move into the UI directory with `cd ui`
- create an env file, `touch .env` and the variable:
```
VITE_API_ENDPOINT = http://localhost:8000/api
```
- Install the packages with `yarn`
- Start your app with `yarn dev`



---

## 🚨 Important Notice 🚨

# **Hello 😀, it's the weekend!**

*Less coding for the weekend*

 The UI provided here is a basic implementation and can be improved significantly with more time invested. Feel free to enhance the design, add animations, or customize it to fit your project's needs.

Additionally, consider integrating minIO for image storage. MinIO can be easily and super simply integrated with Docker or any online free service, providing a scalable solution for managing images within your application.

---




